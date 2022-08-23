import vk_api
from typing import Optional
from quanario.input_message.photo import *
from quanario.input_message.video import *  # Недоделано (проблемы со скачиванием)
from quanario.input_message.voice import *
from quanario.input_message.file import *
from quanario.input_message.geoposition import *


class Message:
    def __init__(self, event: vk_api):
        self.__event = event

    @property
    def type(self):
        """
        :ru Свойство для получения типа сообщения.
        :en Property for getting the message type.
        """
        return self.__event.type

    @property
    def text(self) -> str:
        """
        :ru Свойство для получения текста сообщения отправленного пользователем.
        :en Property for receiving the text of the message sent by the user.
        """
        return self.__event.message.text

    @property
    def user_id(self) -> int:
        """
        :ru Свойство для получения типа сообщения
        :en Property for getting the message type
        """
        return self.__event.object.message['peer_id']

    @property
    def attachments(self) -> Optional[dict]:
        """
        :ru Свойство для получения списка вложений.
        :en Property for getting a list of attachments.
        """
        if len(self.__event.object['message']['attachments']) > 0:
            return self.__event.object['message']['attachments']
        elif 'geo' in self.__event.object['message']:
            return self.__event.object['message']
        else:
            return {}

    def is_have_attachments(self) -> bool:
        """
        :ru Метод для получения информации о наличии вложений в сообщении от пользователя.
        :en Method for getting information about the presence of attachments in a message from a user.
        """
        return len(self.attachments) > 0 or 'geo' in self.__event.object['message']

    def is_voices(self) -> bool:
        """
        :ru Метод для получения информации о наличии аудиофайлов во вложених к сообщению от пользователя.
        :en Method for getting information about the presence of audio files in attachments to a message from a user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'audio_message':
                counter += 1
        return counter > 0 and self.is_voices

    def is_photos(self) -> bool:
        """
        :ru Метод для получения информации о наличии фотографий во вложених к сообщению от пользователя.
        :en Method for getting information about the presence of photos in attachments to a message from the user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'photo':
                counter += 1
        return counter > 0 and self.is_photos

    def is_videos(self) -> bool:
        """
        :ru Метод для получения информации о наличии видеозаписей во вложених к сообщению от пользователя.
        :en Method for getting information about the presence of video recordings in attachments to a message from
         a user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'video':
                counter += 1
        return counter > 0 and self.is_videos

    def is_files(self) -> bool:
        """
        :ru Метод для получения информации о наличии файлов/документов во вложених к сообщению от пользователя.
        :en Method for getting information about the presence of files/documents in attachments to a message from the
         user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'doc':
                counter += 1
        return counter > 0 and self.is_files

    def is_geo(self) -> bool:
        """
        :ru Метод для получения информации об отправке геопозиции пользователем.
        :en Method for getting information about sending a geo position by the user.
        """
        return 'geo' in self.__event.object['message']

    def get_photos(self) -> List[PhotoMessage]:
        """
        :ru Этот метод возвращает список экземпляров класса 'PhotoMessage'.
        :en This method returns a list of instances of the 'PhotoMessage' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no images in this input_message!')
        return [PhotoMessage(attachment['photo']) for attachment in self.attachments
                if attachment['type'] == 'photo']

    def get_voices(self) -> List[Voice]:
        """
        :ru Этот метод возвращает список экземпляров класса 'Voice'.
        :en This method returns a list of instances of the 'Voice' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no audio messages in this input_message!')
        return [Voice(attachment['audio_message']) for attachment in self.attachments
                if attachment['type'] == 'audio_message']

    def get_videos(self) -> List[VideoMessage]:
        """
        :ru Этот метод возвращает список экземпляров класса 'VideoMessage'.
        :en This method returns a list of instances of the 'VideoMessage' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no video messages in this input_message!')
        return [VideoMessage(attachment['video']) for attachment in self.attachments
                if attachment['type'] == 'video']

    def get_files(self) -> List[FileMessage]:
        """
        :ru Этот метод возвращает список экземпляров класса 'FileMessage'.
        :en This method returns a list of instances of the 'FileMessage' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no document messages in this input_message!')
        return [FileMessage(attachment['doc']) for attachment in self.attachments
                if attachment['type'] == 'doc']

    def get_geo(self) -> List[GeoMessage]:
        """
        :ru Этот метод возвращает список экземпляров класса 'GeoMessage'.
        :en This method returns a list of instances of the 'GeoMessage' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no geo messages in this input_message!')
        return [GeoMessage(self.__event.object['message'])]



