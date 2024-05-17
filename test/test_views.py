import unittest
from django.test import TestCase
from django.test import Client
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from apl.models import Img, Post, Category
from apl.forms import AddPost

class TestViewsdd(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.image = Img.objects.create(image='image.jpg')
        self.category1 = Category.objects.create(name='cat1')
        self.category2 = Category.objects.create(name='cat2')
        self.category3 = Category.objects.create(name='cat3')
        self.post1 = Post.objects.create(content='post1')
        self.post1.categories.add(self.category1)
        self.post2 = Post.objects.create(content='post2')
        self.post2.categories.add(self.category2)
        
        response = self.client.get(reverse('show') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['teg']), 4)

    def test_create_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('create'), {'content': 'new post'})
        self.assertEqual(response.status_code, 302)

        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 302)
        add_form = AddPost()
        response = self.client.post(reverse('create'), {'content': 'new post'})
        self.assertEqual(response.status_code, 302)