from django.urls import path
from galapp.views import IndexView, PhotoDetail

urlpatterns = [
    path('index/', IndexView.as_view(), name='index_tasks'),
    path('photo/<int:pk>/', PhotoDetail.as_view(), name='photo'),
]