from django import forms
from .models import Admin
from captcha.fields import CaptchaField

class admin_form(forms.ModelForm):
    Apass=forms.CharField(max_length=100,label='Password',widget=forms.
                          PasswordInput(attrs={'class':'form-control' 'col-2'}))
    captcha=CaptchaField()
    class Meta:
        model=Admin
        fields=('name','email','phone','Apass')
        labels={'name':'Admin name','email':'Email','phone':'Contact'}
        
