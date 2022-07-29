import os
import urllib.request
from typing import Tuple


class DocumentMessage:
    def __init__(self, document: dict):
        self.__document = document

    @property
    def id(self) -> int:
        return self.__document['id']

    @property
    def type(self) -> int:
        return self.__document['type']

    @property
    def title(self) -> str:
        return self.__document['title']

    @property
    def extension(self) -> str:
        return self.__document['ext']

    @property
    def size(self) -> str:
        return self.__document['size']

    @property
    def url(self) -> str:
        return self.__document['url']

    @property
    def date(self) -> int:
        return self.__document['date']

    @property
    def owner_id(self) -> int:
        return self.__document['owner_id']

    @property
    def access_key(self) -> str:
        return self.__document['access_key']

    def save(self, path_to_save: str) -> None:
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if not path_to_save.endswith(self.extension):
            raise Exception(f"Invalid extension to save the file, please save the file in '.{self.extension}' format")
        urllib.request.urlretrieve(self.url, path_to_save)