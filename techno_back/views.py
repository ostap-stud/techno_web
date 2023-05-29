from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import FeedbackForm
from .models import Feedback


def about_and_feedback(request):
    # Retrieve post by id
    new_feedback = Feedback()

    if request.method == 'POST':
        # Form was submitted
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            new_feedback.user_email = form.cleaned_data['user_email']
            new_feedback.feedback = form.cleaned_data['feedback']
            new_feedback.save()
            return redirect('about')
    else:
        form = FeedbackForm()
    return render(request, 'about.html', {'form': form})


def index(request):
    """
    Домашня сторінка сайту.
    """
    return render(
        request,
        'index.html',
        context={},
    )


def history(request):
    """
    Історія.
    """
    return render(
        request,
        'history.html',
        context={},
    )


def artist1(request):
    """
    artist1.
    """
    return render(
        request,
        'artist1.html',
        context={},
    )


def artist2(request):
    """
    artist2.
    """
    return render(
        request,
        'artist2.html',
        context={},
    )


def artist3(request):
    """
    artist3.
    """
    return render(
        request,
        'artist3.html',
        context={},
    )


def about(request):
    """
    about.
    """
    return render(
        request,
        'about.html',
        context={},
    )