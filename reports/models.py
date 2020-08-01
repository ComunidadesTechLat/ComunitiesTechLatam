""" Reports Model """

import uuid
from django.db import models


class ReportModel(models.Model):
    """ Report Model """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    community_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    Description = models.TextField()