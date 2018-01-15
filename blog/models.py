from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)
    # PositiveIntegerField类型只允许为正整数或0
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    # 继承，重定向后面的kwargs是给定向到detail传入的参数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    class Meta:
        ordering=['-created_time']
    # 阅读量加1
    def increase_views(self):
        self.views+=1
        #update_fields数据库只更新views字段的值，提高效率
        self.save(update_fields=['views'])