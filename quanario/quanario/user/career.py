"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import json
from enum import Enum
from typing import Dict, Any


class Career:
    def __init__(self, career: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Каррьера'.
        :en Information about fields from the 'Career' section.

        :param career:ru Json объект полученный от 'Вконтакте'.
        :param career:en Json object received from 'Vkontakte'.
        :type career: Dict[str, Any]
        """
        self.__career = career

    @property
    def group_id(self) -> int:
        """
        :ru Свойство для получения идентификаторa сообщества (если доступно, иначе company).
        :en Property for getting the community ID (if available, otherwise company).
        """
        return self.__career['group_id'] if 'group_id' in self.__career else None

    @property
    def company(self) -> str:
        """
        :ru Свойство для получения названия компании (если доступно, иначе group_id).
        :en Property for getting the company name (if available, otherwise group_id).
        """
        return self.__career['company'] if 'company' in self.__career else None

    @property
    def city_id(self) -> int:
        """
        :ru Свойство для получения идентификаторa города, города (если доступно, иначе city_name).
        :en Everything to get the ids of the city, city (if is available, otherwise city_name).
        """
        return self.__career['city_id'] if 'city_id' in self.__career else None

    @property
    def city_name(self) -> str:
        """
        :ru Свойство для получения названия города.
        :en Property for getting the name of the city.
        """
        return self.__career['city_name'] if 'city_name' in self.__career else None

    @property
    def country_id(self) -> int:
        """
        :ru Свойство для получения идентификаторa страны.
        :ru Property for getting the country ID.
        """
        return self.__career['country_id'] if 'country_id' in self.__career else None

    @property
    def work_from(self) -> int:
        """
        :ru Свойство для получения года начала работы.
        :en Property for getting the year of the start of work.
        """
        return self.__career['from'] if 'from' in self.__career else None

    @property
    def work_until(self) -> int:
        """
        :ru Свойство для получения года окончания работы.
        :en Property for getting the year of completion of work.
        """
        return self.__career['until'] if 'until' in self.__career else None

    @property
    def position(self) -> str:
        """
        :ru Свойство для получения названия должности
        :en Property for getting the title of the position
        """
        return self.__career['position'] if 'position' in self.__career else None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'Career'.
        :en This method generates a json object from the fields of the 'Career' class.
        """
        return {"group_id": self.group_id,
                "company": self.company,
                "city_id": self.city_id,
                "city_name": self.city_name,
                "country_id": self.country_id,
                "from": self.work_from,
                "until": self.work_until,
                "position": self.position}
