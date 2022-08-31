import json
from enum import Enum
from typing import Dict, Any


class Interests:
    def __init__(self, interests: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Interests'.
        :en Information about fields from the 'Interests' section.

        :param interests:ru Json объект полученный от 'Вконтакте'.
        :param interests:en Json object received from 'Vkontakte'.
        :type interests: Dict[str, Any]
        """
        self.__interests = interests

    @property
    def about(self) -> str:
        """
        :ru Свойство для получения содержимого поля «О себе» из профиля.
        :en Property for getting the contents of the "About me" field from the profile.
        """
        return self.__interests['about'] if 'about' in self.__interests else None

    @property
    def status(self) -> str:
        """
        :ru Свойство для получения статуса пользователя. Возвращается строка, содержащая текст статуса, расположенного в
         профиле под именем.
        :en Property for getting user status. Returns a string containing the status text located in profile under the
         name.
        """
        return self.__interests['status'] if 'status' in self.__interests else None

    @property
    def activities(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Деятельность» из профиля.
        :en Property for getting the contents of the "Activity" field from the profile.
        """
        return self.__interests['activities'] if 'activities' in self.__interests else None

    @property
    def interests(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Деятельность» из профиля.
        :en Property for getting the contents of the "Activity" field from the profile.
        """
        return self.__interests['interests'] if 'interests' in self.__interests else None

    @property
    def music(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимая музыка» из профиля.
        :en Property for getting the contents of the "Favorite music" field from the profile.
        """
        return self.__interests['music'] if 'music' in self.__interests else None

    @property
    def movies(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые фильмы» из профиля.
        :en Property for getting the contents of the "Favorite movies" field from the profile.
        """
        return self.__interests['movies'] if 'movies' in self.__interests else None

    @property
    def tv(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые телешоу» из профиля.
        :en Property for getting the contents of the "Favorite TV shows" field from the profile.
        """
        return self.__interests['tv'] if 'tv' in self.__interests else None

    @property
    def books(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые книги» из профиля.
        :en Property for getting the contents of the "Favorite books" field from the profile.
        """
        return self.__interests['books'] if 'books' in self.__interests else None

    @property
    def games(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые игры» из профиля.
        :en Property for getting the contents of the "Favorite games" field from the profile.
        """
        return self.__interests['games'] if 'games' in self.__interests else None

    @property
    def quotes(self) -> str:
        """
        :ru Свойство для получения содержимого поля «Любимые цитаты» из профиля.
        :en Property for getting the contents of the "Favorite quotes" field from the profile.
        """
        return self.__interests['quotes'] if 'quotes' in self.__interests else None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'Interests'.
        :en This method generates a json object from the fields of the 'Interests' class.
        """
        return {"about": self.about,
                "status": self.status,
                "activities": self.activities,
                "interests": self.interests,
                "music": self.music,
                "movies": self.movies,
                "tv": self.tv,
                "books": self.books,
                "games": self.games,
                "quotes": self.quotes}