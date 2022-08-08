from typing import Dict, Any, List, Optional

from vkbox.user.enum import *
from vkbox.user.career import *
from vkbox.user.schools import *
from vkbox.user.military import *
from vkbox.user.personal import *
from vkbox.user.universities import *

"""
counters, education
last_seen, occupation,
site
"""


class User:
    def __init__(self, user: dict):
        """
        :ru Информация о полях из раздела 'User'.
        :en Information about fields from the 'User' section.

        :param career:ru Json объект полученный от 'Вконтакте'.
        :param career:en Json object received from 'Vkontakte'.
        :type career: Dict[str, Any]
        """
        self.__user = user

# ========================== Базовая информация ========================== Basic information ==========================
    @property
    def id(self) -> int:
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
    def home_town(self) -> str:
        """
        :ru Свойство для получения названия родного города.
        :en Property for getting the name of the hometown.
        """
        return self.__user['home_town'] if 'home_town' in self.__user else None

    @property
    def city_id(self) -> int:
        """
        :ru Свойство для получения идентификатора города пользователя, который можно использовать для получения его
         названия с помощью метода 'database.getCitiesById'.
        :en Property for getting the user's city ID, which can be used to get it names using the
         'database' method.getCitiesById'.
        """
        return self.__user['city']['id'] if 'city' in self.__user else None

    @property
    def city_title(self) -> str:
        """
        :ru Свойство для получения названия города в котором находится пользователь.
        :en Property for getting the name of the city where the user is located.
        """
        return self.__user['city']['title'] if 'city' in self.__user else None

    @property
    def country_id(self) -> int:
        """
        :ru Свойство для получения идентификатора страны пользователя, который можно использовать для получения его
         названия с помощью метода database.getCitiesById.
        :en Property for getting the user's country ID, which can be used to get it names using the
         database method.getCitiesById.
        """
        return self.__user['country']['id'] if 'country' in self.__user else None

    @property
    def country_title(self) -> str:
        """
        :ru Свойство для получения названия страны в которой находится пользователь.
        :en Property for getting the name of the country in which the user is located.
        """
        return self.__user['country']['title'] if 'country' in self.__user else None

    @property
    def timezone(self) -> str:
        """
        :ru Свойство для получения информации о временной зоне пользователя.
        :en Property for getting information about the user's time zone.
        """
        return self.__user['timezone'] if 'timezone' in self.__user else None

