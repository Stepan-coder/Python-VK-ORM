from typing import Dict, Any
from vkbox.user.person_enum import *


class School:
    def __init__(self, school: Dict[str, Any]):
        self.__school = school

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения идентификаторa школы.
        """
        return self.__school['id'] if 'id' in self.__school else None

    @property
    def name(self) -> str:
        """
        :ru Свойство для получения названия школы.
        """
        return self.__school['name'] if 'name' in self.__school else None

    @property
    def city(self) -> int:
        """
        :ru Свойство для получения идентификаторa города, в котором расположена школа.
        """
        return self.__school['city'] if 'city' in self.__school else None

    @property
    def country(self) -> int:
        """
        :ru Свойство для получения идентификаторa страны, в которой расположена школа.
        """
        return self.__school['country'] if 'country' in self.__school else None

    @property
    def year_from(self) -> int:
        """
        :ru Свойство для получения года начала обучения в школе.
        """
        return self.__school['year_from'] if 'year_from' in self.__school else None

    @property
    def year_to(self) -> int:
        """
        :ru Свойство для получения года окончания обучения в школе.
        """
        return self.__school['year_to'] if 'year_to' in self.__school else None

    @property
    def year_graduated(self) -> int:
        """
        :ru Свойство для получения года выпуска из школы.
        """
        return self.__school['year_graduated'] if 'year_graduated' in self.__school else None

    @property
    def school_class(self) -> str:
        """
        :ru Свойство для получения буквы класса.
        """
        return self.__school['class'] if 'class' in self.__school else None

    @property
    def speciality(self) -> str:
        """
        :ru Свойство для получения специализации класса в школе.
        """
        return self.__school['speciality'] if 'speciality' in self.__school else None

    @property
    def school_type(self) -> SchoolType:
        """
        :ru Свойство для получения идентификатора школы.
        """
        return self.__convert_school_type(school_type=self.__school['type']) if 'type' in self.__school else None

    @staticmethod
    def __convert_school_type(school_type: int) -> SchoolType:
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
