from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    # django会默认的为我们准备好登录页面，但是我们也可以手动的加一些字段
    nickname = models.CharField(max_length=64)
    # 必须是一对一的关系，
    user = models.OneToOneField(User)