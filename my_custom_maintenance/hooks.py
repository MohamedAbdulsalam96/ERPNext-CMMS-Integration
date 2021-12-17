# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "my_custom_maintenance"
app_title = "My Custom Maintenance"
app_publisher = "cjs"
app_description = "Track status of workstations, schedule and manage corrective and preventive maintenance."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "chiajunshen8@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/my_custom_maintenance/css/my_custom_maintenance.css"
# app_include_js = "/assets/my_custom_maintenance/js/my_custom_maintenance.js"

# include js, css files in header of web template
# web_include_css = "/assets/my_custom_maintenance/css/my_custom_maintenance.css"
# web_include_js = "/assets/my_custom_maintenance/js/my_custom_maintenance.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "my_custom_maintenance.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "my_custom_maintenance.install.before_install"
# after_install = "my_custom_maintenance.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "my_custom_maintenance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"my_custom_maintenance.tasks.all"
# 	],
# 	"daily": [
# 		"my_custom_maintenance.tasks.daily"
# 	],
# 	"hourly": [
# 		"my_custom_maintenance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"my_custom_maintenance.tasks.weekly"
# 	]
# 	"monthly": [
# 		"my_custom_maintenance.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "my_custom_maintenance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "my_custom_maintenance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "my_custom_maintenance.task.get_dashboard_data"
# }

