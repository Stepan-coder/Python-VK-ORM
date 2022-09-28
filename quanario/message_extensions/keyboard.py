"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""
import math
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
        self.__inline = inline
        self.__one_time = one_time
        self.__keyboard = VkKeyboard(inline=inline, one_time=one_time)

    def __str__(self):
        max_len = -1
        this_table = [[f"Keyboard(inline={self.__inline}, one_time={self.__one_time})"]]
        for line in self.__keyboard.lines:
            row = []
            row_len = 2 + len(row) - 1  # 2 * '|' + (count - 1) * '|' (between buttons)
            for button in line:
                label = ""
                if button['action']['type'] == 'text':
                    label = button['action']['label']
                elif button['action']['type'] == 'location':
                    label = 'LOCATION'
                elif button['action']['type'] == 'open_link':
                    label = 'OPENLINK'
                row.append(label)
                row_len += 2 + len(label) + 2  # '  ' + button_text + '  '
            this_table.append(row)
            if row_len > max_len:
                max_len = row_len
        table, last_row = "", ""
        for line in this_table:
            count = (max_len - (2 + len(line) - 1) - len(''.join(line))) / len(line) / 2
            row = f"+{''.join(['-' * (math.ceil(count) + len(button) + int(count)) + '+' for button in line])}\n"
            table += f"{Keyboard.__join_rows(last_row, row=row)}\n" if last_row != "" else row
            table += f"|{''.join([' ' * math.ceil(count) + button + ' ' * int(count) + '|' for button in line])}\n"
            last_row = row
        table += last_row
        return str(table)

    @property
    def lines(self):
        return self.__keyboard.lines

    def add_button(self,
                   button_type: VkKeyboardButton,
                   text: str = None,
                   color: VkKeyboardColor = None,
                   payload: Any = None) -> None:
        """
        ru: Этот метод добавляет кнопку с типом `button_type`, цветом `color`, вложением `payload` и текстом `text`
         `справа`, к имеющейся клавиатуре.
        en: This method adds a button with the type `button_type`, the color `color`, the attachment `payload` and
         the text `text` at the right, to the existing keyboard.
        """
        if button_type == VkKeyboardButton.DEFAULT:
            self.__keyboard.add_button(label=text, color=color)
        elif button_type == VkKeyboardButton.OPENLINK:
            self.__keyboard.add_openlink_button(label=text, link=payload)
        elif button_type == VkKeyboardButton.CALLBACK:
            self.__keyboard.add_button(label=text, color=color, payload={"type": "show_snackbar", "text": payload})
        elif button_type == VkKeyboardButton.LOCATION:
            self.__keyboard.add_location_button()

    def add_line(self) -> None:
        """
        ru: Этот метод делает перенос `курсора` кнопок на одну ячейку вниз. Т.е. по умолчанию кнопки добавляются в
         строку, вправо.
        en: This method moves the `cursor` of the buttons one cell down. I.e., by default, the buttons are added to the
         row, to the right.
        """
        self.__keyboard.add_line()

    def get_keyboard(self) -> str:
        """
        ru: По уму это json, но он возвращает в формате обычной строки.
        en: This is json by mind, but it returns in the format of a regular string.
        """
        return self.__keyboard.get_keyboard()

    def get_empty_keyboard(self) -> str:
        """
        ru: По уму это json, но он возвращает в формате обычной строки.
        en: This is json by mind, but it returns in the format of a regular string
        """
        return self.__keyboard.get_empty_keyboard()

    @staticmethod
    def __join_rows(last_row: str, row: str) -> str:
        if len(last_row) != len(row):
            raise Exception('')
        return ''.join(['+' if l == '+' or r == '+' else '-' for l, r in zip(last_row, row) if l != '\n' or r != '\n'])



