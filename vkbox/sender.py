import vk_api
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vkbox.message_extensions.keyboard import *
from vkbox.message_extensions.carousel import *


class Sender:
    def __init__(self, vk: vk_api.vk_api.VkApiMethod):
        self.__vk = vk

    def message(self, user_id: int, message: str, keyboard: Keyboard = None) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' сообщение с текстом 'message', при необходимости,
         иеется возможность прикрепить клавивтуру с кнопками - 'keyboard'. Подробнее о 'keyboard' см. документацию.
        en: This method allows you to send a message with the text 'message' to a user with the id 'user_id', if
         necessary, it is possible to attach a keyboard with buttons - 'keyboard'. For more information about
         'keyboard', see the documentation.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param message:ru Сообшение пользователю в формате обычной строки.
        :param message:en Message to the user in the format of a regular string.
        :type message: str

        :param keyboard:ru Экземпляр клавиатуры, который будет отправлен пользователю.
        :param keyboard:en An instance of the keyboard that will be sent to the user.
        :type keyboard: Keyboard
        """
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                keyboard=keyboard.get_keyboard() if keyboard is not None else None,
                                random_id=get_random_id())

    def carousel(self, user_id: int, message: str = None, carousel: Carousel = None) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' сообщение с текстом 'message', при необходимости,
         иеется возможность прикрепить карусель - 'carousel'. Подробнее о 'carousel' см. документацию.
        en: This method allows you to send a message with the text 'message' to a user with the id 'user_id', if
         necessary, it is possible to attach a carousel - 'carousel'. For more information about 'carousel', see the
         documentation.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param message:ru Сообшение пользователю в формате обычной строки.
        :param message:en Message to the user in the format of a regular string.
        :type message: str

        :param carousel:ru Экземпляр карусели, который будет отправлен пользователю.
        :param carousel:en An instance of the carousel that will be sent to the user.
        :type carousel: Carousel
        """
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                template=carousel.get_carousel() if carousel is not None else None,
                                random_id=get_random_id())

    def sticker(self, user_id: int, sticker_id: int) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' стикер с номером 'sticker_id'.
        en: This method allows you to send a sticker with the number 'sticker_id' to a user with the id 'user_id'.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param sticker_id:ru Уникальный id стикера.
        :param sticker_id:ru Unique sticker id.
        :type sticker_id: int
        """
        self.__vk.messages.send(peer_id=user_id,
                                sticker_id=sticker_id,
                                random_id=get_random_id())

    def voice(self, user_id: int, attachment: str, message: str = None) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' аудиофайл как голосовое сообщение.
        en: This method allows you to send an audio file to a user with the id 'user_id' as a voice message.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param message:ru Сообшение пользователю в формате обычной строки.
        :param message:en Message to the user in the format of a regular string.
        :type message: str

        :param attachment:ru Уникальная строка ссылка-идентификатор вложения.
        *Для оптравки пользователю вложений их необходимо загрузить на сервер ВКонтакте, в*
        """
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                attachment=attachment,
                                random_id=get_random_id())

    def photo(self, user_id: int, attachment: str, message: str = None):
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                attachment=attachment,
                                random_id=get_random_id())

    def file(self, user_id: int, attachment: str) -> None:
        self.__vk.messages.send(peer_id=user_id,
                                attachment=attachment,
                                random_id=get_random_id())





