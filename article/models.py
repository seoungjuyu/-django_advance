from multiprocessing import AuthenticationError
from django.db import models

# Create your models here.

class Article(models.Model) :
    author = models.ForeignKey('user.User')
    titile = models.CharField(max_length=50)
    content = models.TextField()