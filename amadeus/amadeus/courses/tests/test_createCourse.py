
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from courses.models import Category

class createCourseTest(TestCase):
	"Teste para a criacao de Cursos"

	def setUp(self):
		self.client = Client()
		self.url = reverse('courses:create')


	def test_criar_curso_ok(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed('courses/add_course.html')
		c = Category(name='teste', slug='teste')
		self.data = {'name':'teste','slug':'curso-test', 'is_approved':True, 'category': c}
		response = self.client.post(self.url, self.data)
		print(response.context)
		self.assertEquals(response.status_code, 200)
		self.assertTrue('success' in response.context)

	def test_criar_curso_error(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed('courses/create.html')
		self.data = {'name':'dsadfdsggsdfgdsfgdfsgdfgdfgdsfgdfgdfgdfgdsdfgdfgffdfdfsdfgdfsgdsfgdsfgsdfgdsfgdfgfgdfgdsfgdfgsdfgdfgdfsgdfsgdfgsdfgdfsgdsfgdsfgdfsgfsdgdsfgsddfggddgfd'}
		response = self.client.post(self.url, self.data)
		print("Criar curso com erro")
		print(response.context)
