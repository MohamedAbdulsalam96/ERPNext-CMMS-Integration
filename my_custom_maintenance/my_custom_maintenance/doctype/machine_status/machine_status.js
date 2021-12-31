// Copyright (c) 2021, cjs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Machine Status', {
	// refresh: function(frm) {
	// },

	source: function(frm) {
		if (frm.doc.asset && frm.doc.workstation) {
			if (frm.doc.source == "ERPNext") {
				frm.set_df_property('machine_status', 'read_only', 0);
				frm.set_df_property('availability', 'read_only', 0);
				frm.set_df_property('performance', 'read_only', 0);
				frm.set_df_property('oee', 'read_only', 0);
				frm.set_df_property('pass_rate', 'read_only', 0);
			}
			else if (frm.doc.source == "Node-RED") {
				frm.set_df_property('machine_status', 'read_only', 1);
				frm.set_df_property('availability', 'read_only', 1);
				frm.set_df_property('performance', 'read_only', 1);
				frm.set_df_property('oee', 'read_only', 1);
				frm.set_df_property('pass_rate', 'read_only', 1);
			}
		}
	}
});