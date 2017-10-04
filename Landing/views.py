# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import submissionForm


# Create your views here.
def index(request):
    return render(request, 'Landing/index.html')

def base(request):
    return render(request, 'Landing/base.html')

def about(request):
    return render(request, 'Landing/about.html')

def submission(request):
    return render(request, 'Landing/submission.html')

def submit(request):
    if request.method == "POST":
        form = submissionForm(request.POST)
        if form.is_valid():
            Submision = form.save(commit=False)
            Submision.save()
            return redirect('post_detail', pk=Submision.pk)
    else:
        form = submissionForm()
    return render(request, 'Landing/submit.html', {'form': form})