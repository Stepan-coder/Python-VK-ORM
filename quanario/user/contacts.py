"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import json
from enum import Enum
from typing import Dict, Any


class Contacts:
    def __init__(self, contacts: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Contacts'.
        :en Information about fields from the 'Contacts'.

        :param contacts:ru Json объект полученный от 'Вконтакте'.
        :param contacts:en Json object received from 'Vkontakte'.
        :type contacts: Dict[str, Any]
        """
        self.__contacts = contacts

    @property
    def site(self) -> str:
        """
        :ru Свойство для получения адреса сайта, указанного в профиле.
        :en Property for getting the site address specified in the profile.
        """
        return self.__contacts['site'] if 'site' in self.__contacts else None

    @property
    def connections(self) -> Dict[str, Any]:
        """
        :ru Свойство для получения данных об указанных в профиле сервисах пользователя, таких как: skype, livejournal.
         Для каждого сервиса возвращается отдельное поле с типом string, содержащее никнейм пользователя.
         Например, "skype": "username".
        :en Property for getting data about the user's services specified in the profile, such as: skype, livejournal.
         A separate string field containing the user's nickname is returned for each service.
         For example, "skype": "username".
        """
        return self.__contacts['connections'] if 'connections' in self.__contacts else None

    @property
    def home_town(self) -> str:
        """
        :ru Свойство для получения названия родного города.
        :en Property for getting the name of the hometown.
        """
        return self.__contacts['home_town'] if 'home_town' in self.__contacts else None

    @property
    def city_id(self) -> int:
        """
        :ru Свойство для получения идентификатора города пользователя, который можно использовать для получения его
         названия с помощью метода 'database.getCitiesById'.
        :en Property for getting the user's city ID, which can be used to get it names using the
         'database' method.getCitiesById'.
        """
        return self.__contacts['city']['id'] if 'city' in self.__contacts else None

    @property
    def city_name(self) -> str:
        """
        :ru Свойство для получения названия города в котором находится пользователь.
        :en Property for getting the name of the city where the user is located.
        """
        return self.__contacts['city']['title'] if 'city' in self.__contacts else None

    @property
    def country_id(self) -> int:
        """
        :ru Свойство для получения идентификатора страны пользователя, который можно использовать для получения его
         названия с помощью метода database.getCitiesById.
        :en Property for getting the user's country ID, which can be used to get it names using the
         database method.getCitiesById.
        """
        return self.__contacts['country']['id'] if 'country' in self.__contacts else None

    @property
    def country_name(self) -> str:
        """
        :ru Свойство для получения названия страны в которой находится пользователь.
        :en Property for getting the name of the country in which the user is located.
        """
        return self.__contacts['country']['title'] if 'country' in self.__contacts else None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'Contacts'.
        :en This method generates a json object from the fields of the 'Contacts' class.
        """
        return {"site": self.site,
                "connections": self.connections,
                "home_town": self.home_town,
                "city_id": self.city_id,
                "city_name": self.city_name,
                "country_id": self.country_name}
