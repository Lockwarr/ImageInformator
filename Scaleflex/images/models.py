"""
Database models
"""
import uuid
from django.db import models

class ImageInformation(models.Model):
    """
    Defines the model of a ImageInformation in the database"""

    blur_hash = models.TextField()
    sha1 = models.TextField()
    image_dimensions = models.TextField()
    image_type = models.TextField()