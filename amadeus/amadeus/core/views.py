from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	#return HttpResponse('Testando algo novo')#HTTP response funciona
	return render(request, "core/index.html")

def test(request):
	return render(request, "core/test.html")