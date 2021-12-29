frappe.listview_settings['SHRDC Lvl 4 RFID Based Production Line'] = {
	
	add_fields: ['machine_status'],

	hide_name_column: true,

	get_indicator: function(doc) {
		// doc.status = doc.machine_status;
		if (doc.machine_status == "Up: Idle") {
			return [__("Up: Idle"), "lightblue", "machine_status,=,Up: Idle"];
		} else if (doc.machine_status === "Up: Running") {
			return [__("Up: Running"), "green", "machine_status,=,Up: Running"];
		} else if (doc.machine_status == "Down: Waiting For Maintenance") {
			return [__("Down: Waiting For Maintenance"), "orange", "machine_status,=,Down: Waiting For Maintenance"];
		} else if (doc.machine_status === "Down: Under Maintenance") {
			return [__('Down: Under Maintenance'), "red", "machine_status,=,Down: Under Maintenance"];
		}
	}
};