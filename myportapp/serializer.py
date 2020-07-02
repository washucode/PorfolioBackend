from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Project
        fields = ['project_name','screenshot','project_link']

