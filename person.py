from vk_types import *


class Person:
    def __init__(self, person_json: dict):
        print(person_json)
        self.__id = person_json['id'] if 'id' in person_json else None
        self.__domain = person_json['domain'] if 'domain' in person_json else None
        self.__first_name = person_json['first_name'] if 'first_name' in person_json else None
        self.__last_name = person_json['last_name'] if 'last_name' in person_json else None
        self.__birthday = person_json['birthday'] if 'birthday' in person_json else None
        self.__sex = Person.__decode_sex(person_json['sex']) if 'sex' in person_json else None
        self.__online = Person.__decode_online(person_json['online']) if 'online' in person_json else None
        self.__relation =
        self.__can_access_closed = person_json['can_access_closed'] if 'can_access_closed' in person_json else None
        self.__is_closed = person_json['is_closed'] if 'is_closed' in person_json else None

    @property
    def id(self) -> int:
        return self.__id

    @property
    def domain(self) -> str:
        return self.__domain

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def birthday(self) -> str:
        return self.__birthday

    @property
    def sex(self) -> SEX:
        return self.__sex

    @property
    def online(self) -> ONLINE:
        return self.__online

    @property
    def can_access_closed(self) -> bool:
        return self.__can_access_closed

    @property
    def is_closed(self) -> bool:
        return self.__is_closed

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

