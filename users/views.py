from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegisterForm

def register(request):
    # 先判断是不是post请求
    if request.method == 'POST':
        # 如果是，接收数据
        form =RegisterForm(request.POST)
        # 判断字段是否合法
        if form.is_valid():
            form.save()
            # 返回首页
            return redirect('/')
    else:
        # 如果不是post请求，返回首页，携带的空信息
        form = RegisterForm()
    return render(request,'users/register.html',context={'form':form})