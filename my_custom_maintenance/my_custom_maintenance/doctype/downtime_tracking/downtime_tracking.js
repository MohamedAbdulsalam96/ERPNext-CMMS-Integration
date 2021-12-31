// Copyright (c) 2021, cjs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Downtime Tracking', {
	refresh: function(frm) {
		if (frm.doc.docstatus == 0 && !frm.doc.__unsaved &&  frm.doc.from_time){		
			
			// Add a button which allows user to generate maintenance work request
			frm.add_custom_button(__("Generate Maintenance Work Request"), () => {
				frm.call('create_maintenance_work_request',{ throw_if_missing: true, dt_id: frm.doc.name })
				.then(r => {
					if (r.message) {
						let new_mwr_doc = r.message;	// new maintenance work request
						frappe.set_route("Form", new_mwr_doc.doctype, new_mwr_doc.name);
					}
				})
			}).addClass("btn-primary");

			// Auto Update Machine Status
			if (frm.doc.auto_update_machine_status) {
				frm.call('update_machine_status',{ dt_id: frm.doc.name });
			}
		}


	},
	
	to_time: function(frm) {
		frm.call('calc_time_diff', {to_time: frm.doc.to_time, from_time: frm.doc.from_time}).then(r => {
			frm.set_value('downtime', r.message);
		})
	}
});
