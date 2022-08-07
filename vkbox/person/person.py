from vkbox.person.person_enum import *


"""
career, connections, counters, education
last_seen, military, occupation, personal, schools,
site, universities
"""


class Person:
    def __init__(self, person_json: dict):
        self.__person_json = person_json

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения идентификатора пользователя.
        :en Property for getting the user ID.
        """
        return self.__person_json['id'] if 'id' in self.__person_json else None

    @property
    def domain(self) -> str:
        """
        :ru Свойство для получения короткого адреса страницы. Возвращается строка, содержащая короткий адрес страницы
         (например, andrew). Если он не назначен, возвращается "id"+user_id, например, id35828305.
        :en Property for getting a short page address. A string containing the short address of the page is returned
         (for example, andrew). If it is not assigned, "id"+user_id is returned, for example, id35828305.
        """
        return self.__person_json['domain'] if 'domain' in self.__person_json else None

    @property
    def screen_name(self) -> str:
        """
        :ru Свойство для получения короткого имени страницы.
        :en Property for getting a short page name.
        """
        return self.__person_json['screen_name'] if 'screen_name' in self.__person_json else None

    @property
    def first_name(self) -> str:
        """
        :ru Свойство для получения имени пользователя.
        :en Property for getting the user name.
        """
        return self.__person_json['first_name'] if 'first_name' in self.__person_json else None

    @property
    def last_name(self) -> str:
        """
        :ru Свойство для получения фамилии пользователя.
        :en Property for getting the user's last name.
        """
        return self.__person_json['last_name'] if 'last_name' in self.__person_json else None

    @property
    def birthday(self) -> str:
        """
        :ru Свойство для получения даты рождения пользователя, в формате ГГГГ-ММ-ДД.
        :en Property for getting the user's date of birth, in the format YYYY-MM-DD.
        """
        return self.__convert_birthdate(self.__person_json['bdate']) if 'bdate' in self.__person_json else None

    @property
    def sex(self) -> SEX:
        """
        :ru Свойство для получения пола пользоватедя. Подробнее см. 'person_enum.SEX'.
        :en Property for getting the user's gender. For more information, see 'person_enum.SEX'.
        """
        return self.__decode_sex(self.__person_json['sex']) if 'sex' in self.__person_json else None

    @property
    def timezone(self) -> str:
        """
        :ru Свойство для получения информации о временной зоне пользователя.
        :en Property for getting information about the user's time zone.
        """
        return self.__person_json['timezone'] if 'timezone' in self.__person_json else None

    @property
    def home_town(self) -> str:
        """
        :ru Свойство для получения названия родного города.
        :en Property for getting the name of the hometown.
        """
        return self.__person_json['home_town'] if 'home_town' in self.__person_json else None



    @property
    def about(self) -> str:
        """
        :ru Свойство для получения содержимого поля «О себе» из профиля.
        :en Property for getting the contents of the "About me" field from the profile.
        """
        return self.__person_json['about'] if 'about' in self.__person_json else None

    @property
    def status(self) -> str:
        """
        :ru Свойство для получения статуса пользователя. Возвращается строка, содержащая текст статуса, расположенного в
         профиле под именем.
        :en Property for getting user status. Returns a string containing the status text located in profile under the
         name.
        """
        return self.__person_json['status'] if 'status' in self.__person_json else None

    @property
    def activities(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Деятельность» из профиля.
        :en Property for getting the contents of the "Activity" field from the profile.
        """
        return self.__person_json['activities'] if 'activities' in self.__person_json else None

    @property
    def interests(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Деятельность» из профиля.
        :en Property for getting the contents of the "Activity" field from the profile.
        """
        return self.__person_json['interests'] if 'interests' in self.__person_json else None

    @property
    def music(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимая музыка» из профиля.
        :en Property for getting the contents of the "Favorite music" field from the profile.
        """
        return self.__person_json['music'] if 'music' in self.__person_json else None

    @property
    def movies(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые фильмы» из профиля.
        :en Property for getting the contents of the "Favorite movies" field from the profile.
        """
        return self.__person_json['movies'] if 'movies' in self.__person_json else None

    @property
    def tv(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые телешоу» из профиля.
        :en Property for getting the contents of the "Favorite TV shows" field from the profile.
        """
        return self.__person_json['tv'] if 'tv' in self.__person_json else None

    @property
    def books(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые книги» из профиля.
        :en Property for getting the contents of the "Favorite books" field from the profile.
        """
        return self.__person_json['books'] if 'books' in self.__person_json else None

    @property
    def games(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые игры» из профиля.
        :en Property for getting the contents of the "Favorite games" field from the profile.
        """
        return self.__person_json['games'] if 'games' in self.__person_json else None

    @property
    def quotes(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые цитаты» из профиля.
        :en Property for getting the contents of the "Favorite quotes" field from the profile.
        """
        return self.__person_json['quotes'] if 'quotes' in self.__person_json else None


    @property
    def followers_count(self) -> int:
        return self.__person_json['followers_count'] if 'followers_count' in self.__person_json else None



    @property
    def online(self) -> ONLINE:
        """
        :ru Свойство для получения информация о том, находится ли пользователь сейчас на сайте.
        :en Property for getting information about whether the user is currently on the site.
        """
        return self.__decode_online(self.__person_json['online']) if 'online' in self.__person_json else None




    @property
    def relation(self) -> RELATION:
        """
        :ru Свойство для получения информация о семейном положении пользователя. Подробнее см. 'person_enum.RELATION'.
        :en Property for getting information about the marital status of the user. For more information,
         see 'person_enum.RELATION'.
        """
        return self.__decode_relation(self.__person_json['relation']) if 'relation' in self.__person_json else None


    @property
    def city_id(self) -> int:
        """
        :ru Свойство для получения идентификатора города пользователя, который можно использовать для получения его
         названия с помощью метода 'database.getCitiesById'.
        :en Property for getting the user's city ID, which can be used to get it names using the
         'database' method.getCitiesById'.
        """
        return self.__person_json['city']['id'] if 'city' in self.__person_json else None

    @property
    def city_title(self) -> str:
        """
        :ru Свойство для получения названия города в котором находится пользователь.
        :en Property for getting the name of the city where the user is located.
        """
        return self.__person_json['city']['title'] if 'city' in self.__person_json else None

    @property
    def country_id(self) -> int:
        """
        :ru Свойство для получения идентификатора страны пользователя, который можно использовать для получения его
         названия с помощью метода database.getCitiesById.
        :en Property for getting the user's country ID, which can be used to get it names using the
         database method.getCitiesById.
        """
        return self.__person_json['country']['id'] if 'country' in self.__person_json else None

    @property
    def country_title(self) -> str:
        """
        :ru Свойство для получения названия страны в которой находится пользователь.
        :en Property for getting the name of the country in which the user is located.
        """
        return self.__person_json['country']['title'] if 'country' in self.__person_json else None



    @property
    def can_access_closed(self) -> bool:
        """
        :ru Свойство для получения информации о возможности пользователя видеть профиль при is_closed = 1
         (например, он есть в друзьях).
        :en Property for getting information about the user's ability to see the profile when is_closed = 1
         (for example, he is in friends).
        """
        return self.__person_json['can_access_closed'] if 'can_access_closed' in self.__person_json else None

    @property
    def is_closed(self) -> bool:
        """
        :ru Свойство для получения информации о том, скрыт ли профиль пользователя настройками приватности.
        :en Property for getting information about whether the user's profile is hidden by privacy settings.
        """
        return self.__person_json['is_closed'] if 'is_closed' in self.__person_json else None

    @property
    def has_mobile(self) -> bool:
        """
        :ru Свойство для получения информации о том, известен ли номер мобильного телефона пользователя.
        :en Property for getting information about whether the user's mobile phone number is known.
        """
        return self.__person_json['has_mobile'] == 1 if 'has_mobile' in self.__person_json else None

    @property
    def has_photo(self) -> bool:
        """
        :ru Свойство для получения информации о том, установил ли пользователь фотографию для профиля.
        :en Property for getting information about whether the user has set a profile photo.
        """
        return self.__person_json['has_photo'] == 1 if 'has_photo' in self.__person_json else None

    @property
    def is_no_index(self) -> bool:
        """
        :ru Свойство для получения информации о том, индексируется ли профиль поисковыми сайтами.
        :en Property for getting information about whether the profile is indexed by search sites.
        """
        return self.__person_json['is_no_index'] == 0 if 'is_no_index' in self.__person_json else None

    @property
    def is_trending(self) -> bool:
        """
        :ru Свойство для получения информации о том, индексируется ли профиль поисковыми сайтами.
        :en Property for getting information about whether the profile is indexed by search sites.
        """
        return self.__person_json['trending'] == 1 if 'trending' in self.__person_json else None

    @property
    def is_verified(self) -> bool:
        """
        :ru Свойство для получения информации о том, верифицирована ли страница пользователя.
        :en Property for getting information about whether the user's page has been verified.
        """
        return self.__person_json['verified'] == 1 if 'verified' in self.__person_json else None

    @property
    def is_wall_privat(self) -> bool:
        """
        :ru Свойство для получения информации о том, открыта ли страница пользователя.
        :en Property for getting information about whether the user's page is open.
        """
        return self.__person_json['wall_default'] == 'owner' if 'wall_default' in self.__person_json else None


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
    def __decode_sex(encoded_sex: int) -> SEX:
        if encoded_sex == 0:
            return SEX.NOT_SPECIFIED
        elif encoded_sex == 1:
            return SEX.FEMALE
        elif encoded_sex == 2:
            return SEX.MALE
        else:
            raise Exception("Invalid value!")

    @staticmethod
    def __decode_online(encoded_online: int) -> ONLINE:
        if encoded_online == 0:
            return ONLINE.NOT_ONLINE
        elif encoded_online == 1:
            return ONLINE.ONLINE
        else:
            raise Exception("Invalid value!")

    @staticmethod
    def __decode_relation(encoded_relation: int) -> RELATION:
        if encoded_relation == 0:
            return RELATION.NOT_SPECIFIED
        elif encoded_relation == 1:
            return RELATION.NOT_MARRIED
        elif encoded_relation == 2:
            return RELATION.HAVE_FRIEND
        elif encoded_relation == 3:
            return RELATION.ENGAGED
        elif encoded_relation == 4:
            return RELATION.EVERYTHING_IS_COMPLICATED
        elif encoded_relation == 5:
            return RELATION.ACTIVE_SEARCH
        elif encoded_relation == 6:
            return RELATION.IN_LOVE
        elif encoded_relation == 7:
            return RELATION.CIVIL_MARRIAGE
        else:
            raise Exception("Invalid value!")

