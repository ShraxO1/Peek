from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class People(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200,blank=True)
	url = models.URLField()
	image = models.ImageField(upload_to='people/%Y/%m/%d/')
	description = models.TextField(blank=True)
	created = models.DateField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)