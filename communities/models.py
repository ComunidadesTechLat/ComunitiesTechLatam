""" Community Model """

import uuid
from django.db import models

class Community(models.Model):
    """ Community Model """
    #Display
    display = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    # Main Info
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='communities/logos', blank=True, null=True)
    img = models.ImageField(upload_to='communities/imgs', null=True, blank=True)
    description = models.TextField()
    quantity_of_members = models.IntegerField(blank=True, null=True)


    #Contact
    web = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    fb_page = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)


    #Location
    """ Lists the avaliable countries """
    LATAM_ISO_COUNTRIES = [
        ('BZ', 'Belice'),
        ('CR', 'Costa Rica'),
        ('SV', 'El Salvador'),
        ('GT', 'Guatemala'),
        ('HN', 'Honduras'),
        ('NI', 'Nicaragua'),
        ('PA', 'Panamá'),
        ('AR', 'Argentina'),
        ('BO', 'Bolivia'),
        ('BR', 'Brasil'),
        ('CL', 'Chile'),
        ('CO', 'Colombia'),
        ('EC', 'Ecuador'),
        ('GY', 'Guyana'),
        ('GF', 'Guyana Francesa'),
        ('PY', 'Paraguay'),
        ('PE', 'Perú'),
        ('SR', 'Suriname'),
        ('UY', 'Uruguay'),
        ('VE', 'Venezuela'),
        ('MX', 'México'),
    ]

    country = models.CharField(
        choices=LATAM_ISO_COUNTRIES,
        max_length=60,
        null=True,
    )

    city = models.CharField(max_length=50, blank=True, null=True)


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
        ('Revision', 'In revision'),
        ('Active', 'Active'),
    ]

    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=15,
        null=False,
        default='Revison'
    )


    # DC Counters

    interactions = models.IntegerField(default=0)
    reads = models.IntegerField(default=0)


    # DB info

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    #return the name of the community
    def __str__(self):
        return str(self.name)



class Category(models.Model):
    """ Lists the avaliable categories  """
    class Meta:
        # pylint: disable=C0115,R0903
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.name)


class Flag(models.Model):
    """ Lists the avaliable flags
        for example 'Women only'
    """

    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=3)

    def __str__(self):
        return str(self.name)
