from django.contrib import admin
from student.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    # 列表页过滤器
    list_filter = ('sex', 'status')
    # 列表页查询字段
    search_fields = ('name', 'profession')
    # 编辑页字段，不与fields共存
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'sex', 'profession'),
        }),
        ('联系方式', {
            'fields': ('email', 'qq', 'phone')
        })
    )