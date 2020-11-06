from django.db import models

# Create your models here.

# About model is the "About Me" section of my website.
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=100)
    
    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.title
"""------------------------------------------------------------------------"""
# Project model is the "Projects" section of my website.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    
    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.title #or self.title for blog posts
"""------------------------------------------------------------------------"""
# Contact is the "Contact me" section of my website
class Contact(models.Model):
    name =
    subject = 
    email = 
    message = 