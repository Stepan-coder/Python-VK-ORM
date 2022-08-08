import json
from typing import Dict, Any
from vkbox.user.enum import *


class School:
    def __init__(self, school: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Школа'.
        :en Information about fields from the 'School' section.

        :param school:ru Json объект полученный от 'Вконтакте'.
        :param school:en Json object received from 'Vkontakte'.
        :type school: Dict[str, Any]
        """
        self.__school = school

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения идентификаторa школы.
        :en Property for getting the school ID.
        """
        return self.__school['id'] if 'id' in self.__school else None

    @property
    def name(self) -> str:
        """
        :ru Свойство для получения названия школы.
        :en Property for getting the name of the school.
        """
        return self.__school['name'] if 'name' in self.__school else None

    @property
    def city(self) -> int:
        """
        :ru Свойство для получения идентификаторa города, в котором расположена школа.
        :en Property for getting the ID of the city where the school is located.
        """
        return self.__school['city'] if 'city' in self.__school else None

    @property
    def country(self) -> int:
        """
        :ru Свойство для получения идентификаторa страны, в которой расположена школа.
        :en Property for getting the ID of the country where the school is located.
        """
        return self.__school['country'] if 'country' in self.__school else None

    @property
    def year_from(self) -> int:
        """
        :ru Свойство для получения года начала обучения в школе.
        :en Property for getting the year of starting school.
        """
        return self.__school['year_from'] if 'year_from' in self.__school else None

    @property
    def year_to(self) -> int:
        """
        :ru Свойство для получения года окончания обучения в школе.
        :en Property for getting the year of graduation from school.
        """
        return self.__school['year_to'] if 'year_to' in self.__school else None

    @property
    def year_graduated(self) -> int:
        """
        :ru Свойство для получения года выпуска из школы.
        :en Property for getting the year of graduation from school.
        """
        return self.__school['year_graduated'] if 'year_graduated' in self.__school else None

    @property
    def school_class(self) -> str:
        """
        :ru Свойство для получения буквы класса.
        :en Property for getting a class letter.
        """
        return self.__school['class'] if 'class' in self.__school else None

    @property
    def speciality(self) -> str:
        """
        :ru Свойство для получения специализации класса в школе.
        :en Property for getting a class specialization at school.
        """
        return self.__school['speciality'] if 'speciality' in self.__school else None

    @property
    def school_type(self) -> SchoolType:
        """
        :ru Свойство для получения идентификатора школы.
        :en Property for getting the school ID.
        """
        return self.__convert_school_type(school_type=self.__school['type']) if 'type' in self.__school else None

    def json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'School'.
        :en This method generates a json object from the fields of the 'School' class.
        """
        return {"id": self.id,
                "name": self.name,
                "city": self.city,
                "country": self.country,
                "year_from": self.year_from,
                "year_to": self.year_to,
                "year_graduated": self.year_graduated,
                "school_class": self.school_class,
                "speciality": self.speciality,
                "school_type": self.school_type.value}

    @staticmethod
    def __convert_school_type(school_type: int) -> SchoolType:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'school_type' в Enum 'SchoolType'.
        :en This private method converts the numeric representation of the value 'school_type' to Enum 'SchoolType'.

        :param school_type:ru Числовое представление значения 'school_type'.
        :param school_type:en Numeric representation of the 'school_type' value.
        :type school_type: int
        """
        if school_type == 0:
            return SchoolType.SCHOOL
        elif school_type == 1:
            return SchoolType.GYMNASIUM
        elif school_type == 2:
            return SchoolType.LYCEUM
        elif school_type == 3:
            return SchoolType.BOARDING_SCHOOL
        elif school_type == 4:
            return SchoolType.EVENING_SCHOOL
        elif school_type == 5:
            return SchoolType.MUSIC_SCHOOL
        elif school_type == 6:
            return SchoolType.SPORTS_SCHOOL
        elif school_type == 7:
            return SchoolType.ART_SCHOOL
        elif school_type == 8:
            return SchoolType.COLLAGE
        elif school_type == 9:
            return SchoolType.PROFESSIONAL_LYCEUM
        elif school_type == 10:
            return SchoolType.TECHNICAL_SCHOOL
        elif school_type == 11:
            return SchoolType.VOCATIONAL_SCHOOL
        elif school_type == 12:
            return SchoolType.UCHILISHE
        elif school_type == 13:
            return SchoolType.SCHOOL_OF_ARTS
        else:
            raise Exception("Invalid value!")
