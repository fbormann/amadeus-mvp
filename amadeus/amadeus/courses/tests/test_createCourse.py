
from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class createCourseTest(TestCase):
	"Teste para a criacao de Cursos"

	def setUp(self):
		self.client = Client()
		self.url = reverse('create')


	def test_criar_curso_ok(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	def test_criar_curso_error(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)