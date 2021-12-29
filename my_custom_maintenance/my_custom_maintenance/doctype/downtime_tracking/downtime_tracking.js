// Copyright (c) 2021, cjs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Downtime Tracking', {
	// refresh: function(frm) {

	// }
	
	to_time: function(frm) {
		frm.call('calc_time_diff', {to_time: frm.doc.to_time, from_time: frm.doc.from_time}).then(r => {
			frm.set_value('downtime', r.message);
		})
	}
});
