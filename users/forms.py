from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 继承的模板
        model = User
        # 注册要现实的字段
        fields=["username","email"]