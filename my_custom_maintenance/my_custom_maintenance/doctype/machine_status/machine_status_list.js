frappe.listview_settings['Machine Status'] = {
	
	add_fields: ['machine_status'],

	hide_name_column: true,

	get_indicator: function(doc) {
		// doc.status = doc.machine_status;
		if (doc.machine_status == "Up: Idle") {
			return [__("Up: Idle"), "orange", "machine_status,=,Up: Idle"];
		} else if (doc.machine_status === "Up: Running") {
			return [__("Up: Running"), "green", "machine_status,=,Up: Running"];
		} else if (doc.machine_status == "Down: Scheduling Maintenance") {
			return [__("Down: Scheduling Maintenance"), "red", "machine_status,=,Down: Scheduling Maintenance"];
		} else if (doc.machine_status == "Down: Waiting For Maintenance") {
			return [__("Down: Waiting For Maintenance"), "red", "machine_status,=,Down: Waiting For Maintenance"];
		} else if (doc.machine_status === "Down: Under Maintenance") {
			return [__('Down: Under Maintenance'), "red", "machine_status,=,Down: Under Maintenance"];
		} else if (doc.machine_status === "Down: Post Inspection") {
			return [__('Down: Post Inspection'), "red", "machine_status,=,Down: Post Inspection"];
		}
	}
};