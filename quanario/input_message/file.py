import os
import urllib.request
from typing import Tuple

import quanario.upload


class FileMessage:
    def __init__(self, file: dict):
        self.__file = file

    @property
    def id(self) -> int:
        return self.__file['id']

    @property
    def type(self) -> int:
        return self.__file['type']

    @property
    def title(self) -> str:
        return self.__file['title']

    @property
    def extension(self) -> str:
        return self.__file['ext']

    @property
    def size(self) -> str:
        return self.__file['size']

    @property
    def url(self) -> str:
        return self.__file['url']

    @property
    def date(self) -> int:
        return self.__file['date']

    @property
    def owner_id(self) -> int:
        return self.__file['owner_id']

    @property
    def access_key(self) -> str:
        return self.__file['access_key']

    def get_attachment(self) -> str:
        return f"doc{self.owner_id}_{self.id}_{self.access_key}"

    def save(self, path_to_save: str) -> None:
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if not path_to_save.endswith(self.extension):
            raise Exception(f"Invalid extension to save the file, please save the file in '.{self.extension}' format")
        urllib.request.urlretrieve(self.url, path_to_save)