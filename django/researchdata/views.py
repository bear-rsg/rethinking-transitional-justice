from django.views.generic import (CreateView, TemplateView)
from django.urls import reverse_lazy
from . import forms


class SoundCreateView(CreateView):
    """
    Class-based view to show the 'share your sound' template
    """
    template_name = 'researchdata/sound-create.html'
    form_class = forms.SoundCreateForm
    success_url = reverse_lazy('researchdata:sound-create-success')


class SoundCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the sound create success template
    """
    template_name = 'researchdata/sound-create-success.html'
