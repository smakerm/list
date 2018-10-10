from django import forms
from .models import *

# 作为下拉列表选项的元组
TOPIC_CHOICE = (
    #<option value='level1'>好评</option>
    ('level1', '好评'),
    ('level2', '中评'),
    ('level3', '差评'),
)


class RemarkForm(forms.Form):
    # 1.创建subject属性,对应生成一个文本框
    # 1.1 label:控件前提示的文本
    # 1.2 initial : 控件的初始值
    subject = forms.CharField(label='标题', initial='初始数据')
    # 2.创建email属性,对应生成一个邮件框
    # 2.1 label:控件前提示的文本
    mail = forms.EmailField(label='邮件')
    # 3. 创建多行文本域 - <textarea></textarea>
    # 3.1 widget:取值为forms.Textarea则变为多行文本域
    message = forms.CharField(label='内容', widget=forms.Textarea)
    # 4.下拉列表
    # 4.1 choices:指定下拉列表中的选项们,取值为一个元组
    topic = forms.ChoiceField(label='评价', choices=TOPIC_CHOICE)
    # 5.创建复选框
    save = forms.BooleanField(label='是否保存')


class RegisterForm(forms.Form):
    uname = forms.CharField(label='用户名称')
    upwd = forms.CharField(label='用户密码', widget=forms.PasswordInput)
    uage = forms.CharField(label='用户年龄', widget=forms.NumberInput)
    uemail = forms.EmailField(label='电子邮件')


# 声明一个ModelForm类,与Users实体相关联
class UsersForm(forms.ModelForm):
    class Meta:
        # 1.定义关联的Models
        model = Users
        # 2.定义要生成控件的字段
        fields = '__all__'  # ['uname','upwd']
        # 3.为生成控件的字段指定标签
        labels = {
            'uname': '用户名称',
            'upwd': '用户密码',
            'uage': '用户年龄',
            'uemail': '电子邮箱'
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uname', 'upwd']
        labels = {
            'uname': '登录名称',
            'upwd': '登录密码'
        }
        widgets = {
            'upwd': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入密码',
                'id': 'upwd'
            })
        }


class WidgetForm(forms.Form):
    uname = forms.CharField(
        label='用户名称',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入用户名'
            }
        )
    )
    upwd = forms.CharField(
        label='用户密码',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入密码'
            }
        )
    )
