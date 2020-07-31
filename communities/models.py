""" Community Model """

from django.db import models
import uuid

class Community (models.Model):
    """ Community Model """
    
    #Display
    display = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    
    # Main Info
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='communities/logos', blank = True, null=True)
    img = models.ImageField(upload_to='communities/imgs', null=True, blank=True)
    description = models.TextField()
    quantity_of_members = models.IntegerField(blank = True, null=True)
    
    
    #Contact
    web = models.CharField(max_length=255, blank = True, null=True)
    email = models.EmailField(max_length=255, blank = True, null=True)
    fb_page = models.URLField(blank = True, null=True)
    twitter = models.URLField(blank = True, null=True)
    instagram = models.URLField(blank = True, null=True)
    github = models.URLField(blank = True, null=True)
    
    
    #Location
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank = True, null=True)
    
    
    # Category
    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        null=True
    )


    #Flags
    
    flags = models.ManyToManyField(
        to='Flag'
    )


    #Status
    
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Revision', 'In revision')
    ]
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=15,
        null=False,
        default='In revision'
    )
    
    
    # DC Counters
    
    interactions = models.IntegerField(default=0)
    reads = models.IntegerField(default=0)
    
    
    # DB info
    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name