import vk_api
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from quanario.message_extensions.keyboard import *
from quanario.message_extensions.carousel import *


class Send:
    """
    :ru Класс реализующий отправку медиаконтента пользователям.
    :en A class that implements sending media content to users.
    """
    def __init__(self, vk: vk_api.vk_api.VkApiMethod):
        self.__vk = vk

    def message(self, user_id: int, message: str, keyboard: Keyboard = None) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' сообщение с текстом 'message', при необходимости,
         имеется возможность прикрепить клавиатуру с кнопками - 'keyboard'. Подробнее о 'keyboard' см. документацию.
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

    def voice(self, user_id: int, attachment: str or List[str], message: str = None) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' аудиофайл как голосовое сообщение.
        en: This method allows you to send an audio file to a user with the id 'user_id' as a voice message.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param message:ru Сообщение пользователю в формате обычной строки.
        :param message:en Message to the user in the format of a regular string.
        :type message: str

        :param attachment:ru Уникальная строка ссылка-идентификатор вложения.
        :param attachment:en Unique string link-attachment ID.
        :type attachment: str

        ru: *Для отправки пользователю вложения типа 'голосовое сообщение', его предварительно необходимо загрузить на
         сервер ВКонтакте, с помощью 'voice' класса 'Upload'*
        en: *To send an attachment of the 'voice message' type to the user, it must first be uploaded to the VKontakte
         server using the 'voice' method of the 'Upload' class*
        """
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                attachment=attachment,
                                random_id=get_random_id())

    def photo(self, user_id: int, attachment: str or List[str], message: str = None) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' фотографию.
        en: This method allows you to send a photo to a user with the id 'user_id'.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param message:ru Сообщение пользователю в формате обычной строки.
        :param message:en Message to the user in the format of a regular string.
        :type message: str

        :param attachment:ru Уникальная строка ссылка-идентификатор вложения.
        :param attachment:en Unique string link-attachment ID.
        :type attachment: str or List[str]

        ru: *Для отправки пользователю вложения типа 'фотография', его предварительно необходимо загрузить на
         сервер ВКонтакте, с помощью 'photo' класса 'Upload'*
        en: *To send an attachment of the 'photo' type to the user, it must first be uploaded to the VKontakte server
         using the 'photo' method of the 'Upload' class*
        """
        self.__vk.messages.send(peer_id=user_id,
                                message=message,
                                attachment=attachment if isinstance(attachment, str) else ",".join(attachment),
                                random_id=get_random_id())

    def video(self, user_id: int, attachment: str or List[str]) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' файл. Файл
        en: This method allows you to send video file to a user with the id 'user_id'.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param attachment:ru Уникальная строка ссылка-идентификатор вложения.
        :param attachment:en Unique string link-attachment ID.
        :type attachment: str

        ru: *Для отправки пользователю вложения типа 'видео', в отличие от остальных типов вложений, для него необходимо
        получить 'attachment', с помощью метода 'get_attachment' класса 'VideoMessage'*
        en: *To send an attachment of the 'video' type to the user, unlike other types of attachments, it is necessary
         for him to get the 'attachment', using the 'get_attachment' method of the 'VideoMessage' class*
        """
        self.__vk.messages.send(peer_id=user_id,
                                attachment=attachment if isinstance(attachment, str) else ",".join(attachment),
                                random_id=get_random_id())

    def file(self, user_id: int, attachment: str or List[str]) -> None:
        """
        ru: Этот метод позволяет отправить пользователю с id 'user_id' файл. Файл
        en: This method allows you to send file to a user with the id 'user_id'.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param attachment:ru Уникальная строка ссылка-идентификатор вложения.
        :param attachment:en Unique string link-attachment ID.
        :type attachment: str

        ru: *Для отправки пользователю вложения типа 'файл', его предварительно необходимо загрузить на
         сервер ВКонтакте, с помощью метода 'file' класса 'Upload'*
        en: *To send an attachment of the 'file' type to the user, it must first be uploaded to the VKontakte server
         using the 'file' method of the 'Upload' class*
        """
        self.__vk.messages.send(peer_id=user_id,
                                attachment=attachment if isinstance(attachment, str) else ",".join(attachment),
                                random_id=get_random_id())





