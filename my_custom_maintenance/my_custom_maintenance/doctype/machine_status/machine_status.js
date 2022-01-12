// Copyright (c) 2021, cjs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Machine Status', {
	refresh: function(frm) {
		if (frm.doc.asset && frm.doc.workstation) {
			if (frm.doc.sync_with_nr == 0) {
				frm.set_df_property('machine_status', 'read_only', 0);
				frm.set_df_property('availability', 'read_only', 0);
				frm.set_df_property('performance', 'read_only', 0);
				frm.set_df_property('oee', 'read_only', 0);
				frm.set_df_property('pass_rate', 'read_only', 0);
			}
			else if (frm.doc.sync_with_nr == 1) {	// sync with node-red, make fields READ_ONLY since data is fetched from node-red
				frm.set_df_property('machine_status', 'read_only', 1);
				frm.set_df_property('availability', 'read_only', 1);
				frm.set_df_property('performance', 'read_only', 1);
				frm.set_df_property('oee', 'read_only', 1);
				frm.set_df_property('pass_rate', 'read_only', 1);
			}
		}
	},

	sync_with_nr: function(frm) {
		if (frm.doc.asset && frm.doc.workstation) {
			if (frm.doc.sync_with_nr == 0) {
				frm.set_df_property('machine_status', 'read_only', 0);
				frm.set_df_property('availability', 'read_only', 0);
				frm.set_df_property('performance', 'read_only', 0);
				frm.set_df_property('oee', 'read_only', 0);
				frm.set_df_property('pass_rate', 'read_only', 0);
			}
			else if (frm.doc.sync_with_nr == 1) {	// sync with node-red, make fields READ_ONLY since data is fetched from node-red

				// frm.call('check_if_API_exist',{ ms_id: frm.doc.name});
				frm.call('check_if_API_exist').then(r => {	// check if there is a Server Script API named as "Mac Stat From NR To ERPNext"
					if (r.message == "API not found") {
						frappe.msgprint({
							title: __('Warning: Fail to sync.'),
							indicator: 'red',
							message: __('Reason: Server Scipt API: "Mac Stat From NR To ERPNext" not found. Please name your API correctly.'),
						});
						frm.reload_doc();
					}
					else if (r.message == "API exists") {	// API exists
						frm.set_df_property('machine_status', 'read_only', 1);
						frm.set_df_property('availability', 'read_only', 1);
						frm.set_df_property('performance', 'read_only', 1);
						frm.set_df_property('oee', 'read_only', 1);
						frm.set_df_property('pass_rate', 'read_only', 1);
					}
				});
			}
		}
	},

	// before saving, check if mahcine status has changes
	validate: function (frm) {
		if (frm.doc.log_machine_status) {	// machine status logging checkbox checked

			frm.call('get_previous_mac_stat', {ms_id: frm.doc.name}).then(r => {
				let previous_mac_stat = r.message;

				if (previous_mac_stat != frm.doc.machine_status) {
					// machine status has changed, create a new Machine Status Log
					console.log("inside if frm New mac stat: " + frm.doc.machine_status);
					frappe.call('my_custom_maintenance.my_custom_maintenance.doctype.machine_status.machine_status.create_new_mac_stat_log', {ms_id: frm.doc.name, new_mac_stat: frm.doc.machine_status});
				}
			})
		}
	},
});