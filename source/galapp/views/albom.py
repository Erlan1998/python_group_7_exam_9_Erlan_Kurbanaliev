from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView,  UpdateView, DetailView, DeleteView, TemplateView
from galapp.forms import PhotosForm, PhotoUpdateForm, AlbomCreateForm, AlbomUpdateForm
from galapp.models import Photos, Albom, Chosen

class AlbomIndexView(ListView):
    template_name = 'albom/albomindex.html'
    model = Albom
    context_object_name = 'albom'

class AlbomDetail(DetailView):
    template_name = 'albom/view_albom.html'
    model = Albom
    context_object_name = 'albom'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Photos.objects.filter(album=self.get_object())
        context['photos'] = object_list
        return context

class AlbomCreate(CreateView):
    template_name = 'albom/create_albom.html'
    form_class = AlbomCreateForm
    model = Albom
    # permission_required = 'webapp.add_projects'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = request.user

            if not request.user.is_anonymous:
                form.instance.author = user

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('albom_detail', kwargs={'pk': self.object.pk})


class AlbomUpdateView(UpdateView):
    template_name = 'albom/update_albom.html'
    model = Albom
    form_class = AlbomUpdateForm
    context_object_name = 'albom'
    # permission_required = 'webapp.change_projects'

    def get_success_url(self):
        return reverse('albom_detail', kwargs={'pk': self.object.pk})

class AlbomDelete(DeleteView):
    template_name = 'albom/delete_albom.html'
    model = Albom
    context_object_name = 'albom'
    success_url = reverse_lazy('alboms_all')
    # permission_required = 'webapp.delete_projects'


