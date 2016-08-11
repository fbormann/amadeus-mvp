from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Course, Module
from .forms import createCourseForm, createModuleForm, createCategoryForm

from django.views import generic
# Create your views here.

class IndexView(generic.ListView):

	queryset = Course.objects.filter(is_approved=True)
	template_name = 'courses/index.html'
	context_object_name = 'courses'
	paginate_by = 3


class detailView(generic.DetailView):
	model = Course

	template_name = "courses/details.html"
	
	def get_context_data(self, **kwargs):
		print(self.kwargs)
		context = {}
		course = get_object_or_404(Course, slug=self.kwargs['slug'])
		context['course'] = course
		context['complement_name'] = course.name
		modules = Module.objects.filter(course__slug=self.kwargs['slug'])
		context['modules'] = modules
		return context


class ListByCategory(generic.ListView):

	template_name = 'courses/category.html'
	context_object_name = 'courses'
	paginate_by = 4

def category(request, slug='python'):
	context = {}
	category = get_object_or_404(Category, slug=slug)
	context['category'] = category
	#context['courses'] = Course.objects.filter(category=category)
	context['courses'] = category.course_set.filter(is_approved=True)
	return render(request, 'courses/category.html', context)


class CreateView(generic.CreateView):
	model = Course
	fields = ('name','slug','is_approved', 'category')
	

	def post(self, request):
		context = {}
		create_course = createCourseForm(data=request.POST)
		if create_course.is_valid():
			new_course = create_course.save(commit=False) #So it's not save right now
			new_course.save() #now it was actually saved
			context['success'] = True
			context['create_course_form'] = createCourseForm()
			context['course_name'] = new_course.name

		return render(request, 'courses/add_course.html', context)

	def get(self, request):
		context = {}
		context['create_course_form'] = createCourseForm()
		return render(request, 'courses/add_course.html', context)

class CreateModuleView(generic.CreateView):
	model = Module
	fields = ('name','slug','course','visible','description')

	def post(self, request):
		context = {}
		create_module = createModuleForm(data= request.POST)
		if create_module.is_valid():
			new_module = create_module.save(commit=False) #don't save to the database yet
			new_module.save()
			context['success'] = True
			context['create_module_form'] = createModuleForm()
			context['module_name'] = new_module.name

		return render(request,'courses/add_module.html',context)

	def get(self, request):
		context = {}
		context['create_module_form'] = createModuleForm()
		return render(request,'courses/add_module.html',context)


class CreateCategoryView(generic.CreateView):
	model = Module
	fields = ['name','slug']

	def post(self, request):
		context = {}
		create_category = createCategoryForm(data= request.POST)
		if create_category.is_valid():
			new_category = create_category.save(commit=False) #don't save to the database yet
			new_category.save()
			context['success'] = True
			context['create_category_form'] = createCategoryForm()
			context['module_name'] = new_category.name

		return render(request,'courses/add_category.html',context)

	def get(self, request):
		context = {}
		context['create_category_form'] = createCategoryForm()
		return render(request,'courses/add_category.html.html',context)

