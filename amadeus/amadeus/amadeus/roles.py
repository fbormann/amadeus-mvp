from rolepermissions.roles import AbstractUserRole

class Student(AbstractUserRole):
	available_permissions = {
		'register_in_course': True,
	}