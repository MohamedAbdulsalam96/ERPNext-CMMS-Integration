// Copyright (c) 2021, cjs and contributors
// For license information, please see license.txt

frappe.ui.form.on('Maintenance Work Order', {

	// <Value of status field> (<docstatus>)
	// Open (0)
	// Work In Progress (0)
	// On Hold (0)
	// Completed, Pending Approval from Maintenance Manager (0)
	// Closed (1)
	// Cancelled (2)
	//
	// Update the machine status accordingly. Possible machine status are:
	// Up: Idle
	// Up: Running
	// Down: Scheduling Maintenance
	// Down: Waiting For Maintenance
	// Down: Under Maintenance
	// Down: Post Inspection
	refresh: function(frm) {
		if (frm.doc.status == "Open" && frm.doc.docstatus == 0 && frm.doc.planned_start_date && frm.doc.planned_complete_date && frm.doc.auto_update_machine_status) {
			// machine maintenance has been scheduled, waiting for maintenance
			frm.call('update_machine_status',{ mwo_id: frm.doc.name, opt: 3 });
		}

		if (frm.doc.status == "Work In Progress" && frm.doc.docstatus == 0 && frm.doc.auto_update_machine_status) {
			// machine under maintenance
			frm.call('update_machine_status',{ mwo_id: frm.doc.name, opt: 1 });
		}

		if (frm.doc.status == "Completed, Pending Approval from Maintenance Manager" && frm.doc.docstatus == 0 && frm.doc.auto_update_machine_status) {
			// machine maintenance completed, waiting for Maintenance Manager's Post Inspection
			frm.call('update_machine_status',{ mwo_id: frm.doc.name, opt: 4 });
		}

		if (frm.doc.docstatus == 1 && frm.doc.auto_update_machine_status) {
			// machine ready to operate
			frm.call('update_machine_status',{ mwo_id: frm.doc.name, opt: 2 });
		}

		// When status = 'Work In Progress', auto populate Actual Start Date
		if (frm.doc.status == "Work In Progress" && !frm.doc.actual_start_date) {
			frm.set_value('actual_start_date', frappe.datetime.now_datetime());
			frm.save();
		}

		// When status = 'Completed, Pending Approval from Maintenance Manager', auto populate Actual Complete Date
		if (frm.doc.status == "Completed, Pending Approval from Maintenance Manager" && !frm.doc.actual_complete_date) {
			frm.set_value('actual_complete_date', frappe.datetime.now_datetime());
			frm.save();
		}

		// When status = 'Closed', auto populate Closed Date
		if (frm.doc.docstatus == 1 && !frm.doc.closed_date) {			
			frm.call('populate_closed_date',{ mwo_id: frm.doc.name }).then(r => {
				frm.reload_doc();
			});
		}
	},
});