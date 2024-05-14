from django.test import TestCase
from django.contrib.auth import get_user_model
from recipes.models import Recipe, RecipeIngredient


User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user("arifpaiman",password="123123")

    def test_user_pw(self):
        self.assertTrue(self.user_a)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user("arifpaiman",password="123123")
    def test_user_count(self):
        q = User.objects.all()
        self.assertEqual(q.count(), 1)

    def test_user_recipe_count(self):
        User = self.user_a
        qs = User.recipe_set.all()
        self.assertTrue(qs.count(), 1)