import json
from enum import Enum
from typing import Dict, Any


class Military:
    def __init__(self, military: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Военная служба'.
        :en Information about fields from the 'Military' section.

        :param military:ru Json объект полученный от 'Вконтакте'.
        :param military:en Json object received from 'Vkontakte'.
        :type military: Dict[str, Any]
        """
        self.__military = military

    @property
    def unit(self) -> str:
        """
        :ru Свойство для получения номера военной части.
        :en Property for getting the number of a military unit.
        """
        return self.__military['group_id'] if 'group_id' in self.__military else None

    @property
    def unit_id(self) -> int:
        """
        :ru Свойство для получения идентификатора части в базе данных.
        :en Property for getting the part ID in the database.
        """
        return self.__military['company'] if 'company' in self.__military else None

    @property
    def country_id(self) -> int:
        """
        :ru Свойство для получения идентификаторa страны, в которой находится часть.
        :en Property for getting the ID of the country where the part is located.
        """
        return self.__military['country_id'] if 'country_id' in self.__military else None

    @property
    def military_from(self) -> int:
        """
        :ru Свойство для получения года начала службы.
        :en Property for getting the year of service start.
        """
        return self.__military['from'] if 'from' in self.__military else None

    @property
    def military_until(self) -> int:
        """
        :ru Свойство для получения года окончания службы.
        :en Property for getting the end of service year.
        """
        return self.__military['until'] if 'until' in self.__military else None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'Military'.
        :en This method generates a json object from the fields of the 'Military' class.
        """
        return {"unit": self.unit,
                "unit_id": self.unit_id,
                "country_id": self.country_id,
                "from": self.military_from,
                "until": self.military_until}
