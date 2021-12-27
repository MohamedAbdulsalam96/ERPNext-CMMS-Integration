# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "My Custom Maintenance",
			"category": "Modules",
			"color": "labc9c",
			#"icon": "assets/my_custom_maintenance/images/SHRDC.svg",
			"icon": "fa fa-cogs",
			"type": "module",
			"label": _("SHRDC CMMS"),
			"description":"Downtime Tracking, Corrective and Preventive Maintenance."
		}
	]
