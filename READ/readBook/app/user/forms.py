import re

from django import forms
from user.models import UserRead


class UserForm(forms.ModelForm):

    username = forms.CharField(min_length=6,
                               max_length=20,
                               error_messages={
                                   'required': '账号不能为空',
                                   'min_length': '账号不能小于6位',
                                   'max_length': '账号不能超过20位',
                                   'unique': '账号已存在'
                               })

    class Meta:
        model = UserRead
        fields = ('username', 'password', 'nickName', 'email')
        error_messages = {
            'password': {
                'required': '密码不能为空'
            },
            'nickName': {
                'required': '用户名不能为空'
            },
            'email': {
                'required': '邮箱不能为空'
        },
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is not None and not re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', email):
            raise ValueError('邮箱不合法')
        return email