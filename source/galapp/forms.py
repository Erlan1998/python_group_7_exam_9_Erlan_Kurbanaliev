from galapp.models import Photos, Albom
from django import forms

class PhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['foto', 'text', 'album', 'is_private', 'user']
        exclude = ['user']

class PhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['foto', 'text', 'album', 'is_private']