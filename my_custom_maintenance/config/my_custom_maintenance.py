from __future__ import unicode_literals
from frappe import _

def get_data():
    config = [
        # {
        #     "label": _("Dashboard"),
        #     "items":[
        #         {
        #             "type": "page",
        #             "name": "test-page",
        #             "label": _("MES Dashboard"),
        #             "onboard": 1
        #         }
        #     ]
		# },
		{
            "label": _("Machine Status"),
            "items":[
                {
                    "type": "doctype",
                    "name": "Machine Status",
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Machine Status Log",
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Machine Availability Log",
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Machine Performance Log",
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