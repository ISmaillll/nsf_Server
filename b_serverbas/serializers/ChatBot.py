from rest_framework import serializers
from ..models import *
from ..serializers.Software import SoftwareSerializer

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = '__all__'

class Message_BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_Bot
        fields = '__all__'

class Software_recommandationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software_recommandation
        fields = '__all__'

class User_SoftwaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Softwares
        fields = '__all__'

class Dev_OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dev_Offer
        fields = '__all__'

####
class Software_recommandationSerializerPlus(serializers.ModelSerializer):
    Software = SoftwareSerializer()
    class Meta:
        model = Software_recommandation
        fields = '__all__'
class Message_BotSerializerPlus(serializers.ModelSerializer):

    Software_recommandation = Software_recommandationSerializerPlus(many=True, source='software_recommandation_set', read_only=True)
    class Meta:
        model = Message_Bot
        fields = '__all__'