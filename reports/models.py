""" Reports Model """

import uuid
from django.db import models


class ReportModel(models.Model):
    """ Report Model """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    community_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField()

    STATUS_CHOICES = [
        ('Revision', 'In revision'),
        ('Done', 'Done'),
    ]

    report_status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=15,
        null=False,
        default='In revision'
    )

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.community_name)
