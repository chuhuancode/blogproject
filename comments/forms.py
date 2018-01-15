
# 使用django的表单功能，一定要导入他的表单
from django import forms
from .models import Comment

#通过调用这个CommentForm类，django自动为我们创建表单的代码
# 必须要继承form的类
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','url','text']
