from rest_framework import serializers
from ..models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class Notification_toSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification_to
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'

class InterestedJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedJobs
        fields = '__all__'

class RateWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateWorker
        fields = '__all__'

class Apply_ForSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply_For
        fields = '__all__'
