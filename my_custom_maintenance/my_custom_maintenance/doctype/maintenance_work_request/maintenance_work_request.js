// Copyright (c) 2021, cjs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Maintenance Work Request', {
	refresh(frm) {
		if (frm.doc.docstatus == 1){
			
			frm.add_custom_button(__("Generate Maintenance Work Order"), () => {
				frm.call('create_maintenance_work_order',{ throw_if_missing: true, mwr_id: frm.doc.name })
				.then(r => {
					if (r.message) {
						let new_mwo_doc = r.message;	// new maintenance work order
						frappe.set_route("Form", new_mwo_doc.doctype, new_mwo_doc.name);
					}
				})
			}).addClass("btn-primary");
		}
	}
});
