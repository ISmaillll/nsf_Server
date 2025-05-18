from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('Role', self.model.role.Admin)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    ####
    class role(models.IntegerChoices):
        User = 1, 'User'
        Worker = 2, 'Worker'
        Company = 3, 'Company'
        Manager = 4, 'Manager'
        Admin = 5, 'Admin'
    Role = models.SmallIntegerField(choices=role.choices , default=role.User)
    ProfilePhoto = models.ImageField(upload_to='images/User/',default="images/User/default.jpg", blank=True,null=True)
    Developer = models.BooleanField(default=False)
    ####
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class Worker (models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Profession = models.CharField(max_length=50)
    Education_Level = models.CharField(max_length=50)
    Bio = models.CharField(max_length=201,default='')
    Nbr_Rating = models.IntegerField()
    Rating = models.FloatField()
    Nbr_Post = models.IntegerField(default=0)
    Avalble = models.BooleanField(default=True)

class Company (models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Location = models.CharField(max_length=50,default='')
    Bio = models.CharField(max_length=201,default='')
    # add company info
    Nbr_Rating = models.IntegerField()
    Rating = models.FloatField()
    Nbr_Post = models.IntegerField(default=0)

class LinksProfile (models.Model):

    To = models.CharField(max_length=50)
    URL = models.CharField(max_length=150)
    User = models.ForeignKey("User",on_delete=models.CASCADE)

class workerMaitrise (models.Model):

    Skill_Rating = models.IntegerField()
    Skill = models.ForeignKey("Skill",on_delete=models.CASCADE)
    User = models.ForeignKey("User",on_delete=models.CASCADE)

class Domaine (models.Model):

    Content = models.CharField(max_length=50,default='')

class SubDomain (models.Model):

    Domain = models.ForeignKey("Domaine",on_delete=models.CASCADE,related_name='Domain')
    SubDomain = models.ForeignKey("Domaine",on_delete=models.CASCADE,related_name='SubDomain')

class DomainUser (models.Model):

    Domain = models.ForeignKey("Domaine",on_delete=models.CASCADE)
    User = models.ForeignKey("User",on_delete=models.CASCADE)