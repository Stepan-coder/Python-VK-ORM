import os
import urllib.request
from typing import Tuple


class PhotoMessage:
    def __init__(self, photo: dict):
        self.__photo = photo
        self.__width, self.__height, self.__url = self.__get_image()

    @property
    def id(self) -> int:
        return self.__photo['id']

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def url(self) -> str:
        return self.__url

    @property
    def album_id(self) -> int:
        return self.__photo['album_id']

    @property
    def date(self) -> int:
        return self.__photo['date']

    @property
    def owner_id(self) -> int:
        return self.__photo['owner_id']

    @property
    def access_key(self) -> str:
        return self.__photo['access_key']

    @property
    def post_id(self) -> int:
        return self.__photo['post_id']

    def save(self, path_to_save: str):
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        urllib.request.urlretrieve(self.url, path_to_save)

    def __get_image(self) -> Tuple[int, int, str]:
        sorted_photos = sorted(self.__photo['sizes'], key=lambda x: (x['width'], x['height']), reverse=True)
        return sorted_photos[0]['width'], sorted_photos[0]['height'], sorted_photos[0]['url']
