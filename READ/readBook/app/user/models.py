from django.contrib.auth.hashers import make_password
from django.db import models

class UserRead(models.Model):
    username = models.CharField(max_length=50, verbose_name='账号')
    password = models.CharField(max_length=255, verbose_name='密码')
    nickName = models.CharField(max_length=50, verbose_name='用户名')
    icon = models.ImageField(upload_to='icon', verbose_name='用户头像', default='')
    phone = models.CharField(max_length=11, verbose_name='手机号码', default='')
    email = models.CharField(max_length=16, verbose_name='邮箱', default='')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    source = models.CharField(max_length=50, verbose_name='来源', default='')

    def __str__(self):
        return self.nickName

    def __repr__(self):
        return '<UserRead:%d>%self.id'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.password) <= 20:
            self.password = make_password(self.password, hasher='default')

        super().save()

    class Meta:
        db_table = "t_user"
        verbose_name = '用户'
        verbose_name_plural = verbose_name



