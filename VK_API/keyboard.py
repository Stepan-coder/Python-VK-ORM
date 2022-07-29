from enum import Enum
from typing import Any
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class KeyboardButton(Enum):
    #: Стандартная
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

    def add_button(self, text: str, button: KeyboardButton, color: VkKeyboardColor, payload: Any = None):
        if button == KeyboardButton.DEFAULT:
            self.__keyboard.add_button(label=text, color=color)
        elif button == KeyboardButton.OPENLINK:
            self.__keyboard.add_openlink_button(label=text, link=payload)
        elif button == KeyboardButton.CALLBACK:
            self.__keyboard.add_button(label=text, color=color, payload={"type": "show_snackbar", "text": payload})
        elif button == KeyboardButton.LOCATION:
            self.__keyboard.add_location_button()

    def add_line(self):
        self.__keyboard.add_line()

    def get_keyboard(self):
        return self.__keyboard.get_keyboard()


