from django.db import models

class Software (models.Model):

    Name = models.CharField(max_length=100)
    Logo = models.ImageField(upload_to='images/Software/',default="images/Software/default.jpg", blank=True,null=True)
    Description = models.TextField(default="",blank=True)
    class type_p(models.IntegerChoices):
        Paid = 1, 'Paid'
        Free = 2, 'Free'
    Type = models.SmallIntegerField(default=type_p.Free,choices=type_p)
    Categorie = models.TextField(default=" ",blank=True)
    Genres = models.TextField(default=" ",blank=True)
    Supported_Languages = models.CharField(max_length=200,default=" ",blank=True)
    class systems(models.IntegerChoices): # add choises
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
    
    class types(models.IntegerChoices): # add choises
        Desktop = 1, 'Desktop'
        Mobile = 2, 'Mobile'
        Website = 3, 'Website'
    Platform_Type = models.CharField(max_length=20, blank=True, default="")
    def get_platform_type_display(self):
        type_ids = self.Platform_Type.split(",")
        type_names = [self.types(int(type_id)).label for type_id in type_ids if type_id.isdigit()]
        return type_names
    
    Special = models.CharField(max_length=200,default=" ",blank=True)
    Developer = models.CharField(max_length=100,default='',blank=True)

    Nbr_Rating = models.IntegerField()
    Number_Users = models.IntegerField()
    Rating = models.FloatField()
    Price = models.CharField(max_length=50,blank=True,null=True)
    Version = models.CharField(max_length=20,blank=True,default="1")
    Recommanded_age = models.CharField(max_length=30,default='+3',blank=True)

    Date = models.DateTimeField(null=True,blank=True)
    DateRelease = models.DateField(null=True,blank=True)
    DateUpdate = models.DateField(null=True,blank=True)

    Finiched = models.BooleanField(default=True)
    Forseal = models.BooleanField(default=False)
    signed = models.BooleanField(default=False)
    Published = models.BooleanField(default=False)

    By = models.ForeignKey("Worker",on_delete=models.CASCADE)

class LinksSoftware (models.Model):

    To = models.CharField(max_length=50)
    URL = models.CharField(max_length=150)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE)

class Image (models.Model):

    URL = models.ImageField(upload_to='images/Software/',default="images/Software/default.jpg", blank=True,null=True)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE)

class App_Tags(models.Model):

    Tag = models.CharField(max_length=50)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE)

# User interaction 
class HistorySoftware (models.Model):

    Rating = models.FloatField(default=0)
    Save = models.BooleanField(default=0)
    Content = models.CharField(max_length=500,blank=True,default="")
    date = models.DateTimeField(null=True)
    User = models.ForeignKey("User",on_delete=models.CASCADE)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE)

class Tags (models.Model):

    User = models.ForeignKey("User",on_delete=models.CASCADE)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE)

# Offer
class Software_offer (models.Model):

    content = models.CharField(max_length=500)
    PlusCnt = models.CharField(max_length=100,blank=True)
    Email = models.CharField(max_length=200,blank=True)
    Contact = models.CharField(max_length=200,blank=True)
    Price = models.CharField(max_length=100,blank=True)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE)

class User_Offer (models.Model):

    Message = models.CharField(max_length=500,blank=True)
    Num_Tel = models.CharField(max_length=20,blank=True)
    class state(models.IntegerChoices):
        Init = 1, 'Init'
        In_progress = 2, 'In progress'
        Finished = 3, 'Finished'
    State = models.SmallIntegerField(choices=state.choices, default=state.Init)
    Date = models.DateTimeField()
    Software_offer = models.ForeignKey("Software_offer",on_delete=models.CASCADE)
    User = models.ForeignKey("User",on_delete=models.CASCADE)

# Graphe Relations

class relationships(models.Model):

    Software1 = models.ForeignKey("Software",on_delete=models.CASCADE,related_name='Software1')
    Software2 = models.ForeignKey("Software",on_delete=models.CASCADE,related_name='Software2')
    Score = models.FloatField(default=0.0)
    Type = models.CharField(max_length=50,default="")
    Date = models.DateTimeField(null=True,blank=True)

class Externt_User_Download(models.Model):

    User = models.CharField(max_length=50)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE,null=True,related_name='SoftwareED')

class Externt_User_rating(models.Model):

    User = models.CharField(max_length=50)
    Software = models.ForeignKey("Software",on_delete=models.CASCADE,null=True,related_name='SoftwareER')