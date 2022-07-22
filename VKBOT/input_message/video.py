import urllib.request
from typing import Tuple


class VideoMessage:
    def __init__(self, video: dict):
        self.__video = video
        self.__url = None
        # self.__url = self.__get_image()

    @property
    def id(self) -> int:
        return self.__video['id']

    @property
    def width(self) -> int:
        return self.__video['width']

    @property
    def height(self) -> int:
        return self.__video['height']

    @property
    def title(self) -> str:
        return self.__video['title']

    @property
    def url(self) -> str:
        return self.__url

    @property
    def owner_id(self) -> int:
        return self.__video['owner_id']

    @property
    def access_key(self) -> str:
        return self.__video['access_key']

    @property
    def date(self) -> int:
        return self.__video['date']

    @property
    def description(self) -> str:
        return self.__video['description']

    @property
    def duration(self) -> str:
        return self.__video['duration']

    @property
    def views(self) -> int:
        return self.__video['views']

    @property
    def can_edit(self) -> int:
        return self.__video['can_edit']

    @property
    def can_add(self) -> int:
        return self.__video['can_add']

    @property
    def can_attach_link(self) -> int:
        return self.__video['can_attach_link']

    @property
    def comments(self) -> int:
        return self.__video['comments']

    @property
    def is_favorite(self) -> bool:
        return self.__video['is_favorite']

