from rest_framework import serializers
from ..models import *
from .User import WorkerPublicSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectManagerSerializer(serializers.ModelSerializer):
    Manager = WorkerPublicSerializer()
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class JobRequiredSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequired
        fields = '__all__'