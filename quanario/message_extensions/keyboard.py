from enum import Enum
from typing import Any
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class VkKeyboardButton(Enum):

    #: Стандартная кнопка
    DEFAULT = 'default'

    #: Кнопка с ссылкой
    OPENLINK = "open_link"

    #: Callback-кнопка
    CALLBACK = "callback"

    #: Кнопка с местоположением
    LOCATION = "location"


class Keyboard:
    """
    ru: Клавиатура в мессенджерах особенный тип вложения, в отличие, от обычных текстовых сообщений она представляет
     собой инструмент интерактивного взаимодействия пользователя с ботом. Нажимая на кнопку, пользователь подаёт системе
     различные команды: если это обычные кнопки, то при нажатии на них, пользователь подаёт команду отправить сообществу
     текст, который написан на кнопка (т.е. происходит ускорение процесса набора текста), если же это ссылка или
     геопозиция, то система выполняет эти действия вне беседы с ботом (отправляет на сайт, отправляет метку на карте).

    en: The keyboard in messengers is a special type of attachment, unlike ordinary text messages, it is a tool for
     interactive user interaction with a bot. By clicking on the button, the user gives the system various commands:
     if these are ordinary buttons, then when clicking on them, the user gives the command to send the text to the
     community that is written on the button (i.e., the typing process is accelerated), if it is a link or a
     geo-location, then the system performs these actions outside of a conversation with the bot (sends to the site,
     sends a placemark on the map).
    """
    def __init__(self, inline: bool = False, one_time: bool = False):
        self.__keyboard = VkKeyboard(inline=inline, one_time=one_time)

    def add_button(self,
                   button_type: VkKeyboardButton,
                   text: str = None,
                   color: VkKeyboardColor = None,
                   payload: Any = None) -> None:
        if button_type == VkKeyboardButton.DEFAULT:
            self.__keyboard.add_button(label=text, color=color)
        elif button_type == VkKeyboardButton.OPENLINK:
            self.__keyboard.add_openlink_button(label=text, link=payload)
        elif button_type == VkKeyboardButton.CALLBACK:
            self.__keyboard.add_button(label=text, color=color, payload={"type": "show_snackbar", "text": payload})
        elif button_type == VkKeyboardButton.LOCATION:
            self.__keyboard.add_location_button()

    def add_line(self) -> None:
        self.__keyboard.add_line()

    def get_keyboard(self) -> str:
        """
        ru: По уму это json, но он возвращает в формате обычной строки
        en: This is json by mind, but it returns in the format of a regular string.
        """
        return self.__keyboard.get_keyboard()

    def get_empty_keyboard(self) -> str:
        """
        ru: По уму это json, но он возвращает в формате обычной строки
        en: This is json by mind, but it returns in the format of a regular string
        """
        return self.__keyboard.get_empty_keyboard()


