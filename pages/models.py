from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.TextField()
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text

