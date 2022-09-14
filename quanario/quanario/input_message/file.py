"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import os
import urllib.request
import quanario.upload
from typing import Tuple


class File:
    def __init__(self, file: dict):
        self.__file = file

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения уникального идентификатор файла.
        :en Property for getting a unique file identifier.
        """
        return self.__file['id']

    @property
    def type(self) -> int:
        """
        :ru Свойство для получения идентификатора типа файла.
        :en Property for getting a unique file ID.
        """
        return self.__file['type']

    @property
    def title(self) -> str:
        """
        :ru Свойство для получения полного названия файла.
        :en Property for getting the full name of the file.
        """
        return self.__file['title']

    @property
    def extension(self) -> str:
        """
        :ru Свойство для получения расширения файла, например: '.png' или '.pdf'.
        :en Property for getting the file extension, for example: '.png' or '.pdf'.
        """
        return self.__file['ext']

    @property
    def size(self) -> str:
        """
        :ru Свойство для получения размер файла в байтах. (Сколько места он занимает на диске)
        :en Property for getting the file size in bytes. (How much space does it take up on disk)
        """
        return self.__file['size']

    @property
    def url(self) -> str:
        """
        :ru Свойство для получения ссылки для скачивания файла.
        :en Property for getting a link to download a file.
        """
        return self.__file['url']

    @property
    def date(self) -> int:
        """
        :ru Свойство для получения даты загрузки файла на сервер `ВКонтакте` (в формате Unix).
        :en Property for getting the file upload date to the `VKontakte` server (in Unix format).
        """
        return self.__file['date']

    @property
    def owner_id(self) -> int:
        """
        :ru Свойство для получения идентификатора пользователя/сообщества, загрузившего файл.
        :en Property for getting the ID of the user/community who uploaded the file.
        """
        return self.__file['owner_id']

    @property
    def access_key(self) -> str:
        """
        :ru Свойство для получения ключа доступа, для отправки файла другим пользователям.
        :ru Property for obtaining an access key, for sending a file to other users.
        """
        return self.__file['access_key']

    def get_attachment(self) -> str:
        """
        :ru Метод для получения строки идентификатора файла.
        :en Method for getting the file ID string.
        """
        return f"doc{self.owner_id}_{self.id}_{self.access_key}"

    def save(self, path_to_save: str) -> None:
        """
        :ru Метод для сохранения файла в системе.
        :en Method for saving a file in the system.
        """
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if not path_to_save.endswith(self.extension):
            raise Exception(f"Invalid extension to save the file, please save the file in '.{self.extension}' format")
        urllib.request.urlretrieve(self.url, path_to_save)