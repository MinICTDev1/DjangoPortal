# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import submissionForm


# Create your views here.
def index(request):
    '''View defining the landing page of our application'''
    return render(request, 'Landing/index.html')

def base(request):
    ''' View defining the base template of our application'''
    return render(request, 'Landing/base.html')

def about(request):
    '''View defining the about page of our application.'''
    return render(request, 'Landing/about.html')

def submission(request):
    ''' View defining the submission page of the application'''
    return render(request, 'Landing/submission.html')

def submit(request):
    ''' View defining the actual submit page of the application'''
    if request.method == "POST":
        form = submissionForm(request.POST)
        if form.is_valid():
            Submision = form.save(commit=False)
            Submision.save()
            return redirect('post_detail', pk=Submision.pk)
    else:
        form = submissionForm()
    return render(request, 'Landing/submit.html', {'form': form})