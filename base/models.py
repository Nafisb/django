from django.db import models
#from django.contrib.auth.models import User

#from django.contrib.auth.models import AbstractUser
#class appUser(AbstractUser):
#    customised fields here


class Network(models.Model):
    title = models.CharField(max_length=50, null=False, default= '', unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    #active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True) 
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

#class UserNetworkMembership(models.Model):
#    """handles n-to-n relationship between User and Network"""
#    userID = models.ForeignKey(User, on_delete=models.CASCADE)
#    networkID = models.ForeignKey(Network, on_delete=models.CASCADE)
#    createdAt = models.DateTimeField(auto_now_add=True) 
    #deletedAt = models.DateTimeField(null=True, blank=True)



