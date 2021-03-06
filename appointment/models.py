from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class State(models.Model):
    state_name = models.CharField(max_length=64)


class AppointmentInformation(models.Model):
    subject = models.CharField('约谈主题',max_length=64)
    description = models.TextField('简述约谈内容')
    email = models.EmailField('电子邮箱')  # uses EmailValidator
    name = models.CharField('姓名', max_length=64)
    mobile_number = models.CharField('手机号码', max_length=16)

'''
class User(User):  # 拓展用自带User类，并设定用户发起Appointment权限。
    email = models.EmailField('电子邮箱', max_length=64)
    username = models.CharField('用户名', max_length=64)
    password = models.CharField('密码', max_length=32)
    datetime = models.DateTimeField('注册时间', auto_now_add=True)  # 创建时自动设定，不可修改。auto_now为每次保存自动修改。

    def __str__(self):
        return '<User username:%s>' % self.username
'''


class Appointment(models.Model):
    STATE = (
        ('1', '未预约'),
        ('2', '待确认约定'),
        ('3', '已约定'),
        ('4', '已取消可重新约定'),
        ('5', '已完成'),
        ('6', '已禁止'),
    )
    appointment_time = models.DateTimeField('预约时间')
    state = models.CharField('状态', max_length=1, choices=STATE, default='1')  # get_state_display()
    appointment_information = models.ForeignKey(AppointmentInformation, on_delete=models.CASCADE, null=True)
    appointment_participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participant', null=True)
    appointment_maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='make', blank=True)  # 两个1对多设置related_name

    def __str__(self):
        return 'appointment_time:%s state:%s' % (self.appointment_time, self.get_state_display())
