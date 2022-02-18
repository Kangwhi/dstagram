from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.


def register(request):
    # 회원 가입 데이터 입력 완료
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # 인스턴스 생성
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(
                request,
                template_name="registration/register_done.html",
                context={"new_user": new_user},
            )
    # 회원 가입 내용을 입력하는 상황
    else:
        user_form = RegisterForm()
    return render(
        request, template_name="registration/register.html", context={"form": user_form}
    )
