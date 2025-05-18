from rest_framework import serializers
from ..models import *



class LinksProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksProfile
        fields = '__all__'

class workerMaitriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = workerMaitrise
        fields = '__all__'

# User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 
                  'first_name', 'last_name', 'ProfilePhoto', 'Role', 'Developer')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'email': {'required': False},
            'username': {'required': False}
            }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            **{field: validated_data.get(field) for field in self.Meta.fields if field not in ['id', 'email', 'username', 'password']}
        )
        return user

    def validate_email(self, value):
        user = self.instance
        if user and user.email == value:
            return value
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        user = self.instance
        if user and user.username == value:
            return value
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        if password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class UserPublicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username','first_name', 'last_name', 'ProfilePhoto')

# worker / manager

class WorkerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):

    worker_info = WorkerInfoSerializer(source='worker', read_only=True)
    links = LinksProfileSerializer(many=True, source='linksprofile_set', read_only=True)
    skills = workerMaitriseSerializer(many=True, source='workermaitrise_set', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 
                'first_name', 'last_name', 'ProfilePhoto', 'Role', 'Developer',
                'worker_info', 'links', 'skills')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'email': {'required': False},
            'username': {'required': False}
        }

class WorkerPublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['Profession', 'Education_Level', 'Bio', 'Nbr_Rating', 'Rating', 'Nbr_Post']
        
class WorkerPublicSerializer(serializers.ModelSerializer):
    
    worker_info = WorkerPublicInfoSerializer(source='worker', read_only=True)
    links = LinksProfileSerializer(many=True, read_only=True, source='linksprofile_set')
    skills = workerMaitriseSerializer(many=True, read_only=True, source='workermaitrise_set')
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 
                'ProfilePhoto', 'Role', 'Developer', 'worker_info', 'links', 'skills')

class WorkerRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('id','Profession','Rating','Nbr_Rating')
# company

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    company_info = CompanyInfoSerializer(source='Company', read_only=True)
    links = LinksProfileSerializer(many=True, read_only=True, source='linksprofile_set')
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 
                  'first_name', 'last_name', 'ProfilePhoto', 'Role', 'Developer'
                  ,'company_info','links')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'email': {'required': False},
            'username': {'required': False}
            }

class CompanyPublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['Location','Bio', 'Nbr_Rating', 'Rating', 'Nbr_Post']

class CompanyPublicSerializer(serializers.ModelSerializer):
    
    company_info = CompanyPublicInfoSerializer(source='Company',read_only=True)
    links =LinksProfileSerializer(many=True, read_only=True, source='linksprofile_set')
    class Meta:
        model = User
        fields = ('id', 'email', 'username','first_name', 'last_name', 'ProfilePhoto','company_info','links')

# Domaines and SubDomaines
class DomaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domaine
        fields = '__all__'

class SubDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDomain
        fields = '__all__'

class DomainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainUser
        fields = '__all__'