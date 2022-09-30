from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#
# class User(models.Model):
#     user = models.ForeignKey(User, on_delete= models.CASCADE)

#blog

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    date_created = models.DateField(auto_now_add=True,null=True, blank=True)
    last_modified = models.DateField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_created', ]



class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    title= models.ForeignKey(Post, on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        ordering = ['date_created', ]


from django.db import models


# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question