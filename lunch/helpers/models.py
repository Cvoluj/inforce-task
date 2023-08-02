from django.db import models
from django.utils import timezone

class TrackingModel(models.Model):
    """
    Common abstract model tracking that include basic rows of model
    """
    created_at = models.DateField(default=timezone.now, blank=True)
    updated_at = models.DateField(auto_now=True) 

    class Meta:
        abstract=True
        ordering=('-created_at',)