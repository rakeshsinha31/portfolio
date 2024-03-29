# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import *

# Create your views here.

def homePage(request):
	jobs = Job.objects
	return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
	job_detail = get_object_or_404(Job, pk=job_id)
	return render(request, 'jobs/home.html')
