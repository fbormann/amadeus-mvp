from ..models import Module

from django import template

from ..views import ListModuleView

register = template.Library()


@register.inclusion_tag('courses/list_module.html')
def module_list(request, slug):
	request.slug = slug
	return ListModuleView.as_view()(request)