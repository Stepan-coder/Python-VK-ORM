import json
from typing import Dict, Any


class University:
    def __init__(self, university: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Университет'.
        :en Information about fields from the 'University' section.

        :param university:ru Json объект полученный от 'Вконтакте'.
        :param university:en Json object received from 'Vkontakte'.
        :type university: Dict[str, Any]
        """
        self.__university = university

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения идентификаторa университета.
        :en Property for getting the university ID.
        """
        return self.__university['id'] if 'id' in self.__university else None

    @property
    def name(self) -> str:
        """
        :ru Свойство для получения названия университета.
        :en Property for getting the name of the university.
        """
        return self.__university['name'] if 'name' in self.__university else None

    @property
    def city(self) -> int:
        """
        :ru Свойство для получения идентификаторa города, в котором расположен университет.
        :en Property for getting the ID of the city where the university is located.
        """
        return self.__university['city'] if 'city' in self.__university else None

    @property
    def country(self) -> int:
        """
        :ru Свойство для получения идентификаторa страны, в которой расположен университет.
        :en Property for obtaining the ID of the country in which the university is located.
        """
        return self.__university['country'] if 'country' in self.__university else None

    @property
    def faculty_id(self) -> int:
        """
        :ru Свойство для получения идентификатора факультета.
        :ru Property for getting the faculty ID.
        """
        return self.__university['faculty'] if 'faculty' in self.__university else None

    @property
    def faculty_name(self) -> str:
        """
        :ru Свойство для получения названия факультета.
        :en Property for getting the name of the faculty.
        """
        return self.__university['faculty_name'] if 'faculty_name' in self.__university else None

    @property
    def chair_id(self) -> int:
        """
        :ru Свойство для получения идентификатора кафедры.
        :en Property for getting the department ID.
        """
        return self.__university['chair'] if 'chair' in self.__university else None

    @property
    def chair_name(self) -> str:
        """
        :ru Свойство для получения названия кафедры.
        :en Property for getting the name of the department.
        """
        return self.__university['chair_name'] if 'chair_name' in self.__university else None

    @property
    def graduation(self) -> int:
        """
        :ru Свойство для получения года окончания.
        :en Property for getting the end year.
        """
        return self.__university['graduation'] if 'graduation' in self.__university else None

    @property
    def education_form(self) -> str:
        """
        :ru Свойство для получения формы обучения.
        :en Property for obtaining a form of training.
        """
        return self.__university['education_form'] if 'education_form' in self.__university else None

    @property
    def education_status(self) -> str:
        """
        :ru Свойство для получения статуса обучения.
        :en Property for getting the training status.
        """
        return self.__university['education_status'] if 'education_status' in self.__university else None

    def json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'School'.
        :en This method generates a json object from the fields of the 'School' class.
        """
        return {"id": self.id,
                "name": self.name,
                "city": self.city,
                "country": self.country,
                "faculty": self.faculty_id,
                "faculty_name": self.faculty_name,
                "chair": self.chair_id,
                "chair_name": self.chair_name,
                "graduation": self.graduation,
                "education_form": self.education_form,
                "education_status": self.education_status}
