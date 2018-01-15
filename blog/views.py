import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from comments.forms import CommentForm
# Create your views here.
from blog.models import Post, Category, Tag


# ----------------------------------------------------------------------------
# def index(request):
#     post_list = Post.objects.all()
#     context = {'post_list': post_list}
#     return render(request,'blog/index.html',context)


# 类视图
#对于这种获取某个表的列表数据的，就用ListView类视图
class IndexView(ListView):
    #model:找到需要从那个表里
    model = Post
    #要渲染的模板
    template_name = 'blog/index.html'
    #获取数据的变量名，这个变量会传递给模板，传入的数据
    context_object_name = 'post_list'
    #类视图帮我们分页逻辑，通过paginate_by指定每页的数量
    paginate_by = 5




# 详情页，传入参数，定义详情的那一页--------------------------------------------
'''
def detail(request,pk):
    # 如果能找到文章，返回它的详情，如果找不到，返回404
    post = get_object_or_404(Post,pk=pk)
    # 阅读量加1
    post.increase_views()

    # markdown插入输入格式，在什么地方插入，就在什么地方输入
    post.body = markdown.markdown(post.body,
      extensions=[
          'markdown.extensions.extra',
          'markdown.extensions.codehilite',
          'markdown.extensions.toc',
      ])
    # 获取评论
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form ,
        'comment_list':comment_list
    }

    return render(request,'blog/detail.html',context)
'''
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    #先调用父类的get方法，是因为只有当get方法被调用后，
    # 才有self.object属性，
    # 这个属性就是Post模型的实例
    # 阅读量加1
    def get(self, request, *args, **kwargs):

        response = super().get(request,*args,**kwargs)

        self.object.increase_views()

        return response
    # markdown
    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.body = markdown.markdown(post.body,
          extensions=[
              'markdown.extensions.extra',
              'markdown.extensions.codehilite',
              'markdown.extensions.toc',
          ])
        return post

    #覆写get_context_data是因为要添加出了post传递的值以外，
    #还需要把评论和表单的内容传递给模板，
    #往context里面添加内容
    # 获取评论
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({'form':form,
                        'comment_list':comment_list
                        })
        return context




# 归档,按照时间--------------------------------------------------------------------
# def archives(request,year,month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month)
#     return render(request,'blog/index.html',context={'post_list':post_list})
class ArchivesView(IndexView):
    def get_queryset(self):
        return super().get_queryset().filter(
            created_time__year = self.kwargs.get('year'),
            created_time__month = self.kwargs.get('month'),
        )

'''
listview总结：
1、listview主要用在获取某个model列表中
2、通过template_name属性来指定需要渲染的模板，通过
context_object_name属性来制定需要获取的model列表的名字
3、复写 get_queryset 方法以增加获取model列表的其他逻辑
4、复写get_context_data方法来为上下文对象添加额外的变量以便在模板中访问

'''





# 分类----------------------------------------------------------------------------
# def category(request,pk):
#     cate = get_object_or_404(Category,pk = pk)
#     post_list = Post.objects.filter(category=cate)
#     return render(request,'blog/index.html',context={'post_list':post_list})

class CategoryView(IndexView):
    # model = Post
    # template_name = 'blog/index.html'
    # context_object_name = 'post_list'
    def get_queryset(self):
        cate = get_object_or_404(Category,pk = self.kwargs.get('pk'))
        return super().get_queryset().filter(category = cate)



class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=tag)









