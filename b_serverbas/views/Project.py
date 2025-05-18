from rest_framework.permissions import IsAuthenticated
from ..permissions import *
from ..serializers import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from datetime import datetime

# Project
class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectManagerSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class ProjectCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class ProjectRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

# Skill
class SkillListCreateView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated,UserPermission]

class SkillRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

# Jobs
class JobsListCreateView(ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class JobsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

# JobRequired
class JobRequiredListCreateView(ListCreateAPIView):
    queryset = JobRequired.objects.all()
    serializer_class = JobRequiredSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

class JobRequiredRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = JobRequired.objects.all()
    serializer_class = JobRequiredSerializer
    permission_classes = [IsAuthenticated,WorkerManagerPermission]

@csrf_exempt
def InterestedJobsApi(request,idWorker=0,idJob=0):
    if request.method == 'GET':
        InterestedJobss = InterestedJobs.objects.filter(Worker=idWorker,Job=idJob)
        if len(InterestedJobss) == 0:
            serializer = InterestedJobsSerializer(data={"Worker":idWorker,"Job":idJob,"Time":datetime.now()})
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors,safe=False)
        else:
            updated_data = {
                'Worker': InterestedJobss[0].Worker.id,
                'Job': InterestedJobss[0].Job.id,
                'Viewcount': InterestedJobss[0].Viewcount+1,
                'Time': datetime.now(),
            }
            serializer = InterestedJobsSerializer(instance=InterestedJobss[0], data=updated_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)
            return JsonResponse(serializer.errors,safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        InterestedJobss = InterestedJobs.objects.get(id=data['id'])
        serializer = InterestedJobsSerializer(InterestedJobss, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)    
    
@csrf_exempt
def PreposeJobsApi(request,idWorker=0):
    if request.method == 'GET':
        InterestedJobss = InterestedJobs.objects.filter(Worker=idWorker).order_by("-Time")[0:200]
        if len(InterestedJobss)==0:
            InterestedJobss = InterestedJobs.objects.all().order_by("-Time")[0:200]
        Serializer=InterestedJobsSerializer(InterestedJobss,many=True)
        JobsIds  = [S['id'] for S in Serializer.data]
        InterestedJobss =InterestedJobs.objects.filter(id__in=JobsIds).order_by("-Viewcount")[0:10]  
        Serializer=InterestedJobsSerializer(InterestedJobss,many=True)
        JobsIds  = [S['Job'] for S in Serializer.data]
        jobs = Jobs.objects.filter(id__in=JobsIds)
        Serializer=JobsSerializer(jobs,many=True)
        return JsonResponse(Serializer.data,safe=False)
@csrf_exempt
def HistJobsApi(request,idWorker=0):
    if request.method == 'GET':
        InterestedJobss = InterestedJobs.objects.filter(Worker_id=idWorker,Is_saved=True).order_by("-Time")
        Serializer=InterestedJobsSerializer(InterestedJobss,many=True)
        JobsIds  = [S['Job'] for S in Serializer.data]
        jobs = Jobs.objects.filter(id__in=JobsIds)
        Serializer=JobsSerializer(jobs,many=True)
        return JsonResponse(Serializer.data,safe=False)
@csrf_exempt
def GETStatApi(request):
    if request.method == 'GET':
        Projects = Project.objects.all().count()
        Creators = Worker.objects.all().count()
        jobs = Jobs.objects.all().count()
        return JsonResponse({"Projects":Projects,"Creators":Creators,"jobs":jobs}, safe=False)
      
@csrf_exempt
def WorkerJobsApi(request, id=0):
    if request.method == 'GET':
        Apply_fors = Apply_For.objects.filter(Q(Worker=id) & Q(State=1))
        serializerApply = Apply_ForSerializer(Apply_fors, many=True)
        WorkJobs = [job['Job'] for job in serializerApply.data]
        jobs = Jobs.objects.filter(id__in=WorkJobs)
        serializerJobs = JobsSerializer(jobs, many=True)
        WorkProject = [job['Project'] for job in serializerJobs.data]
        project = Project.objects.filter(id__in=WorkProject)
        serializerProject = ProjectManagerSerializer(project, many=True)
        return JsonResponse(serializerProject.data, safe=False)
    
@csrf_exempt
def GETJobsApi(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        Jobss = Jobs.objects.filter(id__in=data)
        serializer = JobsSerializer(Jobss, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def GETProjefctJobsApi(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        Jobss = Jobs.objects.filter(Project__in=data)
        serializer = JobsSerializer(Jobss, many=True)
        return JsonResponse(serializer.data, safe=False)
