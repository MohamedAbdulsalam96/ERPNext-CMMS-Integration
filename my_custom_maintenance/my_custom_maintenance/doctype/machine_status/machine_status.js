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
});