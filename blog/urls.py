from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

#相当于namespace，可以不用在根urls里设置
app_name = 'blog'

urlpatterns = [
    # as_view方法把一个类转成一个函数
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', login_required(views.PostDetailView.as_view()), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

]