from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView,  UpdateView, DetailView, DeleteView, TemplateView
from galapp.forms import PhotosForm, PhotoUpdateForm
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

class PhotosCreate(CreateView):
    template_name = 'photo/create.html'
    form_class = PhotosForm
    model = Photos
    # permission_required = 'webapp.add_projects'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = request.user

            if not request.user.is_anonymous:
                form.instance.user = user

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('photo', kwargs={'pk': self.object.pk})


class PhotosUpdateView(UpdateView):
    template_name = 'photo/update_photo.html'
    model = Photos
    form_class = PhotoUpdateForm
    context_object_name = 'photos'
    pk_url_kwarg = 'pk'
    # permission_required = 'webapp.change_projects'

    def get_success_url(self):
        return reverse('photo', kwargs={'pk': self.object.pk})

class PhotosDeleteView(DeleteView):
    template_name = 'photo/delete.html'
    model = Photos
    context_object_name = 'photos'
    success_url = reverse_lazy('index_photo')
    # permission_required = 'webapp.delete_projects'

