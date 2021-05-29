from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from galapp.models import Photos, Albom, Chosen

class IndexView(ListView):
    template_name = 'photo/index.html'
    model = Photos
    context_object_name = 'photos'

class PhotoDetail(DetailView):
    template_name = 'photo/view_photo.html'
    model = Photos
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objject_photos = Photos.objects.get(id=self.kwargs.get('pk'))
        choosens_obj = objject_photos.Chosen.all()
        users = [choosen.user for choosen in choosens_obj]
        context['user_obj'] = users
        return context