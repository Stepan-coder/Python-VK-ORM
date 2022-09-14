"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import json
from enum import Enum
from quanario.user.last_seen import *
from typing import Dict, Any, List, Optional


class Params:
    def __init__(self, params: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Params'.
        :en Information about fields from the 'Params' section.

        :param params:ru Json объект полученный от 'Вконтакте'.
        :param params:en Json object received from 'Vkontakte'.
        :type params: Dict[str, Any]
        """
        self.__params = params

    @property
    def can_access_closed(self) -> bool:
        """
        :ru Свойство для получения информации о возможности пользователя видеть профиль при is_closed = 1
         (например, он есть в друзьях).
        :en Property for getting information about the user's ability to see the profile when is_closed = 1
         (for example, he is in friends).
        """
        return self.__params['can_access_closed'] if 'can_access_closed' in self.__params else None

    @property
    def is_closed(self) -> bool:
        """
        :ru Свойство для получения информации о том, скрыт ли профиль пользователя настройками приватности.
        :en Property for getting information about whether the user's profile is hidden by privacy settings.
        """
        return self.__params['is_closed'] if 'is_closed' in self.__params else None

    @property
    def has_mobile(self) -> bool:
        """
        :ru Свойство для получения информации о том, известен ли номер мобильного телефона пользователя.
        :en Property for getting information about whether the user's mobile phone number is known.
        """
        return self.__params['has_mobile'] == 1 if 'has_mobile' in self.__params else None

    @property
    def has_photo(self) -> bool:
        """
        :ru Свойство для получения информации о том, установил ли пользователь фотографию для профиля.
        :en Property for getting information about whether the user has set a profile photo.
        """
        return self.__params['has_photo'] == 1 if 'has_photo' in self.__params else None

    @property
    def is_no_index(self) -> bool:
        """
        :ru Свойство для получения информации о том, индексируется ли профиль поисковыми сайтами.
        :en Property for getting information about whether the profile is indexed by search sites.
        """
        return self.__params['is_no_index'] == 0 if 'is_no_index' in self.__params else None

    @property
    def is_trending(self) -> bool:
        """
        :ru Свойство для получения информации о том, индексируется ли профиль поисковыми сайтами.
        :en Property for getting information about whether the profile is indexed by search sites.
        """
        return self.__params['trending'] == 1 if 'trending' in self.__params else None

    @property
    def is_verified(self) -> bool:
        """
        :ru Свойство для получения информации о том, верифицирована ли страница пользователя.
        :en Property for getting information about whether the user's page has been verified.
        """
        return self.__params['verified'] == 1 if 'verified' in self.__params else None

    @property
    def is_wall_privat(self) -> bool:
        """
        :ru Свойство для получения информации о том, открыта ли страница пользователя.
        :en Property for getting information about whether the user's page is open.
        """
        return self.__params['wall_default'] == 'owner' if 'wall_default' in self.__params else None

    @property
    def timezone(self) -> str:
        """
        :ru Свойство для получения информации о временной зоне пользователя.
        :en Property for getting information about the user's time zone.
        """
        return self.__params['timezone'] if 'timezone' in self.__params else None

    @property
    def last_seen(self) -> Optional[LastSeen]:
        """
        :ru Свойство для получения информации о последнем посещении пользователя.
        :en Property for getting information about the user's last visit.
        """
        if 'last_seen' in self.__params:
            return LastSeen(last_seen=self.__params['last_seen'])
        return None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'Params'.
        :en This method generates a json object from the fields of the 'Params' class.
        """
        return {"can_access_closed": self.can_access_closed,
                "is_closed": self.is_closed,
                "has_mobile": self.has_mobile,
                "has_photo": self.has_photo,
                "is_no_index": self.is_no_index,
                "trending": self.is_trending,
                "verified": self.is_verified,
                "wall_default": self.is_wall_privat,
                "timezone": self.timezone,
                "last_seen_time": self.last_seen.time.strftime('%Y-%m-%d %H:%M:%S'),
                "last_seen_platform": self.last_seen.platform.name}