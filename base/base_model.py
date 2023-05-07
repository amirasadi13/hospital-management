import uuid

from django.db import models


"""

    Used Base Model For Add Extra Field On Project's Models
    See hospital app models.
    
"""


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
