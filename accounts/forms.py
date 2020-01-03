from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    # PasswordInput이라는 input태그를 사용하려고 password는 클래스 변수로 선언
    password = forms.CharField(label='password',widget = forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget = forms.PasswordInput)

    #Meta 클래스를 이용하여 기존에 있는 모델의 입력 폼을 쉽게 작성 가능
    #model 을 설정, fields를 이용해서 입력받을 필드들을 지정하면 된다.
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    #clean_필드명 : 각 필드의 clean메서드가 호출된 후에 호출되는 메서드
    #특별한 유효성 검사나 조작을 하고 싶을 때 만들어서 사용
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
