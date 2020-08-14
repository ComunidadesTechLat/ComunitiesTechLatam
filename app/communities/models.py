""" Community Model """

import uuid
from django.db import models

class Community(models.Model):
    """ Community Model """

    # uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    # Main Info
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    img = models.ImageField(upload_to='imgs/', blank=True, null=True)
    description = models.TextField()
    quantity_of_members = models.IntegerField(blank=True, null=True)


    #Contact
    web = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)


    #Location
    """ Lists the avaliable countries """
    LATAM_ISO_COUNTRIES = [
        ('blz', 'Belice'),
        ('cri', 'Costa Rica'),
        ('slv', 'El Salvador'),
        ('gtm', 'Guatemala'),
        ('hnd', 'Honduras'),
        ('nic', 'Nicaragua'),
        ('pan', 'Panamá'),
        ('arg', 'Argentina'),
        ('bol', 'Bolivia'),
        ('bra', 'Brasil'),
        ('chl', 'Chile'),
        ('col', 'Colombia'),
        ('ecu', 'Ecuador'),
        ('guy', 'Guyana'),
        ('guf', 'Guyana Francesa'),
        ('pry', 'Paraguay'),
        ('per', 'Perú'),
        ('sur', 'Suriname'),
        ('ury', 'Uruguay'),
        ('ven', 'Venezuela'),
        ('mex', 'México'),
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

    created = models.DateTimeField(auto_now_add=True)
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
