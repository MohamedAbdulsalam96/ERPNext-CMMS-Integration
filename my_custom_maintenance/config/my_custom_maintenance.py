from __future__ import unicode_literals
from frappe import _

def get_data():
    config = [
		{
            "label": _("Downtime Tracking"),
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
                    "name": "Maintenance Work Order",
                    "onboard": 1
                }
            ]
		}
	]
    return config