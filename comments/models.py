from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    #作用是当评论保存到数据库的时候，自动把时间的值指定为当前时间
    credited_time = models.DateTimeField(auto_now_add=True)
    #这个评论是关联到某篇文章（Post）,关联另一个APP的表
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        # 返回20个字段
        return self.text[:20]
