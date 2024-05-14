from django.db import models
import datetime
from django.db.models.signals import pre_save,post_save
from articles.utils import slugify_instance_title
from django.utils.text import slugify
from django.urls import reverse


class Article(models.Model):
    user = models.ForeignKey("auth.User",blank=True,null=True,on_delete=models.SET_NULL)
    title = models.TextField()
    content = models.TextField()
    objects = models.Manager()
    create = models.DateField(auto_now=True, null=False)
    slug = models.SlugField(unique=True, null=True,blank=True)

    def get_absolute_url(self):
        return f'/home/{self.slug}/'
        # return revers('article_detail', kwargs={"slug":self.slug})

    def save(self,*args,**kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args,**kwargs)

def articel_pre_save(sender,instance,*args,**kwargs):
    print('pre_save')
    if instance.slug is None:
        # instance.slug = slugify(instance.title)
        slugify_instance_title(instance,save=False)


pre_save.connect(articel_pre_save, sender=Article)


def article_post_save(sender,instance,created,*args,**kwargs):
    print('post_save')
    instance.slug = slugify(instance.title)
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save,sender=Article)

