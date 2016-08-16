from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
import datetime


class Category(models.Model):
   name = models.CharField(_('Name'), max_length=100)
   slug = models.SlugField(_('Identifier'), max_length=100)

class Course(models.Model):

      name = models.CharField('Name', max_length=100) #VARCHAR2, precisa ter o limitante
      slug = models.SlugField('Identifier', max_length=100, unique=True)
      goals = models.TextField('Objectives', blank=True) #neste caso não preciso setar limite para o campo
      programa = models.TextField('Program',blank=True)
      is_approved = models.BooleanField('approved', default=False, blank=True)
      category = models.ForeignKey(Category, verbose_name='Categoria')
      limit = models.IntegerField('Student_Limits',default=0)
      subscription_start = models.DateTimeField(blank=True, null = True)
      subscription_finish = models.DateTimeField(blank=True, null = True)
      start_date = models.DateTimeField(blank=True, null = True)
      end_date = models.DateField(blank=True, null=True)
      image = models.ImageField(upload_to='imagens/', blank=True)



      
class Module(models.Model):

   name = models.CharField('Name', max_length = 100)
   slug = models.SlugField('Identifier', max_length = 100)
   course = models.ForeignKey(Course, on_delete= models.CASCADE,verbose_name='curso')
   visible = models.BooleanField('Visible', default=False)
   description = models.TextField('Description', blank=True)

class HomeWork(models.Model):
   name = models.CharField('Name', max_length=50)
   slug = models.SlugField('Identifier', max_length=50)
