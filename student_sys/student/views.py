from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from student.forms import StudentForm
from student.models import Student


# Create your views here.
class IndexView(View):
    template_name = 'index.html'

    # 获取学员信息
    def get_context(self):
        students = Student.get_all()    # 使用model中定义的类方法
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()    # 创建form对象
        context.update({
            'form': form,
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        # 接受form表单提交的数据
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # 重定向，使用reverse方法反向解析url地址，也可用redirect方法重定向
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        # 走到这则证明form表单数据异常，此时form中会带上错误信息，如qq号格式错误，邮箱格式错误等
        context.update({'form': form})
        return render(request, self.template_name, context=context)