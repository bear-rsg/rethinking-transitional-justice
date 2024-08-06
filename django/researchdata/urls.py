from django.urls import path
from . import views, apps

app_name = apps.app_name

urlpatterns = [
    path('sounds/create/',
         views.SoundCreateView.as_view(),
         name='sound-create'),
    path('sounds/create/success/',
         views.SoundCreateSuccessTemplateView.as_view(),
         name='sound-create-success'),
]
