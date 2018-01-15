# 从后台导入admin
from django.contrib import admin

# Register your models here.
# 导入添加的字段
from .models import Post,Category,Tag
# 显示的列表内容
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
# 注册
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)