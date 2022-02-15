# 2차 URL 파일
from django.urls import path
from .views import *

app_name = "photo"  # 네임스페이스
urlpatterns = [
    path("", photo_list, name="photo_list"),
    path("upload/", PhotoUploadView.as_view(), name="photo_upload"),
]
