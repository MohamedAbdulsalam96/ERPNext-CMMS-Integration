# -*- coding: utf-8 -*-
# Copyright (c) 2021, cjs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_hours

class DowntimeTracking(Document):
	@frappe.whitelist()
	def calc_time_diff(self, to_time, from_time):
		return time_diff_in_hours(to_time, from_time) * 60

	@frappe.whitelist()
	def create_maintenance_work_request(self, throw_if_missing, dt_id):	# dt = downtime tracking
		dt = frappe.get_doc("Downtime Tracking", dt_id)
		mwr = frappe.new_doc("Maintenance Work Request")
		
		mwr.update({
			'status': "Pending Approval from Maintenance Manager",
			'workflow_state': "Pending",
			'asset': dt.asset,
			'raised_by': dt.owner,
			'downtime_tracking': dt.name,
			'workstation': dt.workstation
			})

		mwr.insert(
			ignore_mandatory=True
			)
		
		if not frappe.db.exists(mwr.doctype, mwr.name):
			if throw_if_missing:
				frappe.throw('Linked document (Maintenance Work Request) not found')
		return frappe.get_doc(mwr.doctype, mwr.name)
	
	@frappe.whitelist()
	def update_machine_status(self, dt_id):
		dt = frappe.get_doc("Downtime Tracking", dt_id)		
		mac_stat_list = frappe.db.get_list('Machine Status', filters={'asset': dt.asset})
		mac_stat = frappe.get_doc('Machine Status', mac_stat_list[0])

		# mac_stat.update({'machine_status': 'Down: Under Maintenance'})
		# mac_stat.machine_status = "Down: Under Maintenance"
		mac_stat.db_set('machine_status', 'Down: Scheduling Maintenance', commit=True)	
		mac_stat.save()
		mac_stat.reload()
		# mac_stat.save(ignore_permissions=True)
		# frappe.db.commit()
		# mac_stat.reload()
		# return True