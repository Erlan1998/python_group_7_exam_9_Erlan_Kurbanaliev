from django.db import models
from django.contrib.auth import get_user_model

class Photos(models.Model):
    foto = models.ImageField(null=False, blank=False, upload_to='user_pics', verbose_name='Аватар')
    text = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(),  null=False, blank=False, related_name='Photos', on_delete=models.CASCADE)
    album = models.ForeignKey('galapp.Albom', related_name='Photos', verbose_name='фото', null=True, blank=True, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False, verbose_name='приватный')


class Albom(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=250, null=True, blank=False)
    author = models.ForeignKey(get_user_model(), null=False, blank=False, related_name='Albom', verbose_name='автор', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

