# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import submissionForm
from django.template import Context
from django.template.loader import get_template
from .models import Submision
from django.utils import timezone


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
    return render(request, 'Landing/submission.html', {'form': submissionForm()})

def sidebase(request):
    return render(request, 'Landing/memberbase.html')

def submit(request):
    ''' View defining the actual submit page of the application'''

    form_test = submissionForm
    if request.method == "POST":
        form = submissionForm(data=request.POST)
        if form.is_valid():
            submision =  form.save(commit=False)
            submitter_name = request.POST.get('individual_name', '')
            submitter_gender = request.POST.get('gender', '')
            submitter_number = request.POST.get('phone_number', '')
            submitter_email = request.POST.get('email', '')
            innovation_title = request.POST.get('title', '')
            owned_by = request.POST.get('ownership', '')
            company_registration_date = request.POST.get('company_regDate', '')
            owner_nin = request.POST.get('individual_NIN', '')

            # Email the profile with the 
            # contact information

            template = get_template('Landing/contact_template.txt')
            context = {
                'Innovation_title': innovation_title,
                'Owned_by': owned_by,
                'Owner_NIN': owner_nin,
                'Company_registration_date': company_registration_date,
                'Submitter_name': submitter_name,
                'Submitter_gender': submitter_gender,
                'Submitter_number': submitter_number,
                'Submitter_email': submitter_email,
            }
            content = template.render(context)

            email = EmailMessage(
                "New Innovation submitted",
                content,
                "Innovation Hub Portal" +'',
                ['youremail@ict.go.ug'],
                # headers = {'Reply-To': contact_email }
            )
            email.send()
            submision.save()
            return redirect('submit')

    return render(request, 'Landing/submit.html', {'form': form_test})

def contact(request):
    ''' test for contact form'''
    form_class = ContactForm
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('Landing/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'Landing/contact.html', {'form': form_class})

def test(request):
    # form = PostForm()
    # return render(request, 'Landing/testing.html', {'form': form})

    # form = PostForm()
    # return render(request, 'blog/post_edit.html', {'form': form})

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('test')
    else:
        form = PostForm()
    return render(request, 'Landing/test.html', {'form': form})
