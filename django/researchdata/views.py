from django.views.generic import (ListView, DetailView, CreateView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from . import forms, models


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


class SoundWelcomeTemplateView(TemplateView):
    """
    Class-based view to show the sound welcome template
    """
    template_name = 'researchdata/sound-welcome.html'


class SoundListView(LoginRequiredMixin, ListView):
    """
    Class-based view to show the Sound list template
    """
    template_name = 'researchdata/sound-list.html'

    def get_queryset(self):
        queryset = models.Sound.objects.filter(admin_approved=True)
        # Search results
        search = self.request.GET.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(sound__icontains=search) |
                Q(location__icontains=search) |
                Q(location_soundscape_exhibition__icontains=search) |
                Q(location_soundscape_exhibition_ukrainian__icontains=search) |
                Q(recording_date__icontains=search) |
                Q(recording_time__icontains=search) |
                Q(description__icontains=search) |
                Q(description_ukrainian__icontains=search) |
                Q(interviewee_reflection__icontains=search) |
                Q(interviewee_reflection_ukrainian__icontains=search) |
                Q(prompt_for_public_comments__icontains=search)
            )
        return queryset.order_by('order_in_soundscape_exhibition', '-id')


class SoundDetailView(LoginRequiredMixin, DetailView):
    """
    Class-based view to show the Sound detail template
    """
    template_name = 'researchdata/sound-detail.html'
    queryset = models.Sound.objects.filter(admin_approved=True)


class SoundscapeExhibitionCommentCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view to create a SoundscapeExhibitionComment
    """
    fields = ['sound', 'comment']
    model = models.SoundscapeExhibitionComment
    success_url = reverse_lazy('researchdata:sound-comment-create-success')


class SoundscapeExhibitionCommentCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the SoundscapeExhibitionComment create success template
    """
    template_name = 'researchdata/sound-comment-create-success.html'
