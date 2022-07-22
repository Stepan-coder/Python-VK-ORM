import os
import urllib.request
from typing import Tuple


class GeoMessage:
    def __init__(self, geo_position: dict):
        self.__geo_position = geo_position

    @property
    def id(self) -> int:
        return self.__geo_position['id']

    @property
    def from_id(self) -> int:
        return self.__geo_position['from_id']

    @property
    def date(self) -> int:
        return self.__geo_position['date']

    @property
    def out(self) -> int:
        return self.__geo_position['out']

    @property
    def latitude(self) -> float:
        return self.__geo_position['geo']['coordinates']['latitude']

    @property
    def longitude(self) -> float:
        return self.__geo_position['geo']['coordinates']['longitude']

    @property
    def location_type(self) -> str:
        return self.__geo_position['geo']['type']

    @property
    def title(self) -> str:
        return self.__geo_position['geo']['place']['title']

    @property
    def country(self) -> str:
        return self.__geo_position['geo']['place']['country']

    @property
    def city(self) -> str:
        return self.__geo_position['geo']['place']['city']

