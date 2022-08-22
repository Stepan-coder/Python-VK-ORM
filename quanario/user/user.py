from enum import Enum

from quanario.user.params import *
from quanario.user.career import *
from quanario.user.military import *
from quanario.user.counters import *
from quanario.user.contacts import *
from quanario.user.interests import *
from quanario.user.occupation import *
from quanario.user.lifeposition import *
from quanario.user.education.education import *
from typing import Dict, Any, List, Optional


class Sex(Enum):
    NOT_SPECIFIED = "NOT SPECIFIED"  # Пол не указан
    FEMALE = "FEMALE"  # Женщина
    MALE = "MALE"  # Мужщина


class Relation(Enum):
    NOT_SPECIFIED = "NOT SPECIFIED"
    NOT_MARRIED = "NOT MARRIED"
    HAVE_FRIEND = "HAVE FRIEND"
    ENGAGED = "ENGAGED"
    EVERYTHING_IS_COMPLICATED = "EVERYTHING_IS_COMPLICATED"
    ACTIVE_SEARCH = "ACTIVE_SEARCH"
    IN_LOVE = "IN LOVE"
    CIVIL_MARRIAGE = "CIVIL MARRIAGE"


class Online(Enum):
    ONLINE = "ONLINE"  # Пользователь онлайн
    NOT_ONLINE = "NOT ONLINE"  # Пользователь не онлайн


class User:
    def __init__(self, user: dict):
        """
        :ru Информация о полях из раздела 'User'.
        :en Information about fields from the 'User' section.

        :param user:ru Json объект полученный от 'Вконтакте'.
        :param user:en Json object received from 'Vkontakte'.
        :type user: Dict[str, Any]
        """
        self.__user = user

