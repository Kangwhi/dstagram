from django.contrib.auth.models import User
from django import forms

# HTML의 Form Tag: frontend에서 사용자의 입력을 받는 인터페이스.
# Django의 Form: HTML의 폼 역할. DB에 저장할 내용을 형식, 제약조건을 결정.
# DJango의 Form을 만들어 보자!
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    # `clean_{필드}` 함수: 해당 필드에 대한 검증을 어떻게 할 것인지 결정
    def clean_password2(self):
        cd = self.cleaned_data  # clean된 data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords not matched!")
        return cd["password2"]  # 해당 필드의 데이터를 return하는 것이 관례
