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


