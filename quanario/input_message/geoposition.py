import os
import urllib.request
from typing import Tuple


class Geo:
    def __init__(self, geo_position: dict):
        self.__geo_position = geo_position

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения уникального идентификатора метки на карте.
        :en Property for getting the unique identifier of the placemark on the map.
        """
        return self.__geo_position['id']

    @property
    def from_id(self) -> int:
        """
        :ru Свойство для получения уникального идентификатора пользователя, отправившего метку.
        :en Property for getting the unique identifier of the user who sent the tag.
        """
        return self.__geo_position['from_id']

    @property
    def date(self) -> int:
        """
        :ru Свойство для получения даты отправки геопозиции.
        :en Property for getting the date of sending the geo position.
        """
        return self.__geo_position['date']

    @property
    def out(self) -> int:
        return self.__geo_position['out']

    @property
    def latitude(self) -> float:
        """
        :ru Свойство для получения географической широты исходной точки, заданной в градусах.
        :en Property for getting the geographical latitude of the starting point, set in degrees.
        """
        return self.__geo_position['geo']['coordinates']['latitude']

    @property
    def longitude(self) -> float:
        """
        :ru Свойство для получения географической долготы исходной точки, заданной в градусах.
        :en Property for getting the geographical longitude of the starting point, set in degrees.
        """
        return self.__geo_position['geo']['coordinates']['longitude']

    @property
    def location_type(self) -> str:
        """
        :ru Свойство для получения типа отправленной пользователем метки.
        :en Property for getting the type of the label sent by the user.
        """
        return self.__geo_position['geo']['type']

    @property
    def title(self) -> str:
        """
        :ru Свойство для получения названия локации в виде строки.
        :en Property for getting the location name as a string.
        """
        return self.__geo_position['geo']['place']['title']

    @property
    def country(self) -> str:
        """
        :ru Свойство для получения страны, где расположена метка.
        :en Property for getting the country where the label is located.
        """
        return self.__geo_position['geo']['place']['country']

    @property
    def city(self) -> str:
        """
        :ru Свойство для получения города, где расположена метка.
        :en Property for getting the city where the label is located.
        """
        return self.__geo_position['geo']['place']['city']

