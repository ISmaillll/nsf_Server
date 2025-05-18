from rest_framework import serializers
from ..models import *
from ..serializers.User import WorkerPublicSerializer,UserPublicSerializer

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'

class SoftwareSerializerMoin(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = ('id','Name','Logo','Type','Categorie','Rating')

class SoftwareSerializerPlus(serializers.ModelSerializer):
    By = WorkerPublicSerializer()
    class Meta:
        model = Software
        fields = "__all__"

class LinksSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksSoftware
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class App_TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = App_Tags
        fields = '__all__'

class HistorySoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorySoftware
        fields = '__all__'

class HistorySoftwareSerializerPlus(serializers.ModelSerializer):
    User = UserPublicSerializer()
    class Meta:
        model = HistorySoftware
        fields = "__all__"

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class TagsSerializerPlus(serializers.ModelSerializer):
    User = UserPublicSerializer()
    class Meta:
        model = Tags
        fields = "__all__"

class Software_offerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software_offer
        fields = '__all__'

class User_OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Offer
        fields = '__all__'

class relationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = relationships
        fields = '__all__'

class Externt_User_DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Externt_User_Download
        fields = '__all__'
        
class Externt_User_ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Externt_User_rating
        fields = '__all__'