# ============================== О пользователе ============================== About user ==============================
    @property
    def about(self) -> str:
        """
        :ru Свойство для получения содержимого поля «О себе» из профиля.
        :en Property for getting the contents of the "About me" field from the profile.
        """
        return self.__user['about'] if 'about' in self.__user else None

    @property
    def status(self) -> str:
        """
        :ru Свойство для получения статуса пользователя. Возвращается строка, содержащая текст статуса, расположенного в
         профиле под именем.
        :en Property for getting user status. Returns a string containing the status text located in profile under the
         name.
        """
        return self.__user['status'] if 'status' in self.__user else None

    @property
    def activities(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Деятельность» из профиля.
        :en Property for getting the contents of the "Activity" field from the profile.
        """
        return self.__user['activities'] if 'activities' in self.__user else None

    @property
    def interests(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Деятельность» из профиля.
        :en Property for getting the contents of the "Activity" field from the profile.
        """
        return self.__user['interests'] if 'interests' in self.__user else None

    @property
    def music(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимая музыка» из профиля.
        :en Property for getting the contents of the "Favorite music" field from the profile.
        """
        return self.__user['music'] if 'music' in self.__user else None

    @property
    def movies(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые фильмы» из профиля.
        :en Property for getting the contents of the "Favorite movies" field from the profile.
        """
        return self.__user['movies'] if 'movies' in self.__user else None

    @property
    def tv(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые телешоу» из профиля.
        :en Property for getting the contents of the "Favorite TV shows" field from the profile.
        """
        return self.__user['tv'] if 'tv' in self.__user else None

    @property
    def books(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые книги» из профиля.
        :en Property for getting the contents of the "Favorite books" field from the profile.
        """
        return self.__user['books'] if 'books' in self.__user else None

    @property
    def games(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые игры» из профиля.
        :en Property for getting the contents of the "Favorite games" field from the profile.
        """
        return self.__user['games'] if 'games' in self.__user else None

    @property
    def quotes(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые цитаты» из профиля.
        :en Property for getting the contents of the "Favorite quotes" field from the profile.
        """
        return self.__user['quotes'] if 'quotes' in self.__user else None


    @property
    def personal(self) -> Optional[Personal]:
        """
        :ru Свойство для получения списка школ, в которых учился пользователь. Массив экземпляров класса 'University'.
        :en Property for getting a list of schools where the user studied. Array of instances of the 'School' class.
        """
        if 'personal' in self.__user:
            return Personal(personal=self.__user['personal'])
        return None

    @property
    def schools(self) -> Optional[List[School]]:
        """
        :ru Свойство для получения списка школ, в которых учился пользователь. Массив экземпляров класса 'University'.
        :en Property for getting a list of schools where the user studied. Array of instances of the 'School' class.
        """
        if 'schools' in self.__user:
            return [School(school=school) for school in self.__user['schools']]
        return None

    @property
    def universities(self) -> Optional[List[University]]:
        """
        :ru Свойство для получения списка вузов, в которых учился пользователь. Массив экземпляров класса 'University'.
        :en Property for getting a list of universities where the user studied.
         Array of instances of the 'University' class.
        """
        if 'universities' in self.__user:
            return [University(university=university) for university in self.__user['universities']]
        return None

    @property
    def military(self) -> Optional[Military]:
        """
        :ru Свойство для получения информации о военной службе пользователя.
        :en Property for getting information about the user's military service.
        """
        if 'military' in self.__user:
            return Military(military=self.__user['military'])
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
    def followers_count(self) -> int:
        return self.__user['followers_count'] if 'followers_count' in self.__user else None

    @property
    def connections(self):
        return self.__user['connections'] if 'connections' in self.__user else None

    @property
    def online(self) -> Online:
        """
        :ru Свойство для получения информация о том, находится ли пользователь сейчас на сайте.
        :en Property for getting information about whether the user is currently on the site.
        """
        return self.__decode_online(self.__user['online']) if 'online' in self.__user else None




    @property
    def can_access_closed(self) -> bool:
        """
        :ru Свойство для получения информации о возможности пользователя видеть профиль при is_closed = 1
         (например, он есть в друзьях).
        :en Property for getting information about the user's ability to see the profile when is_closed = 1
         (for example, he is in friends).
        """
        return self.__user['can_access_closed'] if 'can_access_closed' in self.__user else None

    @property
    def is_closed(self) -> bool:
        """
        :ru Свойство для получения информации о том, скрыт ли профиль пользователя настройками приватности.
        :en Property for getting information about whether the user's profile is hidden by privacy settings.
        """
        return self.__user['is_closed'] if 'is_closed' in self.__user else None

    @property
    def has_mobile(self) -> bool:
        """
        :ru Свойство для получения информации о том, известен ли номер мобильного телефона пользователя.
        :en Property for getting information about whether the user's mobile phone number is known.
        """
        return self.__user['has_mobile'] == 1 if 'has_mobile' in self.__user else None

    @property
    def has_photo(self) -> bool:
        """
        :ru Свойство для получения информации о том, установил ли пользователь фотографию для профиля.
        :en Property for getting information about whether the user has set a profile photo.
        """
        return self.__user['has_photo'] == 1 if 'has_photo' in self.__user else None

    @property
    def is_no_index(self) -> bool:
        """
        :ru Свойство для получения информации о том, индексируется ли профиль поисковыми сайтами.
        :en Property for getting information about whether the profile is indexed by search sites.
        """
        return self.__user['is_no_index'] == 0 if 'is_no_index' in self.__user else None

    @property
    def is_trending(self) -> bool:
        """
        :ru Свойство для получения информации о том, индексируется ли профиль поисковыми сайтами.
        :en Property for getting information about whether the profile is indexed by search sites.
        """
        return self.__user['trending'] == 1 if 'trending' in self.__user else None

    @property
    def is_verified(self) -> bool:
        """
        :ru Свойство для получения информации о том, верифицирована ли страница пользователя.
        :en Property for getting information about whether the user's page has been verified.
        """
        return self.__user['verified'] == 1 if 'verified' in self.__user else None

    @property
    def is_wall_privat(self) -> bool:
        """
        :ru Свойство для получения информации о том, открыта ли страница пользователя.
        :en Property for getting information about whether the user's page is open.
        """
        return self.__user['wall_default'] == 'owner' if 'wall_default' in self.__user else None


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
            return Sex.NOT_SPECIFIED
        elif sex == 1:
            return Sex.FEMALE
        elif sex == 2:
            return Sex.MALE
        else:
            raise Exception("Invalid value!")

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
            return Online.Online
        else:
            raise Exception("Invalid value!")

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
            raise Exception("Invalid value!")

