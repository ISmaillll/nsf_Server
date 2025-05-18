from django.db import models

class Project (models.Model): # change attribute more specific
    
    Name = models.CharField(max_length=50,default='')
    Type = models.CharField(max_length=50)
    State = models.CharField(max_length=50,default='_')
    Date = models.DateTimeField(null=True)
    Date_Start = models.DateTimeField(null=True)
    Duration = models.DateTimeField(null=True)
    Budget = models.CharField(max_length=150,default="0")
    LinkF = models.CharField(max_length=150,default='\\')
    LinkChat = models.CharField(max_length=150,default='\\')
    Description = models.CharField(max_length=500)
    Manager = models.ForeignKey("User",on_delete=models.SET_NULL,null=True)
    
class Skill (models.Model):

    skill = models.CharField(max_length=100)
    
class Jobs (models.Model):

    Job = models.CharField(max_length=50)
    State = models.CharField(max_length=50,default='_')
    Description = models.CharField(max_length=300,default='_')
    Date = models.DateTimeField(default='2000-01-01')
    Payment = models.CharField(max_length=50)
    Project = models.ForeignKey("Project",on_delete=models.CASCADE)

class JobRequired (models.Model):

    Skill_Rating = models.IntegerField()
    Skill = models.ForeignKey("Skill",on_delete=models.CASCADE)
    Job = models.ForeignKey("Jobs",on_delete=models.CASCADE)
