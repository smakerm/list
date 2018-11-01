from django import forms
from .models import *

TOPIC_CHOICE=(
    ('level1','好评'),
    ('level2','中评'),
    ('level3','差评'),
)

class RemarkFrom(forms.Form):
    subject = forms.CharField(label='标题',initial='初始值')
    mail = forms.EmailField(label='邮件')
    message = forms.CharField(label='内容',widget=forms.Textarea)
    topic = forms.ChoiceField(label='评价',choices=TOPIC_CHOICE)
    save = forms.BooleanField(label="是否保存")


class RegisterForm(forms.Form):
    uname = forms.CharField(label="用户名")
    upwd = forms.CharField(label="密码",widget=forms.PasswordInput)
    uage = forms.IntegerField(label='年龄')
    # uage = forms.CharField(label='年龄',widget=forms.NumberInput)
    uemail = forms.EmailField(label='邮箱')

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uname','uage']
        labels = {
            'uname': '用户名称',
            'uage' : '用户年龄',
        }