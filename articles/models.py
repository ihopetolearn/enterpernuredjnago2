from django.db import models


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    objects = models.Manager()

    # def __str__(self):
    #     return self.content
