from django.db import models

class ChatSession(models.Model):

    User = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    Title = models.CharField(max_length=100, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Use = models.BooleanField(default=False)
    Creation = models.BooleanField(default=False)
    can_Generate = models.BooleanField(default=False)

class Message_Bot(models.Model):

    Session = models.ForeignKey("ChatSession", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(blank=True, default="")
    Time = models.DateTimeField(auto_now_add=True)
    is_user = models.BooleanField(default=False)
    App_Info_persentage = models.FloatField(default=0.0)
    Rec_semularity = models.FloatField(default=0.0)
    
class Software_recommandation(models.Model):

    Message_Bot = models.ForeignKey("Message_Bot", on_delete=models.CASCADE, null=True, blank=True)
    Software = models.ForeignKey("Software", on_delete=models.CASCADE, null=True, blank=True)

class User_Softwares(models.Model):

    Description = models.TextField(blank=True, default="")
    Specifications = models.FileField(upload_to='Documents/ChatBot/', null=True, blank=True)
    Categorie = models.CharField(max_length=200, blank=True, default="")
    Genres = models.CharField(max_length=200, blank=True, default="")
    class systems(models.IntegerChoices):
        Windows = 1, 'Windows'
        Mac = 2, 'Mac'
        Linux = 3, 'Linux'
        Android = 4, 'Android'
        IOS = 5, 'IOS'
    Platform_System = models.CharField(max_length=20, blank=True, default="")
    def get_platform_system_display(self):
        system_ids = self.Platform_System.split(",")
        system_names = [self.systems(int(system_id)).label for system_id in system_ids if system_id.isdigit()]
        return system_names
    
    class types(models.IntegerChoices):
        Desktop = 1, 'Desktop'
        Mobile = 2, 'Mobile'
        Website = 3, 'Website'
    Platform_Type = models.CharField(max_length=20, blank=True, default="")
    def get_platform_type_display(self):
        type_ids = self.Platform_Type.split(",")
        type_names = [self.types(int(type_id)).label for type_id in type_ids if type_id.isdigit()]
        return type_names
    
    Offer = models.BooleanField(default=False)
    Date = models.DateTimeField(auto_now_add=True)
    Session = models.ForeignKey("ChatSession", on_delete=models.SET_NULL, null=True, blank=True)
    User = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)

class Dev_Offer(models.Model): # add offer management (wich Manger take the project)

    Published = models.DateTimeField(auto_now_add=True)
    Accepted = models.DateTimeField(null=True, blank=True)
    Refused = models.DateTimeField(null=True, blank=True)
    class state(models.IntegerChoices):
        Init = 1, 'Init'
        Accepted = 2, 'Accepted'
        Refused = 3, 'Refused'
        In_progress = 4, 'In progress'
        Finished = 5, 'Finished'
    State = models.SmallIntegerField(choices=state.choices, default=state.Init)
    Comment = models.CharField(max_length=500, blank=True, default="")
    Contact = models.CharField(max_length=100, blank=True, default="")
    Email = models.CharField(max_length=100, blank=True, default="")
    Phone_Number = models.CharField(max_length=20, blank=True, default="")
    User_Softwares = models.ForeignKey("User_Softwares", on_delete=models.CASCADE, null=True, blank=True)
    Manager = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True)
    Project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, blank=True)