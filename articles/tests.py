from django.test import TestCase
from .models import Article
from django.utils.text import slugify
from .utils import slugify_instance_title

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_Articles = 5
        for i in range(0,  self.number_of_Articles):
             Article.objects.create(title="hello world", content="somthingelse")
    def test_queryset_exist(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(),  self.number_of_Articles)

    def test_helloworld_slug(self):
        obj = Article.objects.all().order_by("id").first()
        title = obj.title
        slug = obj.slug
        slugifyed_title = slugify(title)
        self.assertEqual(slug, slugifyed_title)

    def test_helloworld_slug(self):
        qs = Article.objects.all().exclude(slug__iexact="hello-world")
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugifyed_title = slugify(title)
            self.assertNotEqual(slug, slugifyed_title)

    def test_slugify_instance_title(self):
        lastobj = Article.objects.all().last()
        new_slugs = []
        for i in range(0, 5):
            lastinstance = slugify_instance_title(lastobj, save=False)
            new_slugs.append(lastinstance.slug)
            unique_slugs = list(set(new_slugs))
            self.assertEqual(len(new_slugs),len(unique_slugs))

    def slugify_instance_title_redux(self):
        slug_list = Article.objects.all().values_list(slug, flat=True)
        unique_slug = list(set(slug_list))
        self.assertEqual(len(slug_list),len(unique_slug))


