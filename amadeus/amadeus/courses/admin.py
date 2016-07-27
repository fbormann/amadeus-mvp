from django.contrib import admin

# Register your models here.
from .models import Category, Course


#admin.site.register([Category, Course])

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name','slug']


class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'is_approved']
	search_fields = ['name','slug']

admin.site.register(Category, CategoryAdmin)

admin.site.register(Course, CourseAdmin)