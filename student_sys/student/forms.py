from django import forms
from student.models import Student


# 定义form表单
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone',
        )

    # 自定义数据校验，方法名：clean_字段名
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            # 错误信息会保存到form对象上，最终渲染到页面上
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)