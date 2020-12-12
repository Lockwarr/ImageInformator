import blurhash
import requests
import json
from io import BytesIO
from urllib.request import urlopen
from images.models import ImageInformation
from images.serializers import ImagesSerializer
from images.helpers import is_url_image
from rest_framework import status, generics
from rest_framework.response import Response
from PIL import Image
from io import BytesIO
from hashlib import sha1

class Images(generics.ListCreateAPIView):
    """Generic view for Create/List image information
        
        Attributes:
            generics.ListCreateAPIView : generic view
        """
    queryset = ImageInformation.objects.all()
    serializer_class = ImagesSerializer

    @staticmethod
    def post(request):
        """
        Validates and inserts new image information into the database.
        """
        if "url" in json.loads(request.body):
            validated_url = is_url_image(json.loads(request.body)["url"])
        else:
            return Response("Url should be specified in the body", status=status.HTTP_400_BAD_REQUEST)

        if validated_url:
            response = requests.get(validated_url, stream=True)
            image = Image.open(BytesIO(response.content))

            #get blurHash of the image
            image_response = requests.get(validated_url, stream=True)
            image_blur_hash = blurhash.encode(image_response.raw, x_components=4, y_components=3)

            #get sha1 of the image
            contents = urlopen(validated_url).read()
            image_sha1 = sha1(contents).hexdigest()

            #check if the same image already exists in the DB
            #we don't check for blur_hash because it's x-y dimensions can vary in the future
            if ImageInformation.objects.filter(sha1=image_sha1, image_dimensions=image.size, image_type = image.format).exists():
                return Response("This image already exists in the DB with the same dimensions and type", status=status.HTTP_304_NOT_MODIFIED)

            #add information about this image to the DB
            ImageInformation.objects.create(blur_hash = image_blur_hash, sha1 = image_sha1, image_dimensions = image.size, image_type = image.format)
            
            return Response("Successfully collected image information", status=status.HTTP_200_OK)
        else:
            return Response("No image found at this url", status=status.HTTP_404_NOT_FOUND)