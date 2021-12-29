from __future__ import unicode_literals
from frappe import _

def get_data():
    config = [
		{
            "label": _("Machine Status"),
            "items":[
                {
                    "type": "doctype",
                    "name": "SHRDC Lvl 4 RFID Based Production Line",
                    "onboard": 1
                }
            ]
		},
		{
            "label": _("Downtime"),
            "items":[
                {
                    "type": "doctype",
                    "name": "Downtime Tracking",
                    "onboard": 1
                }
            ]
		},
		{
            "label": _("Maintenance"),
            "items":[
                {
                    "type": "doctype",
                    "name": "Maintenance Work Request",
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Maintenance Work Order",
                    "onboard": 1
                }
            ]
		}
	]
    return config