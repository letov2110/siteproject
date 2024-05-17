import unittest
from django.test import TestCase
from datetime import datetime, timedelta
from apl.models import *
from forum.models import * 

########
'''apl'''
class TestCategoryModel(unittest.TestCase):
    def create_category(self):
        category = Category(name='ubuntu')
        self.assertTrue(category.name == 'ubuntu')
    def str_method(self):
        category = Category(name='ubuntu')
        self.assertEqual(str(category), 'ubuntu')

class TestPostModel(unittest.TestCase):
    def test_categories(self):
        category = Category(name='ubuntu')
        category.save()
        post = Post(title='command', content='blablabla')
        post.save()
        post.categories.add(category)
        self.assertIn(category, post.categories.all())
    def create_post(self):
        post = Post(title='command', content='blablabla')
        self.assertTrue(post.title == 'command')
        self.assertTrue(post.content == 'blablabla')
    def str_method(self):
        post = Post(title='command')
        self.assertEqual(str(post), 'command')

###########
# '''forum'''
class TestCatModel(unittest.TestCase):
    def create_category(self):
        category = Cat_topics(name='errors')
        self.assertTrue(category.name == 'errors')
    def str_method(self):
        category = Cat_topics(name='errors')
        self.assertEqual(str(category), 'errors')

class TestForumQuestionModel(unittest.TestCase):
    def quest_cat(self):
        category=Cat_topics(name="errors")
        category.save()
        post = Forum_Question(
            title="aaaaaaaaa",
            text= "more aaa",
            author = "user",
            views ="0",
            date=datetime.now(),
            cat_topic="errors"
            )
        post.save()
        post.category.add(category)
        self.assertIn(category, post.categories.all())
    def create_quest(self):
        post= Forum_Question(
            title="aaaaaaaaa",
            text= "more aaa",
            author = "user",
            views ="60",
            date=datetime.now(),
            cat_topic="errors"
            )
        self.assertTrue(post.title == 'aaaaaaaaa')
        self.assertTrue(post.text =='more aaa')
        self.assertTrue(post.author== 'user')
        self.assertTrue(post.views == '60')
        self.assertTrue(post.date == datetime.now())
        self.assertTrue(post.cat_topic== 'errors')
    def str_method(self):
        post = Forum_Question(title='aaaaaaaa')
        self.assertEqual(str(post), 'aaaaaaaa')
        cat_post = Cat_topics(name='errors')
        self.assertEqual(str(cat_post), 'errors')
        post_answer = Forum_Answer(text='asd asd asd')
        self.assertEqual(str(post_answer), 'asd asd asd')