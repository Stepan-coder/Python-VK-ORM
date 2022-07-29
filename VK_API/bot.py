from __future__ import annotations

import os
import warnings
import traceback
from typing import List, Callable
from VK_API.person import *
from VK_API.keyboard import *
from VK_API.input_message.message import *
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class Bot(object):
    def __init__(self, token: str = None, app_id: int = None):
        """
        :param token:ru Токен для авторизации бота в сообществе
        :param token:en Token used to authorize the bot in the community
        :param app_id:ru Идентификатор сообщества, к которому будет подключен бот
        :param app_id: ID of the community to which the bot will be connected
        """
        self.__TOKEN = token
        self.__APP_ID = app_id
        self.__bot_boot()

    @property
    def TOKEN(self) -> str:
        """
        :ru Свойство для получения токена сообщества
        :en Property for getting a community TOKEN
        """
        return self.__TOKEN

    @TOKEN.setter
    def TOKEN(self, token: str) -> None:
        """
        :ru Сеттер для свойства TOKEN
        :en Setter for the TOKEN property
        :param token:ru Новый токен сообщества ВКонтакте
        :param token:en New VKontakte community TOKEN
        """
        self.__TOKEN = token
        self.__bot_boot()

    @property
    def APP_ID(self) -> int:
        """
         :ru Свойство для получения ID сообщества
         :en Property for getting a community ID
         """
        return self.__APP_ID

    @APP_ID.setter
    def APP_ID(self, app_id: int):
        """
        :ru Сеттер для свойства APP_ID
        :en Setter for the APP_ID property
        :param app_id:ru Новый ID сообщества ВКонтакте
        :param app_id:en New VKontakte community ID
        :return:
        """
        self.__APP_ID = app_id
        self.__bot_boot()

    @property
    def vk(self) -> vk_api.vk_api.VkApiMethod:
        """
        :ru Свойство для получения основного объекта бота
        :en Property for getting the main bot object
        """
        return self.__vk

    @property
    def longpoll(self) -> vk_api.bot_longpoll.VkBotLongPoll:
        """
        :ru Свойство для получения объекта longpoll (нужен для взаимодействия с серверами ВКонтакте)
        :en Property for getting a long poll object (needed for interacting with VKontakte servers)
        """
        return self.__longpoll

    def run(self, init_method: Callable[['Bot', Message, tuple], None], args: tuple = None):
        while True:
            try:
                for event in self.longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW and  event.to_me:
                        init_method(self, Message(event=event), args)
            except Exception as e:
                print(traceback.format_exc())

    def get_user_info(self, user_id: int) -> Person:
        result = self.__vk.users.get(user_ids=user_id,
                                     fields="about, bdate, sex, city, country, last_seen, online, domain, relation")
        return Person(person_json=result[0])

    def send_message(self, user_id: int, message: str, keyboard=None) -> None:
        if keyboard is None:
            self.__vk.messages.send(peer_id=user_id,
                                    message=message,
                                    random_id=get_random_id())
        else:
            self.__vk.messages.send(peer_id=user_id,
                                    message=message,
                                    keyboard=keyboard,
                                    random_id=get_random_id())

    def send_sticker(self, user_id: int, sticker_id: int) -> None:
        self.__vk.messages.send(peer_id=user_id,
                                sticker_id=sticker_id,
                                random_id=get_random_id())

    def send_photo(self, user_id: int, path_to_photo: str, message: str = None) -> str:
        if not os.path.exists(path_to_photo):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        photo = upload.photo_messages(path_to_photo)
        attachment = f"photo{photo[0]['owner_id']}_{photo[0]['id']}_{photo[0]['access_key']}"
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                attachment=attachment,
                                random_id=get_random_id())
        return attachment

    def send_audio(self, user_id: int, path_to_audio: str, message: str = None) -> str:
        if not os.path.exists(path_to_audio):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        audio = upload.audio_message(path_to_audio, peer_id=user_id)
        attachment = f"audio_message{audio['audio_message']['owner_id']}_{audio['audio_message']['id']}"
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                attachment=attachment,
                                random_id=get_random_id())
        return attachment

    def send_document(self, user_id: int, path_to_document: str) -> str:
        if not os.path.exists(path_to_document):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        photo = upload.document_message(path_to_document,
                                        title=str(os.path.basename(path_to_document)).split(".")[0],
                                        peer_id=user_id)
        attachment = f"doc{photo['doc']['owner_id']}_{photo['doc']['id']}"
        self.__vk.messages.send(peer_id=user_id,
                                random_id=get_random_id(),
                                attachment=attachment)
        return attachment

    def resend_document(self, user_id: int, message: str, attachment: str):
        self.__vk.messages.send(peer_id=user_id,
                                random_id=get_random_id(),
                                attachment=attachment,
                                message=message)

    def __bot_boot(self) -> None:
        if self.__TOKEN is not None and self.APP_ID is not None:
            self.__vk_session = VkApi(token=self.__TOKEN)
            self.__vk_session.RPS_DELAY = 1 / 100
            self.__longpoll = VkBotLongPoll(self.__vk_session, self.__APP_ID)
            self.__vk = self.__vk_session.get_api()
        else:
            warnings.warn("Bot was not restarted! 'TOKEN' and 'APP_ID' are required fields for user authorization!",
                          Warning)

    @staticmethod
    def create_keyboard(inline: bool = False, one_time: bool = False):
        return Keyboard(inline=inline, one_time=one_time)
