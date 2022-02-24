from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=300)
	data = models.DateTimeField()
	text = models.TextField()
	image = models.ImageField(upload_to='event_images/')