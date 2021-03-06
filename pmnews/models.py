from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False,)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    cover_img = models.ImageField("Foto Sampul", upload_to='cover/', null=True, blank=True)    
    created_on = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=1)
    tags = TaggableManager()
    vlink = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)