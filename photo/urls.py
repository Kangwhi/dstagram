# 2차 URL 파일
from django.urls import path
from .views import *

app_name = "photo"  # 네임스페이스 (앱이 여러개인 경우 html에 구분하기 위해 사용)
urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update')
]
