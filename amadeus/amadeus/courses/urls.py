from django.conf.urls import url 

from . import views



urlpatterns = [
	url(r'^cursos/$', views.IndexView.as_view(), name='index'),
	url(r'^cursos/(?P<slug>([\w_-]+))/$', views.detailView.as_view(), name='details'),
	url(r'^categorias/([\w_-]+)/$', views.category, name='categories'),
	url(r'^create/curso$', views.CreateView.as_view(), name='create'),
	url(r'^create/module$', views.CreateModuleView.as_view(), name='create_module'),
	url(r'^create/categoria$', views.CreateCategoryView.as_view(), name='create_category')
]