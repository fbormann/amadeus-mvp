from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import UserForm, RegisterForm
from django.views import generic
from .models import User
from rolepermissions.shortcuts import assign_role

@login_required
def edit_user(request):
	form = UserForm(data=request.POST or None, instance=request.user)
	context = {}
	if form.is_valid():
		form.save()
		context['success'] = True
	context['form'] = form
	return render(request, 'accounts/edit.html', context)


class RegistrationView(generic.CreateView):
	form_class = RegisterForm
	model = User
	template_name = "accounts/register.html"

	def form_valid(self, form):
		obj = form.save(commit=False)
		assign_role(form.instance,'student')
		obj.set_password(User.objects.make_random_password())
		obj.save()
		context = self.get_context_data(form=form)
		context['success'] = True
		return self.render_to_response(context)