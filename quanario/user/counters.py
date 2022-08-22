import json
from enum import Enum
from typing import Dict, Any


class Counters:
    def __init__(self, counters: Dict[str, Any]):
        """
        :ru Количество различных объектов у пользователя.
        :en Information about fields from the 'Military' section.

        :param counters:ru Json объект полученный от 'Вконтакте'.
        :param counters:en Json object received from 'Vkontakte'.
        :type counters: Dict[str, Any]
        """
        self.__counters = counters

    @property
    def notes(self) -> int:
        """
        :ru Свойство для получения количества заметок у пользователя.
        :en Property for getting the number of notes from the user.
        """
        return self.__counters['notes'] if 'notes' in self.__counters else None

    @property
    def pages(self) -> int:
        """
        :ru Свойство для получения количества подписчиков у пользователя.
        :en Property for getting the number of subscribers from the user.
        """
        return self.__counters['pages'] if 'pages' in self.__counters else None

    @property
    def audios(self) -> int:
        """
        :ru Свойство для получения количества аудиозаписей у пользователя.
        :en Property for getting the number of audio recordings from the user.
        """
        return self.__counters['audios'] if 'audios' in self.__counters else None

    @property
    def albums(self) -> int:
        """
        :ru Свойство для получения количества фотоальбомов у пользователя.
        :en Property for getting the number of photo albums from the user.
        """
        return self.__counters['albums'] if 'albums' in self.__counters else None

    @property
    def photos(self) -> int:
        """
        :ru Свойство для получения количества фотографий у пользователя.
        :en Property for getting the number of photos from the user.
        """
        return self.__counters['photos'] if 'photos' in self.__counters else None

    @property
    def videos(self) -> int:
        """
        :ru Свойство для получения количества видеозаписей у пользователя.
        :en Property for getting the number of videos from the user.
        """
        return self.__counters['videos'] if 'videos' in self.__counters else None

    @property
    def user_videos(self) -> int:
        """
        :ru Свойство для получения количества видеозаписей с пользователем.
        :en Property for getting the number of videos with the user.
        """
        return self.__counters['user_videos'] if 'user_videos' in self.__counters else None

    @property
    def clips_followers(self) -> int:
        """
        :ru Свойство для получения количества клипов с пользователем.
        :en Property for getting the number of clips with the user.
        """
        return self.__counters['clips_followers'] if 'clips_followers' in self.__counters else None

    @property
    def groups(self) -> int:
        """
        :ru Свойство для получения количества подписчиков сообществ у пользователя.
        :ru Property for getting the number of community subscribers from the user.
        """
        return self.__counters['groups'] if 'groups' in self.__counters else None

    @property
    def friends(self) -> int:
        """
        :ru Свойство для получения количества друзей у пользователя.
        :en Property for getting the number of friends a user has.
        """
        return self.__counters['friends'] if 'friends' in self.__counters else None

    @property
    def followers(self) -> int:
        """
        :ru Свойство для получения количества подписчиков у пользователя.
        :en Property for getting the number of subscribers from the user.
        """
        return self.__counters['followers'] if 'followers' in self.__counters else None

    @property
    def subscriptions(self) -> int:
        """
        :ru Свойство для получения количества подписок у пользователя.
        :en Property for getting the number of subscriptions from the user.
        """
        return self.__counters['subscriptions'] if 'subscriptions' in self.__counters else None

    @property
    def online_friends(self) -> int:
        """
        :ru Свойство для получения количества друзей онлайн пользователя.
        :ru Property for getting the number of online friends of the user.
        """
        return self.__counters['online_friends'] if 'online_friends' in self.__counters else None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'Counters'.
        :en This method generates a json object from the fields of the 'Counters' class.
        """
        return {"notes": self.notes,
                "pages": self.pages,
                "audios": self.audios,
                "albums": self.albums,
                "photos": self.photos,
                "videos": self.videos,
                "user_videos": self.user_videos,
                "clips_followers": self.clips_followers,
                "groups": self.groups,
                "friends": self.friends,
                "followers": self.followers,
                "subscriptions": self.subscriptions,
                "online_friends": self.online_friends}
