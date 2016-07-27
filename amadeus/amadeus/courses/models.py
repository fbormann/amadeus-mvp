from django.db import models
from django.utils import timezone
import datetime

class Category(models.Model):
   name = models.CharField('Nome', max_length=100)
   slug = models.SlugField('Identificador', max_length=100)

class Course(models.Model):

      name = models.CharField('Nome', max_length=100) #VARCHAR2, precisa ter o limitante
      slug = models.SlugField('Identificador', max_length=100, unique=True)
      goals = models.TextField('Objetivos', blank=True) #neste caso não preciso setar limite para o campo
      programa = models.TextField('Programa',blank=True)
      is_approved = models.BooleanField('Aprovado', default=False, blank=True)
      category = models.ForeignKey(Category, verbose_name='Categoria')
      limit = models.IntegerField('Limite_Alunos',default=0)
      subscription_start = models.DateTimeField(default=timezone.now)
      subscription_finish = models.DateTimeField(default=timezone.now)
      start_date = models.DateTimeField(default=datetime.date.today)
      end_date = models.DateField(default=datetime.date.today)
      image = models.ImageField(upload_to='static/images', blank=True)



      
class Module(models.Model):

   name = models.CharField('Nome', max_length = 100)
   slug = models.SlugField('Identificador', max_length = 100)
   course = models.ForeignKey(Course, on_delete= models.CASCADE,verbose_name='curso')
   visible = models.BooleanField('Visivel', default=False)
   description = models.TextField('Descricao', blank=True)

class HomeWork(models.Model):
   name = models.CharField('Nome', max_length=50)
   slug = models.SlugField('Identificador', max_length=50)
