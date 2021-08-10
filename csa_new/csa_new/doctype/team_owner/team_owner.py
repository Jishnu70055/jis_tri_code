# Copyright (c) 2021, sd and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
from datetime import date
from datetime import datetime
import frappe
from frappe.model.document import Document
import random

class TeamOwner(Document):
	def before_save(self):
		date_stamp = self.dob
		dob = datetime.strptime(date_stamp, '%Y-%m-%d')
		month = str(dob.strftime('%m'))
		day = str(dob.strftime('%d'))
		year = str(dob.strftime('%y'))
		id = str(self.first_name[0]) + str(self.last_name[0])+str(year)+str(month)+str(day)
		if self.gender == 'Male':
			self.user_name = id + str(random_number_males())
			user_creation(self)
		if self.gender == 'Female':
			self.user_name = id + str(random_number_females())
			user_creation(self)
		if self.gender == 'Other':
			self.user_name = id + str(random_number_others())
			user_creation(self)


def user_creation(self):
	user = frappe.new_doc('User')
	user.email = str(self.first_name) + 'xxyyzz1100@gmail.com'
	user.first_name = self.first_name
	user.last_name = self.last_name
	user.username = self.user_name
	user.save(ignore_permissions=True)
	user_modifiy = frappe.get_doc('User' ,user.name)
	user_modifiy.update({
		"doctype":"User",
		"role_profile_name":"Team Owner",
		"logout_all_sessions":1
	})
	user_modifiy.save(ignore_permissions=True)


def random_number_males():
	for rand_num in [random.randrange(*sorted([4000,8999])) for i in range(10)]:
		return rand_num


def random_number_females():
	for rand_num in [random.randrange(*sorted([0,3999])) for i in range(10)]:
		return rand_num


def random_number_others():
	for rand_num in [random.randrange(*sorted([9000,9999])) for i in range(10)]:
		return rand_num

