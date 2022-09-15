"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import json
from enum import Enum
from typing import Any, Dict, List
from prettytable import PrettyTable
from .keyboard import *
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class CarouselElement:
    """
    ru: Класс представляющий собой один элемент `карусели`.
    en: A class representing a single `carousel` element.
    """
    def __init__(self, title: str, description: str, attachment: str, keyboard: Keyboard = None):
        """
        :param title:ru Короткий заголовок блока, при его написании не рекомендуется использовать более 30 символов.
        :param title:en It is a short block title, it is not recommended to use more than 30 characters when writing it.
        :type title: str

        :param description:ru Описание того, что находится на блоке, рекомендуемое количество символов - 80
        :param description:en Description of what is on the block, the recommended number of characters is 80
        :type description: str

        :param attachment:ru Изображение, которое будет добавлено к блоку карусели. В 'attachment' необходимо
         передать результат загрузки изображения через 'bot.upload.photo'.
        :param attachment:en Image to be added to the carousel block. In the 'attachment' it is necessary to pass the
         result of uploading the image via 'bot.upload.photo'.
        :type attachment: str
        """
        self.__title = self.__check_length(title, 30)
        self.__description = self.__check_length(description, 80)
        self.__attachment = self.__cut_attachment(attachment=attachment)
        self.__keyboard = self.__extract_keyboard_buttons(keyboard=keyboard)

    @property
    def title(self) -> str:
        """
        ru: Это свойство возвращает заголовок блока.
        en: This property contains the block header.
        """
        return self.__title

    @title.setter
    def title(self, new_title: str) -> None:
        """
        ru: Сеттер для свойства 'title' позволяет установить новое значение для свойства.
        en: The setter for the 'title' property allows you to set a new value for the property.

        :param new_title:ru Короткий заголовок блока, при его написании не рекомендуется использовать более 30 символов.
        :param new_title:en It is a short block title, it is not recommended to use more than 30 characters when writing
         it.
        :type new_title: str
        """
        self.__title = self.__check_length(new_title, 30)

    @property
    def description(self) -> str:
        """
        ru: Это свойство возвращает описание блока.
        en: This property contains the block description.
        """
        return self.__description

    @description.setter
    def description(self, new_description: str) -> None:
        """
        ru: Сеттер для свойства 'description' позволяет установить новое значение для свойства.
        en: The setter for the 'description' property allows you to set a new value for the property.

        :param new_description:ru Описание того, что находится на блоке, рекомендуемое количество символов - 80
        :param new_description:en Description of what is on the block, the recommended number of characters is 80
        :type new_description: str
        """
        self.__description = self.__check_length(new_description, 80)

    @property
    def attachment(self) -> str:
        """
        ru: Это свойство возвращает ссылку картинки блока.
        en: This property contains a link to the block image.
        """
        return self.__attachment

    @attachment.setter
    def attachment(self, new_attachment: str) -> None:
        """
        ru: Сеттер для свойства 'attachment' позволяет установить новое значение для свойства.
        en: The setter for the 'attachment' property allows you to set a new value for the property.

        :param new_attachment:ru Изображение, которое будет добавленно к блоку карусели. В 'attachment' необходимо
         передать результат загрузки изображения через 'bot.upload.photo'.
        :param new_attachment:en Image to be added to the carousel block. In the 'attachment' it is necessary to pass
         the result of uploading the image via 'bot.upload.photo'.
        :type new_attachment: str
        """
        self.__attachment = self.__cut_attachment(attachment=new_attachment)

    @property
    def keyboard(self) -> json:
        """
        ru: Это свойство возвращает json с кнопками для элемента.
        en: This property contains json with buttons for the element.
        """
        return self.__keyboard

    @keyboard.setter
    def keyboard(self, new_keyboard: Keyboard) -> None:
        """
        ru: Сеттер для свойства 'keyboard' позволяет установить новое значение для свойства.
        en: The setter for the 'keyboard' property allows you to set a new value for the property.

        :param new_keyboard:ru Объект класс 'Keyboard', необходим для прикрепления кнопок к клавиатуре
        :param new_keyboard:en An object of the 'Keyboard' class, necessary for attaching buttons to the keyboard
        """
        self.__keyboard = self.__extract_keyboard_buttons(keyboard=new_keyboard)

    def compile(self) -> Dict[str, Any]:
        """
        ru: Этот метод производит 'сборку' блока карусели, для последующей отправки её пользователю.
        en: This method performs the 'assembly' of the carousel block, for subsequent sending it to the user.
        """
        if self.__title is None:
            raise IOError("В карточке не может отсутствовать поле title")
        if self.__description is None:
            raise IOError("В карточке не может отсутствовать поле description")
        return {"title": self.__title if self.__title is not None else "",
                "description": self.__description if self.__description is not None else "",
                "photo_id": self.__attachment if self.__attachment is not None else "",
                "action": {"type": "open_photo"},
                "buttons": self.__keyboard}

    @staticmethod
    def __check_length(text: str, count: int) -> str:
        """
        ru: Этот приватный метод укорачивает входную строку до указанной 'count' длины.
        en: This privat method shortens the input string to the specified 'count' length.

        :param text:ru Входной текст который возможно необходимо укоротить.
        :param text:en Input text that may need to be shortened.
        :type text: str

        :param count:ru Количество символов, до которого, в случае необходимости, необходимо укоротить входную строку.
        :param count:en The number of characters to which, if necessary, it is necessary to shorten the input string.
        :type count: int
        """
        return text if len(text) <= count else text[:count]

    @staticmethod
    def __cut_attachment(attachment: str) -> str:
        """
        ru: Этот приватный метод выделяет из входного 'проложения' уникальное id изображения
        en: This private method allocates a unique image id from the input 'attachment'

        :param attachment:ru Предоставленное пользователем вложение.
        :param attachment:en User-provided attachment.
        :type attachment: str
        """
        attachment = attachment.replace('photo', '')
        return "_".join(attachment.split('_')[:2])

    @staticmethod
    def __extract_keyboard_buttons(keyboard: Keyboard) -> json:
        """
        ru: Этот `приватный` метод позволяет подготовить клавиатуру для добавления её в блок `карусели`. Он необходим, так как клавиатура для `карусели` не может содержать несколько кнопок `в ряд`.
        en: This `private` method allows you to prepare the keyboard for adding it to the `carousel` block. It is necessary because the keyboard for the `carousel` cannot contain several buttons `in a row`.

        :param keyboard:ru Объект клавиатуры, который необходимо преобразовать
        :param keyboard:en Keyboard object to be converted.
        :type keyboard: keyboard
        """
        if keyboard is not None:
            buttons = []
            for line in json.loads(keyboard.get_keyboard())['buttons']:
                for button in line:
                    buttons.append(button)
            return buttons
        else:
            return None


