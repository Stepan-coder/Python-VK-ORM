import os
import urllib.request
from typing import List


class Voice:
    def __init__(self, audio_message: dict):
        self.__audio_message = audio_message

    @property
    def id(self) -> int:
        return self.__audio_message['id']

    @property
    def duration(self) -> int:
        return self.__audio_message['duration']

    @property
    def url_mp3(self) -> str:
        return self.__audio_message['link_mp3']

    @property
    def url_ogg(self) -> str:
        return self.__audio_message['link_ogg']

    @property
    def owner_id(self) -> int:
        return self.__audio_message['owner_id']

    @property
    def access_key(self) -> str:
        return self.__audio_message['access_key']

    @property
    def waveform(self) -> List[int]:
        return self.__audio_message['waveform']

    def save_mp3(self, path_to_save: str):
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if os.path.splitext(path_to_save)[1] != ".mp3":
            raise Exception("Invalid extension to save the file, please save the file in '.mp3' format")
        urllib.request.urlretrieve(self.url_mp3, path_to_save)

    def save_ogg(self, path_to_save: str):
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if os.path.splitext(path_to_save)[1] != ".ogg":
            raise Exception("Invalid extension to save the file, please save the file in '.ogg' format")
        urllib.request.urlretrieve(self.url_ogg, path_to_save)
