from django.http.response import JsonResponse 
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from dateutil.relativedelta import relativedelta
from datetime import date
from scipy.stats import chi2
from rest_framework import status
from django.utils.dateparse import parse_date
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..permissions import *
from ..serializers import *
import os

# User 
# -- Public --
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer

# -- Private --
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated, UserPermission]

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(User, id=user_id)

        if 'ProfilePhoto' in request.FILES:
            if user.ProfilePhoto and os.path.isfile(user.ProfilePhoto.path):
                os.remove(user.ProfilePhoto.path)
            user.ProfilePhoto = request.FILES['ProfilePhoto']

        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.ProfilePhoto and os.path.isfile(instance.ProfilePhoto.path):
            os.remove(instance.ProfilePhoto.path)
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CheckEmail(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        
        if not email:
            return Response(
                {"error": "Email parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        email_exists = User.objects.filter(email=email).exists()
        
        return Response(
            {
                "exists": email_exists,
                "email": email
            },
            status=status.HTTP_200_OK
        )
    
class CheckUsername(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        
        if not username:
            return Response(
                {"error": "username parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        username_exists = User.objects.filter(username=username).exists()
        
        return Response(
            {
                "exists": username_exists,
                "username": username
            },
            status=status.HTTP_200_OK
        )
# worker
# -- Public --
class WorkerListView(ListAPIView):
    queryset = User.objects.filter(
            Role=User.role.Worker,
            worker__isnull=False
        ).select_related('worker').prefetch_related(
            'linksprofile_set',
            'workermaitrise_set'
        )
    serializer_class = WorkerPublicSerializer

@csrf_exempt
def GettheseWorkersApi(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        user = Worker.objects.filter(id__in=data).order_by('-Rating')
        Serializer=WorkerPublicSerializer(user,many=True)
        return JsonResponse(Serializer.data,safe=False)
# -- Private --
class WorkerCreateView(CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerInfoSerializer
    permission_classes = [IsAuthenticated, UserPermission]

class WorkerdetailView(RetrieveAPIView):
    serializer_class = WorkerSerializer
    permission_classes = [IsAuthenticated, WorkerPermission]

    def get_object(self):
        user = self.request.user
        return User.objects.select_related('worker').prefetch_related(
            'linksprofile_set',
            'workermaitrise_set'
        ).get(pk=user.pk)
    
class WorkerUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerInfoSerializer
    permission_classes = [IsAuthenticated, WorkerPermission]

# company
# -- Public --
class CompanyListView(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerPublicSerializer

# -- Private --
class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [IsAuthenticated, UserPermission]

class CompanydetailView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, CompanyPermission]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        serializer = CompanySerializer(user)
        return Response(serializer.data)

class CompanyUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [IsAuthenticated, CompanyPermission]

# LinksProfile
class LinksProfileListCreateView(ListCreateAPIView):
    queryset = LinksProfile.objects.all()
    serializer_class = LinksProfileSerializer
    permission_classes = [IsAuthenticated,WorkerCompanyManagerPermission]

class LinksProfileRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = LinksProfile.objects.all()
    serializer_class = LinksProfileSerializer
    permission_classes = [IsAuthenticated,WorkerCompanyManagerPermission]

# workerMaitrise
class workerMaitriseListCreateView(ListCreateAPIView):
    queryset = workerMaitrise.objects.all()
    serializer_class = workerMaitriseSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class workerMaitriseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = workerMaitrise.objects.all()
    serializer_class = workerMaitriseSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

# Domaine
class DomaineListCreateView(ListCreateAPIView):
    queryset = Domaine.objects.all()
    serializer_class = DomaineSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class DomaineRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Domaine.objects.all()
    serializer_class = DomaineSerializer
    permission_classes = [IsAuthenticated,UserPermission]

# SubDomain
class SubDomainListCreateView(ListCreateAPIView):
    queryset = SubDomain.objects.all()
    serializer_class = SubDomainSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class SubDomainRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SubDomain.objects.all()
    serializer_class = SubDomainSerializer
    permission_classes = [IsAuthenticated,UserPermission]

# DomainUser
class DomainUserListCreateView(ListCreateAPIView):
    queryset = DomainUser.objects.all()
    serializer_class = DomainUserSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class DomainUserRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = DomainUser.objects.all()
    serializer_class = DomainUserSerializer
    permission_classes = [IsAuthenticated,UserPermission]

# Rating 
@csrf_exempt
def RateWorkerApi(request, rater=0, worker=0, NewRate=0): # profilePro
    if request.method == 'GET':
        RateWorkers = RateWorker.objects.filter(Q(Rater=rater) & Q(Worker=worker))
        serializer = RateWorkerSerializer(RateWorkers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        rater_user = User.objects.get(id=rater)
        worker_user = Worker.objects.get(id=worker)
        RateWorkers, created = RateWorker.objects.get_or_create(Rater=rater_user, Worker=worker_user)
        workerrated = Worker.objects.get(id=worker)
        if created:
            workerrated.Rating = ((workerrated.Rating * workerrated.Nbr_Rating) + NewRate) / (workerrated.Nbr_Rating + 1)
            workerrated.Nbr_Rating += 1
            RateWorkers.Rating = NewRate
            RateWorkers.save()
        else:
            workerrated.Rating = ((workerrated.Rating*workerrated.Nbr_Rating)+NewRate-RateWorkers.Rating)/(workerrated.Nbr_Rating)
            RateWorkers.Rating = NewRate
            RateWorkers.save()
        workerrated.Rating = round(workerrated.Rating, 1)
        workerrated.save()

        new_Rate_serializer = RateWorkerSerializer(RateWorkers)

        return JsonResponse({"new_Rate": new_Rate_serializer.data,"UserRate":workerrated.Rating})