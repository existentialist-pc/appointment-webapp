from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):  # 为什么没id?
    question_text = models.CharField('问题内容',max_length=200)  # 类属性名或Field实例名也是数据库列名
    pub_date = models.DateTimeField('发布时间')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)  # 后者通过减1天的时间戳，获得昨天此刻的时间

    was_published_recently.admin_order_field = 'pub_date'  # 排序功能按pub_date项
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布?'

    def __str__(self):
        return self.question_text

    __repr__ = __str__


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项', max_length=200)
    votes = models.IntegerField('投票', default=0)

    def __str__(self):
        return self.choice_text

    __repr__ = __str__



