from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    doc_id = models.IntegerField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(upload_to='blog_images/', blank=True, null=True)  
    date = models.DateTimeField(auto_now_add=True)  
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='General')
    summary = models.TextField()
    uploaded = models.BooleanField()  

    def __str__(self):
        return f"{self.author} ({self.title})"
