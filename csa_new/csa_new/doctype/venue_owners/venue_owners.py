# Copyright (c) 2021, sd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VenueOwners(Document):
	def before_save(self):
		user_creation(self)


def user_creation(self):
	user = frappe.new_doc('User')
	user.email = self.email_id
	user.first_name = self.venue_name
	# user.last_name = self.last_name
	# user.username = self.user_name
	user.save(ignore_permissions=True)
	user_modifiy = frappe.get_doc('User' ,user.name)
	user_modifiy.update({
		"doctype":"User",
		"role_profile_name":"Venue Owner",
		"logout_all_sessions":1
	})
	user_modifiy.save(ignore_permissions=True)
