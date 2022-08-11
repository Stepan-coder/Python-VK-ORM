import json
from enum import Enum
from typing import Dict, Any


class OccupationType(Enum):
    WORK = "WORK"  # Работа
    SCHOOL = "SCHOOL"  # Школа
    UNIVERSITY = "UNIVERSITY"  # Университет


class Occupation:
    def __init__(self, occupation: Dict[str, Any]):
        """
        :ru Информация о текущем роде занятия пользователя.
        :en Information about the user's current occupation.

        :param occupation:ru Json объект полученный от 'Вконтакте'.
        :param occupation:en Json object received from 'Vkontakte'.
        :type occupation: Dict[str, Any]
        """
        self.__occupation = occupation

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения идентификаторa деятельности.
        :en Property for getting the activity ID.
        """
        return self.__occupation['id'] if 'id' in self.__occupation else None

    @property
    def name(self) -> str:
        """
        :ru Свойство для получения названия деятельности.
        :en Property for getting the name of the activity.
        """
        return self.__occupation['name'] if 'name' in self.__occupation else None

    @property
    def type(self) -> OccupationType:
        """
        :ru Свойство для получения типа деятельности.
        :en Property for getting the type of activity.
        """
        return self.__convert_occupation_type(self.__occupation['type']) if 'type' in self.__occupation else None

    def json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'Occupation'.
        :en This method generates a json object from the fields of the 'Occupation' class.
        """
        return {"id": self.id,
                "name": self.name,
                "type": self.type.name}

    @staticmethod
    def __convert_occupation_type(occupation_type: str) -> OccupationType:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'occupation_type' в Enum 'Platform'.
        :en This private method converts the numeric representation of the value 'occupation_type' to Enum 'Platform'.

        :param occupation_type:ru Числовое представление значения 'occupation_type'.
        :param occupation_type:en Numeric representation of the 'occupation_type' value.
        :type occupation_type: int
        """
        if occupation_type == 'work':
            return OccupationType.WORK  # Работа
        elif occupation_type == 'school':
            return OccupationType.SCHOOL  # Школа
        elif occupation_type == 'university':
            return OccupationType.UNIVERSITY  # Университет
        else:
            raise Exception(f"Invalid value '{occupation_type}' for Enum 'OccupationType'!")