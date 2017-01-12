from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):  # 作为Inline的form
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):  # model admin class
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('日期信息', {'fields':['pub_date'], 'classes':['collapse']}),  # 默认隐藏
    ]  # 设定fields内容显示位置顺序 intuitive order
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text', 'pub_date']  # 对哪些field内容进行搜索，使用LIKE语句所以不宜过多项

admin.site.register(Question, QuestionAdmin)  # 为admin注册Question表进行管理


