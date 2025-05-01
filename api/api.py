import frappe

@frappe.whitelist()
def get_system_manager_users(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""
		select u.name, concat(u.first_name, ' ', u.last_name)
		from tabUser u, `tabHas Role` r
		where u.name = r.parent and r.role = 'Projects Manager' 
		and u.enabled = 1 and u.name like %s
	""", ("%" + txt + "%"))


@frappe.whitelist()
def get_linked_team_members(doctype, txt, searchfield, start, page_len, filters):
	project = filters.get("project")
	if not project:
		return []

	return frappe.db.sql("""
        SELECT user, user
        FROM `tabLinked Team Member 2`
        WHERE parent = %(project)s
        AND user LIKE %(txt)s
        LIMIT %(start)s, %(page_len)s
    """, {
        "project": project,
        "txt": f"%{txt}%",
        "start": start,
        "page_len": page_len
    })