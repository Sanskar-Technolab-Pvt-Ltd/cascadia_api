import frappe

@frappe.whitelist()
def get_system_manager_users(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""
		select u.name, concat(u.first_name, ' ', u.last_name)
		from tabUser u, `tabHas Role` r
		where u.name = r.parent and r.role = 'Projects Manager' 
		and u.enabled = 1 and u.name like %s
	""", ("%" + txt + "%"))