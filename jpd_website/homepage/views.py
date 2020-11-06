from django.shortcuts import render
from homepage.models import About, Project

# Create your views here.

# About section
def about_me(request):
"""------------------------------------------------------------------------"""
# Project section
def all_projects(request):
    # query database to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                    {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html',
                    {'project': project})
"""------------------------------------------------------------------------"""
# Contact section
def contact_me(request):