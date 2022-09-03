from __future__ import annotations
import asyncio
import warnings
import traceback
from vk_api import VkApi
from typing import Callable, Awaitable
from quanario.send import *
from quanario.upload import *
from quanario.user.user import *
from quanario.input_message.message import *
from quanario.message_extensions.keyboard import *
from quanario.message_extensions.carousel import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class Bot(object):
    """
    :ru Основной класс библиотеки `quanario`, объединяющий в себе все доступные функции по приёму и отправке сообщений
      пользователям.
    :en The main class of the library is `quanario`, which combines all the available functions for receiving and
     sending messages to users.
    """
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
        :ru Свойство для получения объекта 'longpoll' (нужен для взаимодействия с серверами ВКонтакте)
        :en Property for getting a long poll object (needed for interacting with VKontakte servers)
        """
        return self.__longpoll

    @property
    def send(self) -> Send:
        """
        :ru Свойство для получения экземпляра класса 'Send'. Этот класс реализует функционал отправки различных типов
         сообщений пользователю.
        :en Property for getting an instance of the 'Send' class. This class implements the functionality of sending
         various types of messages to the user.
        """
        return Send(vk=self.__vk)

    @property
    def upload(self) -> Upload:
        """
        :ru Свойство для получения экземпляра класса 'Upload'. Этот класс реализует функционал публикации контента на
         сервер ВКонтакте
        :en Property for getting an instance of the 'Upload' class. This class implements the functionality of
         publishing content on vkontakte server
        """
        return Upload(vk=self.__vk)

    def run(self,
            init_method: Callable[['Bot', Message, tuple], Optional[Awaitable[None]]],
            is_async: bool = False,
            args: tuple = None) -> None:
        """
        :ru Основной метод класса 'Bot'. Он запускает вызов метода 'init_method' в вечном цикле для получения и
         обработки сообщений от пользователя.
        :en The main method of the 'Bot' class. It launches a call to the 'init_method' method in an eternal loop to
         receive and process messages from the user.

        :param init_method:ru Ссылка на метод, который необходимо вызывать при получении сообщений от пользователей.
         Подробнее см. примеры.
        :param init_method:en Reference to the method to be called when receiving messages from users.
         For more information, see the examples.
        :type init_method: Callable

        :param is_async:ru Аргумент, отвечающий за перевод бота в асинхронный режим, для увеличения производительности
        :param is_async:en The argument responsible for switching the bot to asynchronous mode to increase performance
        :type is_async: bool

        :param args:ru Кортеж аргументов, которые необходимо передать в init_method
        :param args:en Tuple of arguments to be passed to init_method
        :type args: tuple
        """
        while True:
            try:
                for event in self.longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        if is_async:
                            asyncio.run(init_method(self, Message(event=event), args))
                        else:
                            init_method(self, Message(event=event), args)
            except Exception as e:
                print(traceback.format_exc())

    def get_user_info(self, user_id: int) -> User:
        """
        :ru Этот метод делает запрос в ВКонтакте на получение информации о пользователе, в ответ он получает json,
         который преобразуется в экземпляр класса 'User'.
        :en This method makes a request in VKontakte to get information about the user, in response it receives json,
         which is converted into an instance of the 'User' class.

        :param user_id:ru Уникальный id пользователя для которого необходимо получить информацию.
        :param user_id:ru The unique ID of the user for whom you need to get information.
        :type user_id: int
        """
        result = self.__vk.users.get(user_ids=user_id,
                                     fields="about, activities, bdate, books, career, city, connections, counters, "
                                            "country, domain, education, followers_count, games, has_mobile, has_photo,"
                                            "home_town, interests, is_no_index, last_seen, military, movies, music, "
                                            "occupation, online, personal, quotes, relatives, relation, schools, "
                                            "screen_name, sex, site, status, timezone, trending, tv, universities, "
                                            "verified, wall_default, phone")
        return User(user=result[0])

    @staticmethod
    def create_keyboard(inline: bool = False, one_time: bool = False) -> Keyboard:
        """
        :ru Статический метод класса 'Bot' позволяющий получить экземпляр класса 'Keyboard' для создания клавиатуры.
        :en Static method of the 'Bot' class that allows you to get an instance of the 'Keyboard' class to create a
         keyboard.

        :param inline:ru Аргумент отвечающий за прикрепление клавиатуры к диалогу (True)/ прикрепление клавиатуры к
         нижней части экрана (False).
        :param inline:en Argument responsible for attaching the keyboard to the dialog (True)/ attaching the keyboard
         to the bottom of the screen (False).
        :type inline: bool

        :param one_time:ru Этот аргумент обязательно выставлен в 'True' если аргумент 'inline' выставлен в значении
         'True'. Его основная задача заключается в повторном отображении клавиатуры.
        :param one_time:en This argument must be set to 'True' if the 'inline' argument is set to 'True'. Its main task
         is to re-display the keyboard.
        :type one_time: bool
        :return:
        """
        return Keyboard(inline=inline, one_time=one_time)

    @staticmethod
    def create_carousel() -> Carousel:
        """
        :ru Статический метод класса 'Bot' позволяющий получить экземпляр класса 'Carousel' для создания карусели.
        :en Static method of the 'Bot' class that allows you to get an instance of the 'Carousel' class to create a
         carousel.
        """
        return Carousel()

    def __bot_boot(self) -> None:
        """
        :ru Приватный метод класса 'Bot', который производит авторизацию бота в ВКонтакте.
        :en A private method of the 'Bot' class that authorizes the bot in VKontakte.
        """
        if self.__TOKEN is not None and self.APP_ID is not None:
            self.__vk_session = VkApi(token=self.__TOKEN)
            self.__vk_session.RPS_DELAY = 1 / 100
            self.__longpoll = VkBotLongPoll(self.__vk_session, self.__APP_ID)
            self.__vk = self.__vk_session.get_api()
        else:
            warnings.warn("Bot was not restarted! 'TOKEN' and 'APP_ID' are required fields for user authorization!",
                          Warning)
