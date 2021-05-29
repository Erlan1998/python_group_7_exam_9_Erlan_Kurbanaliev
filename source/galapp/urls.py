from django.urls import path
from galapp.views import (
    IndexView,
    PhotoDetail,
    PhotosCreate,
    PhotosUpdateView,
    PhotosDeleteView,
    AlbomIndexView,
AlbomDetail,
AlbomCreate,
AlbomUpdateView,
AlbomDelete
)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index_photo'),
    path('photo/<int:pk>/', PhotoDetail.as_view(), name='photo'),
    path('photo/create', PhotosCreate.as_view(), name='photo_create'),
    path('photo/<int:pk>/update', PhotosUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete', PhotosDeleteView.as_view(), name='photo_delete'),
    path('alboms/', AlbomIndexView.as_view(), name='alboms_all'),
    path('albom/<int:pk>/', AlbomDetail.as_view(), name='albom_detail'),
    path('albom/create/', AlbomCreate.as_view(), name='albom_create'),
    path('albom/<int:pk>/update', AlbomUpdateView.as_view(), name='albom_update'),
    path('albom/<int:pk>/delete', AlbomDelete.as_view(), name='albom_delete'),

]