# -*- coding: utf-8 -*-
# Copyright (c) 2021, cjs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.desk.form import assign_to
from frappe.utils import now
from my_custom_maintenance.my_custom_maintenance.doctype.machine_status.machine_status import create_new_mac_stat_log

class MaintenanceWorkOrder(Document):
	@frappe.whitelist()
	def update_machine_status(self, mwo_id, opt):
		mwo = frappe.get_doc("Maintenance Work Order", mwo_id)		
		mac_stat_list = frappe.db.get_list('Machine Status', filters={'asset': mwo.asset})
		mac_stat = frappe.get_doc('Machine Status', mac_stat_list[0])

		if opt==1:
			# mac_stat.update({'machine_status': 'Down: Under Maintenance'})
			# mac_stat.machine_status = "Down: Under Maintenance"
			mac_stat.db_set('machine_status', 'Down: Under Maintenance', commit=True)
			create_new_mac_stat_log(mac_stat.name, "Down: Under Maintenance")

		elif opt==2:
		# else:
			# mac_stat.update({'machine_status': 'Up: Idle'})
			# mac_stat.machine_status = "Up: Idle"
			mac_stat.db_set('machine_status', 'Up: Idle', commit=True)
			create_new_mac_stat_log(mac_stat.name, "Up: Idle")

		elif opt==3:
			mac_stat.db_set('machine_status', 'Down: Waiting For Maintenance', commit=True)
			create_new_mac_stat_log(mac_stat.name, "Down: Waiting For Maintenance")

		elif opt==4:
			mac_stat.db_set('machine_status', 'Down: Post Inspection', commit=True)
			create_new_mac_stat_log(mac_stat.name, "Down: Post Inspection")
			
		mac_stat.save()
	
	@frappe.whitelist()
	def populate_closed_date(self, mwo_id):
		mwo = frappe.get_doc("Maintenance Work Order", mwo_id)
		if not mwo.closed_date:
			mwo.db_set('closed_date', now())
			mwo.save(ignore_permissions=True)
			mwo.reload()

	def on_update(self):
		if self.status == "Open" and self.assign_to:			
			team_member = frappe.db.get_value('User', self.assign_to, "email")
			args = {
				'doctype': 'Maintenance Work Order',
				'assign_to': team_member,
				'name': self.name,
				'description': 'You have been assigned a maintenance work.',
				'priority': self.maintenance_priority,
				# 'date': self.planned_start_date
			}
			if not frappe.db.sql("""select owner from `tabToDo`
				where reference_type=%(doctype)s and reference_name=%(name)s and status="Open"
				and owner=%(assign_to)s""", args):
				assign_to.add(args)
	
	def get_previous_mac_stat(self, mwo_id):
		mwo = frappe.get_doc('Maintenance Work Order', mwo_id)
		mac_stat_list = frappe.db.get_list('Machine Status', filters={'asset': mwo.asset})
		ms = frappe.get_doc('Machine Status', mac_stat_list[0])
		return ms.machine_status