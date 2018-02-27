from django.test import TestCase
from blog.models import Post
# Create your tests here.
class PostTests(TestCase):

	def test_str(self):
		my_title = Post(title="this is test case title")
		self.assertEquals(
				str(my_title), 'this is test case title',
			)
