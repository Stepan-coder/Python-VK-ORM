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
        :param user_id:
        :param message:
        :param keyboard:
        :return:
        """
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                keyboard=keyboard.get_keyboard() if keyboard is not None else None,
                                random_id=get_random_id())

    def sticker(self, user_id: int, sticker_id: int) -> None:
        self.__vk.messages.send(peer_id=user_id,
                                sticker_id=sticker_id,
                                random_id=get_random_id())

    def voice(self, user_id: int, attachment: str, message: str = None) -> None:
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

    def carousel(self, user_id: int, message: str = None, carousel: Carousel = None) -> None:
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                template=carousel.get_carousel() if carousel is not None else None,
                                random_id=get_random_id())



