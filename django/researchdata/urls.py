from django.urls import path
from . import views, apps

app_name = apps.app_name

urlpatterns = [
    path('sounds/exhibition/',
         views.SoundWelcomeTemplateView.as_view(),
         name='sound-welcome'),

    path('sounds/exhibition/sounds/',
         views.SoundListView.as_view(),
         name='sound-list'),

    path('sounds/exhibition/sounds/<pk>/',
         views.SoundDetailView.as_view(),
         name='sound-detail'),

    path('sounds/exhibition/comment/create/',
         views.SoundscapeExhibitionCommentCreateView.as_view(),
         name='sound-comment-create'),

    path('sounds/exhibition/comment/create/success/',
         views.SoundscapeExhibitionCommentCreateSuccessTemplateView.as_view(),
         name='sound-comment-create-success'),

    path('sounds/create/',
         views.SoundCreateView.as_view(),
         name='sound-create'),

    path('sounds/create/success/',
         views.SoundCreateSuccessTemplateView.as_view(),
         name='sound-create-success'),
]
