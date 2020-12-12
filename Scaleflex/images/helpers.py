"""Help for images"""
import http.client
import requests
from urllib.request import urlopen


def is_url_image(image_url):
    """
    Checks if the provided url contains image
    """
    #check if content-type headers contain 'image'
    try:
        response = requests.get(image_url, stream=True)
        with urlopen(image_url) as response:
            info = response.info()
            if "image" in info.get_content_type():
                return image_url
            else:
                return False
    except:
        return False