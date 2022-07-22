import os
import urllib.request
from typing import List

[{'type': 'audio_message', 'audio_message': {'duration': 3, 'id': 642928275, 'link_mp3': 'https://psv4.userapi.com/s/v1/amsg/kHdbiArtBQ78QkhumH2itbscGphO_0aXKD5sq67YjazXLmRGQGk5zG2GREF8OdK5Urta.mp3', 'link_ogg': 'https://psv4.userapi.com/s/v1/amsg/GVf-Xxzn6FZlcN-4vqcXjU26iW6TtC10qoCWIyvqRbHx2B52QNYjWTb55VE4h4c3TJBF.ogg', 'owner_id': 360919000, 'access_key': 'pDSmFtISfbQ3SiDPWYv5KwU5W2blmpdwxEV84kA7yWw', 'waveform': [3, 4, 4, 5, 6, 2, 3, 30, 13, 25, 18, 10, 18, 21, 26, 5, 9, 31, 24, 13, 10, 20, 21, 18, 17, 18, 16, 6, 5, 7, 8, 3, 3, 4, 26, 24, 13, 3, 24, 13, 20, 20, 5, 17, 18, 12, 8, 13, 23, 17, 10, 11, 11, 11, 7, 4, 6, 4]}}]


class AudioMessage:
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
    def url_oog(self) -> str:
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

    def save_oog(self, path_to_save: str):
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        if os.path.splitext(path_to_save)[1] != ".oog":
            raise Exception("Invalid extension to save the file, please save the file in '.oog' format")
        urllib.request.urlretrieve(self.url_oog, path_to_save)
