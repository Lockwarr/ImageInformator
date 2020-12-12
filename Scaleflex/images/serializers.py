"""Contains serialization for Images model."""
from rest_framework import serializers
from images.models import ImageInformation


class ImagesSerializer(serializers.ModelSerializer):
    """ImagesSerializer class will convert ImageInformations model into other format"""

    class Meta:
        """This Meta class will define how ImagesSerializer class will behave"""
        model = ImageInformation
        fields = ["blur_hash", "sha1", "image_dimensions", "image_type"]