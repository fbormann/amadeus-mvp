from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^edit/$',views.edit_user,name='edit_user'),
	url(r'^register/$', views.RegistrationView.as_view(), name='register_user')
]