import json
from enum import Enum
from typing import Dict, Any
from datetime import datetime


class Platform(Enum):
    MOBILE_SITE = "MOBILE_SITE"  # Мобильная версия
    IPHONE_APP = "IPHONE_APP"  # Приложение для iPhone
    IPAD_APP = "IPAD_APP"  # Приложение для iPad
    ANDROID_APP = "ANDROID_APP"  # Приложение для Android
    WINPHONE_APP = "WINPHONE_APP"  # Приложение для Windows Phone
    WINDOWS10_APP = "WINDOWS10_APP"  # Приложение для Windows 10
    FULL_SITE = "FULL_SITE"  # Полная версия сайта


class LastSeen:
    def __init__(self, last_seen: Dict[str, Any]):
        """
        :ru Время последнего посещения.
        :en The time of the last visit.

        :param last_seen:ru Json объект полученный от 'Вконтакте'.
        :param last_seen:en Json object received from 'Vkontakte'.
        :type last_seen: Dict[str, Any]
        """
        self.__last_seen = last_seen

    @property
    def time(self) -> datetime:
        """
        :ru Свойство для получения количества заметок у пользователя.
        :en Property for getting the number of notes from the user.
        """
        return datetime.utcfromtimestamp(self.__last_seen['time']) if 'time' in self.__last_seen else None

    @property
    def platform(self) -> Platform:
        """
        :ru Свойство для получения информации о том, с какого устройства пользователь заходил в последний раз.
        :en A property for getting information about which device the user last logged in from.
        """
        return self.__convert_platform(self.__last_seen['platform']) if 'platform' in self.__last_seen else None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'LastSeen'.
        :en This method generates a json object from the fields of the 'LastSeen' class.
        """
        return {"time": self.time.strftime('%Y-%m-%d %H:%M:%S'),
                "platform": self.platform.name}

    @staticmethod
    def __convert_platform(platform: int) -> Platform:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'platform' в Enum 'Platform'.
        :en This private method converts the numeric representation of the value 'platform' to Enum 'Platform'.

        :param platform:ru Числовое представление значения 'platform'.
        :param platform:en Numeric representation of the 'platform' value.
        :type platform: int
        """
        if platform == 1:
            return Platform.MOBILE_SITE  # Мобильная версия
        elif platform == 2:
            return Platform.IPHONE_APP  # Приложение для iPhone
        elif platform == 3:
            return Platform.IPAD_APP  # Приложение для iPad
        elif platform == 4:
            return Platform.ANDROID_APP  # Приложение для Android
        elif platform == 5:
            return Platform.WINPHONE_APP  # Приложение для Windows Phone
        elif platform == 6:
            return Platform.WINDOWS10_APP  # Приложение для Windows 10
        elif platform == 7:
            return Platform.FULL_SITE  # Полная версия сайта
        else:
            raise Exception(f"Invalid value '{platform}' for Enum 'Platform'!")
