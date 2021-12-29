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