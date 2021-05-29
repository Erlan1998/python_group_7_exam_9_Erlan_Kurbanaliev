from django.urls import path
from galapp.views import IndexView, PhotoDetail, PhotosCreate, PhotosUpdateView, PhotosDeleteView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index_photo'),
    path('photo/<int:pk>/', PhotoDetail.as_view(), name='photo'),
    path('photo/create', PhotosCreate.as_view(), name='photo_create'),
    path('photo/<int:pk>/update', PhotosUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete', PhotosDeleteView.as_view(), name='photo_delete'),
]