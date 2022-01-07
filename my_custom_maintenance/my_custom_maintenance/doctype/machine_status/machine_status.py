# -*- coding: utf-8 -*-
# Copyright (c) 2021, cjs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MachineStatus(Document):

	# return True if API exist in database, otherwise return False.
	@frappe.whitelist()
	def check_if_API_exist(self):
		if frappe.db.exists("Server Script", "Mac Stat From NR To ERPNext"):
			return "API exists"
		else:
			return "API not found"