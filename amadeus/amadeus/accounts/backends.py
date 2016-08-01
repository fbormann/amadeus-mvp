from django.contrib.auth.backends import ModelBackEnd as BaseModelBackEnd

from .models import User

class ModelBackEnd(BaseModelBackEnd):

	def authenticate(self, username=None,password =None, **kwargs):
		if not username is None:
			try:
				user = User.objecst.get(username=username)
				if user.check_password(password):
					return user
			except User.DoesNotExit:
				pass