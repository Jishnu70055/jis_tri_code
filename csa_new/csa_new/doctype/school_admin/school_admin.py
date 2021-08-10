# Copyright (c) 2021, sd and contributors
# For license information, please see license.txt

# from _typeshed import Self
import frappe
from frappe.model.document import Document

class SchoolAdmin(Document):
	def before_save(self):
		user_creation(self)


def user_creation(self):
	user = frappe.new_doc('User')
	user.email = self.email_id
	user.first_name = self.school_name
	# user.last_name = self.last_name
	# user.username = self.user_name
	user.save(ignore_permissions=True)
	user_modifiy = frappe.get_doc('User' ,user.name)
	user_modifiy.update({
		"doctype":"User",
		"role_profile_name":"School Admin",
		"logout_all_sessions":1
	})
	user_modifiy.save(ignore_permissions=True)