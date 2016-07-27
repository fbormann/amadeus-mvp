from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Course, Module
from .forms import createCourseForm, createModuleForm, createCategoryForm
# Create your views here.

def details(request, slug):
	context = {}
	print(slug)
	course = get_object_or_404(Course, slug=slug)
	context['course'] = course
	context['complement_name'] = course.name
	modules = Module.objects.filter(course__slug=slug)
	context['modules'] = modules
	return render(request, 'courses/details.html', context)

def index(request):
	context = {}
	courses = Course.objects.all()
	context['courses'] = courses
	return render(request, 'courses/index.html', context)

def category(request, slug='python'):
	context = {}
	category = get_object_or_404(Category, slug=slug)
	context['category'] = category
	#context['courses'] = Course.objects.filter(category=category)
	context['courses'] = category.course_set.filter(is_approved=True)
	return render(request, 'courses/category.html', context)

def create(request):
	context = {}
	if request.method == 'POST': #form submitted
		create_course = createCourseForm(data= request.POST)
		if create_course.is_valid():
			new_course = create_course.save(commit=False) #don't save to the database yet
			new_course.save()
			context['success'] = True
			context['create_course_form'] = createCourseForm()
			context['course_name'] = new_course.name
	else:
		context['create_course_form'] = createCourseForm()
	return render(request,'courses/add_course.html',context)

def createModule(request):
	context = {}
	if request.method == 'POST': #form submitted
		create_module = createModuleForm(data= request.POST)
		if create_module.is_valid():
			new_module = create_module.save(commit=False) #don't save to the database yet
			new_module.save()
			context['success'] = True
			context['create_module_form'] = createModuleForm()
			context['module_name'] = new_module.name
	else:
		context['create_module_form'] = createModuleForm()
	return render(request,'courses/add_module.html',context)

def createCategory(request):
	context = {}
	if request.method == 'POST': #form submitted
		create_category = createCategoryForm(data= request.POST)
		if create_category.is_valid():
			new_category = create_category.save(commit=False) #don't save to the database yet
			new_category.save()
			context['success'] = True
			context['create_category_form'] = createCategoryForm()
			context['category_name'] = new_category.name
	else:
		context['create_category_form'] = createCategoryForm()
	return render(request,'courses/add_category.html',context)