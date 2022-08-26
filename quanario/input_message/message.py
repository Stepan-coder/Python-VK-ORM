import vk_api
from typing import Optional
from quanario.input_message.voice import *
from quanario.input_message.audio import *
from quanario.input_message.photo import *
from quanario.input_message.video import *  # Недоделано (проблемы со скачиванием)
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
        :ru Метод для получения информации о наличии голосовых сообщений во вложениях к сообщению от пользователя.
        :en A method for getting information about the presence of voice messages in attachments to a message
         from a user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'audio_message':
                counter += 1
        return counter > 0

    def is_audio(self) -> bool:
        """
        :ru Метод для получения информации о наличии музыки во вложениях к сообщению от пользователя.
        :en A method for getting information about the presence of music in attachments to a message from a user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'audio':
                counter += 1
        return counter > 0

    def is_photos(self) -> bool:
        """
        :ru Метод для получения информации о наличии фотографий во вложениях к сообщению от пользователя.
        :en Method for getting information about the presence of photos in attachments to a message from the user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'photo':
                counter += 1
        return counter > 0

    def is_videos(self) -> bool:
        """
        :ru Метод для получения информации о наличии видеозаписей во вложениях к сообщению от пользователя.
        :en Method for getting information about the presence of video recordings in attachments to a message from
         a user.
        """
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'video':
                counter += 1
        return counter > 0

    def is_files(self) -> bool:
        """
        :ru Метод для получения информации о наличии файлов/документов во вложениях к сообщению от пользователя.
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

    def get_voices(self) -> List[Voice]:
        """
        :ru Этот метод возвращает список экземпляров класса 'Voice'.
        :en This method returns a list of instances of the 'Voice' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no audio messages in this input_message!')
        return [Voice(attachment['audio_message']) for attachment in self.attachments
                if attachment['type'] == 'audio_message']

    def get_audios(self) -> List[Audio]:
        """
        :ru Этот метод возвращает список экземпляров класса 'Audio'.
        :en This method returns a list of instances of the 'Audio' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no audio messages in this input_message!')
        return [Audio(attachment['audio']) for attachment in self.attachments if attachment['type'] == 'audio']

    def get_photos(self) -> List[Photo]:
        """
        :ru Этот метод возвращает список экземпляров класса 'Photo'.
        :en This method returns a list of instances of the 'Photo' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no images in this input_message!')
        return [Photo(attachment['photo']) for attachment in self.attachments if attachment['type'] == 'photo']

    def get_videos(self) -> List[Video]:
        """
        :ru Этот метод возвращает список экземпляров класса 'Video'.
        :en This method returns a list of instances of the 'Video' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no video messages in this input_message!')
        return [Video(attachment['video']) for attachment in self.attachments if attachment['type'] == 'video']

    def get_files(self) -> List[File]:
        """
        :ru Этот метод возвращает список экземпляров класса 'File'.
        :en This method returns a list of instances of the 'File' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no document messages in this input_message!')
        return [File(attachment['doc']) for attachment in self.attachments if attachment['type'] == 'doc']

    def get_geo(self) -> List[Geo]:
        """
        :ru Этот метод возвращает список экземпляров класса 'Geo'.
        :en This method returns a list of instances of the 'Geo' class.
        """
        if not self.is_have_attachments():
            raise Exception('There are no geo messages in this input_message!')
        return [Geo(self.__event.object['message'])]