# ========================== Базовая информация ========================== Basic information ==========================
    @property
    def user_id(self) -> int:
        """
        :ru Свойство для получения идентификатора пользователя.
        :en Property for getting the user ID.
        """
        return self.__user['id'] if 'id' in self.__user else None

    @property
    def domain(self) -> str:
        """
        :ru Свойство для получения короткого адреса страницы. Возвращается строка, содержащая короткий адрес страницы
         (например, andrew). Если он не назначен, возвращается "id"+user_id, например, id35828305.
        :en Property for getting a short page address. A string containing the short address of the page is returned
         (for example, andrew). If it is not assigned, "id"+user_id is returned, for example, id35828305.
        """
        return self.__user['domain'] if 'domain' in self.__user else None

    @property
    def screen_name(self) -> str:
        """
        :ru Свойство для получения короткого имени страницы.
        :en Property for getting a short page name.
        """
        return self.__user['screen_name'] if 'screen_name' in self.__user else None

    @property
    def first_name(self) -> str:
        """
        :ru Свойство для получения имени пользователя.
        :en Property for getting the user name.
        """
        return self.__user['first_name'] if 'first_name' in self.__user else None

    @property
    def last_name(self) -> str:
        """
        :ru Свойство для получения фамилии пользователя.
        :en Property for getting the user's last name.
        """
        return self.__user['last_name'] if 'last_name' in self.__user else None

    @property
    def birthday(self) -> str:
        """
        :ru Свойство для получения даты рождения пользователя, в формате ГГГГ-ММ-ДД.
        :en Property for getting the user's date of birth, in the format YYYY-MM-DD.
        """
        return self.__convert_birthdate(self.__user['bdate']) if 'bdate' in self.__user else None

    @property
    def sex(self) -> Sex:
        """
        :ru Свойство для получения пола пользоватедя. Подробнее см. 'person_enum.Sex'.
        :en Property for getting the user's gender. For more information, see 'person_enum.Sex'.
        """
        return self.__decode_sex(self.__user['sex']) if 'sex' in self.__user else None

    @property
    def relation(self) -> Relation:
        """
        :ru Свойство для получения информация о семейном положении пользователя. Подробнее см. 'person_enum.Relation'.
        :en Property for getting information about the marital status of the user. For more information,
         see 'person_enum.Relation'.
        """
        return self.__decode_relation(self.__user['relation']) if 'relation' in self.__user else None

    @property
    def online(self) -> Online:
        """
        :ru Свойство для получения информация о том, находится ли пользователь сейчас на сайте.
        :en Property for getting information about whether the user is currently on the site.
        """
        return self.__decode_online(self.__user['online']) if 'online' in self.__user else None

    @property
    def count(self) -> Optional[Counters]:
        """
        :ru Свойство для получения информации количестве различных объектов у пользователя.
        :en Property for getting information about the number of different objects from the user.
        """
        if 'counters' in self.__user:
            return Counters(counters=self.__user['counters'])
        return None

    @property
    def occupation(self) -> Optional[Occupation]:
        """
        :ru Свойство для получения информации о деятельности пользователя.
        :en Property for getting information about user activity.
        """
        if 'occupation' in self.__user:
            return Occupation(occupation=self.__user['occupation'])
        return None

    @property
    def contacts(self) -> Optional[Contacts]:
        """
        :ru Свойство для получения информации о контактной информации пользователя
        :ru Property for getting information about the user's contact information
        """
        return Contacts(contacts=self.__user)

    @property
    def interests(self) -> Optional[Interests]:
        """
        :ru Свойство для получения информации о полях из раздела «Жизненная позиция».
        :en Property for getting information about fields from the "Life position" section.
        """
        return Interests(interests=self.__user)

    @property
    def education(self) -> Optional[Education]:
        """
        :ru Свойство для получения образовательных учереждений, в которых обучался пользователь.
        :en Property for obtaining educational institutions in which the user studied.
        """
        if 'schools' in self.__user or 'universities' in self.__user:
            return Education(education=self.__user)
        return None

    @property
    def career(self) -> Optional[List[Career]]:
        """
        :ru Свойство для получения списка школ, в которых учился пользователь. Массив экземпляров класса 'University'.
        :en Property for getting a list of schools where the user studied. Array of instances of the 'School' class.
        """
        if 'career' in self.__user:
            return [Career(career=career) for career in self.__user['career']]
        return None

    @property
    def military(self) -> Optional[List[Military]]:
        """
        :ru Свойство для получения информации о военной службе пользователя.
        :en Property for getting information about the user's military service.
        """
        if 'military' in self.__user:
            return [Military(military=military) for military in self.__user['military']]
        return None

    @property
    def life_position(self) -> Optional[LifePosition]:
        """
        :ru Свойство для получения информации о полях из раздела «Жизненная позиция».
        :en Property for getting information about fields from the "Life position" section.
        """
        if 'personal' in self.__user:
            return LifePosition(personal=self.__user['personal'])
        return None

    @property
    def params(self) -> Optional[Params]:
        """
        :ru Свойство для получения информации о дополнительных полях пользователя.
        :en Property for getting information about additional user fields.
        """
        return Params(params=self.__user)

    def get_json(self, is_full: bool = False) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'User'.
        :en This method generates a json object from the fields of the 'User' class.
        """
        if self.education.schools is not None:
            schools_id =[school.json() if is_full else school.id for school in self.education.schools]
        else:
            schools_id = self.education.schools
        if self.education.universities is not None:
            uni_id = [university.json() if is_full else university.id for university in self.education.universities]
        else:
            uni_id = self.education.universities
        if self.career is not None:
            for career in self.career:
                if is_full:
                    user_career = career.json()
                else:
                    user_career = career.company if career.company is not None else career.group_id
        else:
            user_career = self.career
        if self.military is not None:
            military = [military.json() if is_full else military.unit_id for military in self.military]
        else:
            military = self.military
        main_info = {"id": self.user_id,
                     "domain": self.domain,
                     "screen_name": self.screen_name,
                     "first_name": self.first_name,
                     "last_name": self.last_name,
                     "birthday": self.birthday,
                     "sex": self.sex.name,
                     "relation": self.relation.name,
                     "online": self.online.name}

        count = self.count.get_json()
        occupation = self.occupation.get_json()
        contacts = self.contacts.get_json() if is_full else {"city_id": self.contacts.city_id,
                                                             "country_id": self.contacts.country_id}
        interests = self.interests.get_json()
        activities = {"schools_id": schools_id,
                      "universities_id": uni_id,
                      "career": user_career,
                      "military": military}
        life_position = self.life_position.get_json()
        params = self.params.get_json()
        return {**main_info,
                **count,
                **occupation,
                **contacts,
                **interests,
                **activities,
                **life_position,
                **params}

    @staticmethod
    def __convert_birthdate(birthdate: str) -> str:
        date = str(birthdate).split(".")
        if len(date) == 3:
            return str(date[2]) + "-" + str(date[1]) + "-" + str(date[0])
        elif len(date) == 2:
            return "0000" + "-" + str(date[1]) + "-" + str(date[0])
        else:
            return "0000-00-00"

    @staticmethod
    def __decode_sex(sex: int) -> Sex:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'sex' в Enum 'Sex'.
        :en This private method converts the numeric representation of the value 'sex' to Enum 'Sex'.

        :param sex:ru Числовое представление значения 'sex'.
        :param sex:en Numeric representation of the 'sex' value.
        :type sex: int
        """
        if sex == 0:
            return Sex.NOT_SPECIFIED  # Пол не указан
        elif sex == 1:
            return Sex.FEMALE  # Женщина
        elif sex == 2:
            return Sex.MALE  # Мужщина
        else:
            raise Exception(f"Invalid value '{sex}' for Enum 'Sex'!")

    @staticmethod
    def __decode_online(online: int) -> Online:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'online' в Enum 'Online'.
        :en This private method converts the numeric representation of the value 'online' to Enum 'Online'.

        :param online:ru Числовое представление значения 'encoded_sex'.
        :param online:en Numeric representation of the 'encoded_sex' value.
        :type online: int
        """
        if online == 0:
            return Online.NOT_ONLINE
        elif online == 1:
            return Online.ONLINE
        else:
            raise Exception(f"Invalid value '{online}' for Enum 'Online'!")

    @staticmethod
    def __decode_relation(relation: int) -> Relation:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'relation' в Enum 'Relation'.
        :en This private method converts the numeric representation of the value 'relation' to Enum 'Relation'.

        :param relation:ru Числовое представление значения 'relation'.
        :param relation:en Numeric representation of the 'relation' value.
        :type relation: int
        """
        if relation == 0:
            return Relation.NOT_SPECIFIED
        elif relation == 1:
            return Relation.NOT_MARRIED
        elif relation == 2:
            return Relation.HAVE_FRIEND
        elif relation == 3:
            return Relation.ENGAGED
        elif relation == 4:
            return Relation.EVERYTHING_IS_COMPLICATED
        elif relation == 5:
            return Relation.ACTIVE_SEARCH
        elif relation == 6:
            return Relation.IN_LOVE
        elif relation == 7:
            return Relation.CIVIL_MARRIAGE
        else:
            raise Exception(f"Invalid value '{relation}' for Enum 'Relation'!")

