from __future__ import annotations

import warnings
import traceback
from typing import Callable


from VK_API.upload import *
from VK_API.sender import *
from VK_API.person.person import *
from VK_API.input_message.message import *
from VK_API.message_extensions.keyboard import *
from VK_API.message_extensions.carousel import *
from vk_api import VkApi
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
    def APP_ID(self, app_id: int) -> None:
        """
        :ru Сеттер для свойства APP_ID
        :en Setter for the APP_ID property
        :param app_id:ru Новый ID сообщества ВКонтакте
        :param app_id:en New VKontakte community ID
        :type app_id: int
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

    @property
    def send(self) -> Sender:
        return Sender(vk=self.__vk)

    @property
    def upload(self) -> Upload:
        return Upload(vk=self.__vk)

    def run(self, init_method: Callable[['Bot', Message, tuple], None], args: tuple = None) -> None:
        while True:
            try:
                for event in self.longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        init_method(self, Message(event=event), args)
            except Exception as e:
                print(traceback.format_exc())

    def get_user_info(self, user_id: int) -> Person:
        result = self.__vk.users.get(user_ids=user_id,
                                     fields="about, bdate, sex, city, country, last_seen, online, domain, relation")
        return Person(person_json=result[0])

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
    def create_keyboard(inline: bool = False, one_time: bool = False) -> Keyboard:
        return Keyboard(inline=inline, one_time=one_time)

    @staticmethod
    def create_carousel() -> Carousel:
        return Carousel()
