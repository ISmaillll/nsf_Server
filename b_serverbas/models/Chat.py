from django.db import models

class Conversation (models.Model):

    User1 = models.ForeignKey("User",on_delete=models.SET_NULL,null=True,related_name='User1')
    User2 = models.ForeignKey("User",on_delete=models.SET_NULL,null=True,related_name='User2')

class Messages (models.Model):

    Content = models.CharField(max_length=200)
    Date = models.DateTimeField()
    By = models.ForeignKey("User",on_delete=models.SET_NULL,null=True)
    Conversation = models.ForeignKey("Conversation",on_delete=models.CASCADE)