from rest_framework import serializers
from . import models

class ProjectSerializer(serializers.ModelSerializer):
    techused = serializers.StringRelatedField(many=True)
    class Meta:
        model= models.Project
        
        fields = ['project_name','screenshot','techused','project_link','project_type' ]

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Skills
        fields=['skill_name','logo','description']