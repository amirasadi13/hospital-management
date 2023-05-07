from django.db import models

from base.base_model import BaseModel


class Department(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

