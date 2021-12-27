# -*- coding: utf-8 -*-
# Copyright (c) 2021, cjs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from typing import Any
import frappe
from frappe.model.document import Document

class MaintenanceWorkRequest(Document):
	@frappe.whitelist()
	def create_maintenance_work_order(self, throw_if_missing, mwr_id):	# mwr = maintenance work request
		mwr = frappe.get_doc("Maintenance Work Request", mwr_id)
		mwo = frappe.new_doc("Maintenance Work Order")
		
		mwo.update({
			'status': 'Open',
			'asset': mwr.asset,
			'raised_by': mwr.raised_by,
			'maintenance_type': mwr.request_type,
			'maintenance_priority': mwr.request_priority,
			'maintenance_work_request': mwr.name
			})

		mwo.insert(
			ignore_mandatory=True
			)
		
		if not frappe.db.exists(mwo.doctype, mwo.name):
			if throw_if_missing:
				frappe.throw('Linked document not found')
		return frappe.get_doc(mwo.doctype, mwo.name)