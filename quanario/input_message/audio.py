import os
import urllib.request
from typing import Tuple


class Audio:
    def __init__(self, audio: dict):
        self.__audio = audio

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения уникального идентификатор файла.
        :en Property for getting a unique file identifier.
        """
        return self.__audio['id']

    @property
    def title(self) -> str:
        """
        :ru Свойство для получения названия аудиофайла.
        """
        return self.__audio['title']

    @property
    def artist(self) -> str:
        """
        :ru Свойство для получения имени исполнителя.
        """
        return self.__audio['artist']

    @property
    def date(self) -> int:
        """
        :ru Свойство для получения даты загрузки файла на сервер `ВКонтакте` (в формате Unix).
        :en Property for getting the file upload date to the `VKontakte` server (in Unix format).
        """
        return self.__audio['date']

    @property
    def duration(self) -> int:
        """
        :ru Свойство для получения длительности музыки.
        :en Property for getting the duration of an audio.
        """
        return self.__audio['duration']

    @property
    def url_mp3(self) -> str:
        """
        :ru Свойство для получения ссылки для скачивания файла.
        :en Property for getting a link to download a file.
        """
        return self.__audio['url']

    @property
    def is_explicit(self) -> bool:
        return self.__audio['is_explicit']

    @property
    def is_focus_track(self) -> bool:
        return self.__audio['is_focus_track']

    @property
    def owner_id(self) -> int:
        """
        :ru Свойство для получения идентификатора пользователя/сообщества, загрузившего файл.
        :en Property for getting the ID of the user/community who uploaded the file.
        """
        return self.__audio['owner_id']

    @property
    def track_code(self) -> str:
        """
        :ru Свойство для получения ключа доступа, для отправки файла другим пользователям.
        :ru Property for obtaining an access key, for sending a file to other users.
        """
        return self.__audio['track_code']

    def save_mp3(self, path_to_save: str) -> None:
        """
        :ru Метод для сохранения файла в системе в формате '.mp3'.
        :en A method for saving a file in the system in '.mp3' format.
        """
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if os.path.splitext(path_to_save)[1] != ".mp3":
            raise Exception("Invalid extension to save the file, please save the file in '.mp3' format")
        urllib.request.urlretrieve(self.url_mp3, path_to_save)

