# https://docs.djangoproject.com/en/4.0/ref/signals/#pre-save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from drfbackend.models import Post, Article


@receiver(pre_save, sender=Post)
def add_slug(sender,instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)      # converts spaces to hyphens
        instance.slug = slug

@receiver(pre_save, sender=Article)
def add_slug2(sender,instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.subtitle)      # converts spaces to hyphens
        instance.slug = slug
