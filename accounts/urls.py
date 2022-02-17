from django.urls import path
from django.contrib.auth import views as auth_view

# profile 페이지가 없다... 해결방법은?
# 1. profile 만들기
# 2. profile 페이지가 아닌 페이지로 보내기
#   a. 장고 설정 변경
#   b. 웹 서버에서 설정(redirect, 다른 페이지로 보내줌)
urlpatterns = [
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]
