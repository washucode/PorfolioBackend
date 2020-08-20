from django.shortcuts import render
from django.http import HttpResponse
from . import models
from rest_framework import generics
from . import serializer


def HomePageView(request):
    return HttpResponse("Hello World")

class ProjectView(generics.ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializer.ProjectSerializer

class SkillsView(generics.ListAPIView):
    queryset = models.Skills.objects.all()
    serializer_class = serializer.SkillsSerializer



    