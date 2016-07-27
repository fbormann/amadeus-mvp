from .models import Course, Category, Module
from django import forms

class createCourseForm(forms.ModelForm):
	"""def __init__(self, *args, **kwargs):
		super(createCourseForm, self).__init__(*args, **kwargs)"""
	

	class Meta:
		model = Course
		fields = ('name','slug','goals','is_approved','limit', 'category', 'image') #I am able to set which fields I want


class createCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug')
    
class createModuleForm(forms.ModelForm):
	class Meta:
		model = Module
		fields = ('name','slug','course','visible','description')