class Carousel:
    """
    ru: Основной класс для создания вложений типа "Карусель".
     Отличие карусели от обычных сообщений это её необычный внешний вид, карусель состоит из блоков (максимум 10 шт.),
     в каждом блоке есть заголовок, описание и картинка. В последствии есть возможность прикрепить к каждому блоку
     уникальную клавиатуру. !!!Важно, чтобы количество кнопок совпадало во всех блоках!!!

    en: The main class for creating attachments of the "Carousel" type.
     The difference between the carousel and ordinary messages is its unusual appearance, the carousel consists of blocks
     (maximum 10 pcs.), each block has a title, description and picture. Subsequently, it is possible to attach to each
     block unique keyboard. !!!It is important that the number of buttons matches in all blocks!!!
    """

    def __init__(self):
        self.__elements: List[CarouselElement] = []
        self.__last_element = None

    @property
    def count(self) -> int:
        """
        ru: Это свойство возвращает количество элементов в карусели
        en: This property contains the number of elements in the carousel
        """
        return len(self.__elements)

    @property
    def last_element(self) -> CarouselElement:
        """
        ru: Это свойство возвращает последний добавленный в карусель элемент, тем самым открывет возможность его
         редактирования, например, для изменения описания или изменения фотографии.

        en: This property contains the last element added to the carousel, thereby opening the possibility of its
         editing, for example, to change the description or change the photo.
        """
        if self.count == 0:
            raise Exception("There are no carousels yet! Add them using the 'add_element' method!")
        return self.__elements[-1]

    def add_element(self, title: str, description: str, attachment: str, keyboard: Keyboard = None) -> None:
        """
        ru: Этот метод создаёт новый блок для карусели и добавляет его к уже существующим.
        en: This method creates a new block for the carousel and adds it to the existing ones.

        :param title:ru Короткий заголовок блока, при его написании не рекомендуется использовать более 30 символов.
        :param title:en It is a short block title, it is not recommended to use more than 30 characters when writing it.
        :type title: str

        :param description:ru Описание того, что находится на блоке, рекомендуемое количество символов - 80
        :param description:en Description of what is on the block, the recommended number of characters is 80
        :type description: str

        :param attachment:ru Изображение, которое будет добавлено к блоку карусели. В 'attachment' необходимо
         передать результат загрузки изображения через 'bot.upload.photo'.
        :param attachment:en Image to be added to the carousel block. In the 'attachment' it is necessary to pass the
         result of uploading the image via 'bot.upload.photo'.
        :type attachment: str
        """
        if self.__last_element is not None:
            self.__elements.append(self.__last_element)
        self.__last_element = CarouselElement(title=title,
                                              description=description,
                                              attachment=attachment,
                                              keyboard=keyboard)

    def get_carousel(self) -> json:
        """
        ru: Этот метод производит 'сборку' всей карусели, для последующей отправки её пользователю.
        en: This method 'builds' the entire carousel, for later sending it to the user.
        """
        if self.__last_element is not None:
            if self.count > 0 and self.__elements[-1].title != self.__last_element.title or self.count == 0:
                self.__elements.append(self.__last_element)
        elements = {i: len(self.__elements[i].keyboard) for i in range(len(self.__elements))}
        if max(elements.values()) != min(elements.values()):
            table = PrettyTable()
            table.title = "Carousel buttons"
            table.field_names = ["  ID  ", "    Count   "]
            for elem in elements:
                table.add_row([elem, elements[elem]])
            print(table)
            raise Exception('The number of buttons in each carousel block must be the same!')
        return json.dumps({"type": "carousel", "elements": [element.compile() for element in self.__elements]})


