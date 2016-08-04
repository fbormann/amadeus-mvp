from django.conf.urls import url 

from . import views



urlpatterns = [
	url(r'^cursos/$', views.IndexView.as_view(), name='index'),
	url(r'^cursos/(?P<slug>\w+)/$', views.detailView.as_view(), name='details'),
	url(r'^categorias/([\w_-]+)/$', views.category, name='categories'),
	url(r'^create/curso$', views.create, name='create'),
	url(r'^create/module$', views.createModule, name='create_module'),
	url(r'^create/categoria$', views.createCategory, name='create_category')
]