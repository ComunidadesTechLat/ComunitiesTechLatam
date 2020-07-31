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
    

class Category(models.Model):
    """ Lists the avaliable categories  """
    class Meta:
        # pylint: disable=C0115,R0903
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Country(models.Model):
    """ Lists the avaliable countries """
    class Meta:
        # pylint: disable=C0115,R0903
        verbose_name_plural = "Countries"

    LATAM_ISO_COUNTRIES = [
        ('BZ','Belice'),
        ('CR','Costa Rica'),
        ('SV','El Salvador'),
        ('GT','Guatemala'),
        ('HN','Honduras'),
        ('NI','Nicaragua'),
        ('PA','Panamá'),
        ('AR','Argentina'),
        ('BO','Bolivia'),
        ('BR','Brasil'),
        ('CL','Chile'),
        ('CO','Colombia'),
        ('EC','Ecuador'),
        ('GY','Guyana'),
        ('GF','Guyana Francesa'),
        ('PY','Paraguay'),
        ('PE','Perú'),
        ('SR','Suriname'),
        ('UY','Uruguay'),
        ('VE','Venezuela'),
        ('MX','México'),
    ]
    
    name = models.CharField(
        choices=LATAM_ISO_COUNTRIES,
        max_length=60,
        null=False,    
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    """ Saves the country and exact coordenates of a community """

    community = models.OneToOneField(to='community', on_delete=models.CASCADE)
    country = models.ForeignKey(
        to='Country',
        on_delete=models.SET_NULL,
        null=True
    )
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        if self.latitude and self.longitude:
            return "{0}'s location:\n Country:{1}\n coord:{2},{3}".format(
                self.community,
                self.country,
                self.latitude,
                self.longitude
            )

        return "{0}'s location:\n Country:{1}".format(
            self.community,
            self.country
        )


class Flag(models.Model):
    """ Lists the avaliable flags
        for example 'Women only'
    """

    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=3)

    def __str__(self):
        return self.name