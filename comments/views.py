from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm
# Create your views here.
def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk = post_pk)
    # 判断如果是post请求，提交请求到的，如果不是，刷新回到原页面
    if request.method == 'POST':
        # 构造实例，把请求到的加入到form表单
        form = CommentForm(request.POST)
        # 检测数据是否合法，如果合法，保存到数据库
        if form.is_valid():
            # 如果直接保存，post_id保存不进来，在这里保存，但是不提交
            comment = form.save(commit=False)
            # 将post请求到的加进来
            comment.post = post
            comment.save()
            # redirect函数可以接收URL作为参数，也接收一个模型的实例，会调用实例的get_absolute_url
            # 会根据get_absolute_url方法返回的url值进行重定向
            return redirect(post)
        else:
            # 如果不合法，把评论过的显示出来，包括把错误的信息渲染出来
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context)
    else:
        return redirect(post)