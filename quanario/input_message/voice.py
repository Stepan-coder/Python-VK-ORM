import os
import urllib.request
from typing import List


class Voice:
    def __init__(self, audio_message: dict):
        self.__audio_message = audio_message

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения уникального идентификатор файла.
        :en Property for getting a unique file identifier.
        """
        return self.__audio_message['id']

    @property
    def duration(self) -> int:
        """
        :ru Свойство для получения длительности аудиофайла.
        :en Property for getting the duration of an audio file.
        """
        return self.__audio_message['duration']

    @property
    def url_mp3(self) -> str:
        """
        :ru Свойство для получения ссылки для скачивание файла в формате '.mp3'.
        :en Property for getting a link to download a file in the '.mp3' format.
        """
        return self.__audio_message['link_mp3']

    @property
    def url_ogg(self) -> str:
        """
        :ru Свойство для получения ссылки для скачивание файла в формате '.ogg'.
        :en Property for getting a link to download a file in the '.ogg' format.
        """
        return self.__audio_message['link_ogg']

    @property
    def owner_id(self) -> int:
        """
        :ru Свойство для получения идентификатора пользователя/сообщества, загрузившего файл.
        :en Property for getting the ID of the user/community who uploaded the file.
        """
        return self.__audio_message['owner_id']

    @property
    def access_key(self) -> str:
        """
        :ru Свойство для получения ключа доступа, для отправки файла другим пользователям.
        :ru Property for obtaining an access key, for sending a file to other users.
        """
        return self.__audio_message['access_key']

    @property
    def waveform(self) -> List[int]:
        """
        :ru Свойство для получения графика изменения громкости файла.
        :ru Property for getting a graph of file volume changes.
        """
        return self.__audio_message['waveform']

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

    def save_ogg(self, path_to_save: str) -> None:
        """
        :ru Метод для сохранения файла в системе в формате '.ogg'.
        :en A method for saving a file in the system in '.ogg' format.
        """
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if os.path.splitext(path_to_save)[1] != ".ogg":
            raise Exception("Invalid extension to save the file, please save the file in '.ogg' format")
        urllib.request.urlretrieve(self.url_ogg, path_to_save)
