from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):

    class relation(models.IntegerChoices):
        User = 1 , 'User'
        Project = 2, 'Project'
        User_Software = 3 , 'User_Software'
        Job = 4 , 'Job'
        Software = 5 , 'Software'
        User_Offer = 6 , 'User_Offer'
        ChatBot = 7 , 'ChatBot'
        Message = 8 , 'Message'
    Relation = models.IntegerField(choices=relation.choices, default=relation.Project)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    Message  = models.CharField(max_length=100, blank=True, default="")
    Date_Time = models.DateTimeField(null=True,blank=True)


class Notification_to(models.Model):

    Notification = models.ForeignKey("Notification", on_delete=models.CASCADE,default=1)
    To = models.ForeignKey("User", on_delete=models.CASCADE,default=1)
    Opened = models.BooleanField(default=False)

class Search(models.Model):

    content = models.CharField(max_length=250)
    Time = models.DateTimeField(null=True)
    user = models.ForeignKey("User",on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

class InterestedJobs(models.Model):

    Worker = models.ForeignKey("Worker",on_delete=models.CASCADE)
    Job = models.ForeignKey("Jobs",on_delete=models.CASCADE)
    Viewcount = models.IntegerField(default=1)
    Time = models.DateTimeField(null=True)
    Save = models.BooleanField(default=False)
    Is_saved = models.BooleanField(default=False)
    Apply = models.BooleanField(default=False)

class RateWorker (models.Model):

    Rater = models.ForeignKey("User",on_delete=models.CASCADE,related_name="Rater")
    Worker = models.ForeignKey("Worker",on_delete=models.CASCADE,related_name="Worker")
    Rating = models.IntegerField(default=0,null=True)

class Apply_For (models.Model):
    
    Worker = models.ForeignKey("Worker",on_delete=models.CASCADE,default=0)
    Job = models.ForeignKey("Jobs",on_delete=models.CASCADE,default=0)
    Date_Apply = models.DateTimeField()
    Date_Work = models.DateTimeField(null=True)
    State = models.BooleanField(default=False)