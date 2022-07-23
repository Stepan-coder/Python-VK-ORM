from VKBOT.vk_types import *


class Person:
    def __init__(self, person_json: dict):
        self.__id = person_json['id'] if 'id' in person_json else None
        self.__domain = person_json['domain'] if 'domain' in person_json else None
        self.__first_name = person_json['first_name'] if 'first_name' in person_json else None
        self.__last_name = person_json['last_name'] if 'last_name' in person_json else None
        self.__about = person_json['about'] if 'about' in person_json else None
        self.__city_id = person_json['city']['id'] if 'city' in person_json else None
        self.__city_title = person_json['city']['title'] if 'city' in person_json else None
        self.__country_id = person_json['country']['id'] if 'country' in person_json else None
        self.__country_title = person_json['country']['title'] if 'country' in person_json else None
        self.__birthday = Person.__convert_birthdate(person_json['bdate']) if 'bdate' in person_json else None
        self.__sex = Person.__decode_sex(person_json['sex']) if 'sex' in person_json else None
        self.__online = Person.__decode_online(person_json['online']) if 'online' in person_json else None
        self.__relation = Person.__decode_relation(person_json['relation']) if 'relation' in person_json else None
        self.__can_access_closed = person_json['can_access_closed'] if 'can_access_closed' in person_json else None
        self.__is_closed = person_json['is_closed'] if 'is_closed' in person_json else None

    @property
    def id(self) -> int:
        return self.__id

    @property
    def domain(self) -> str:
        return self.__domain

    @property
    def online(self) -> ONLINE:
        return self.__online

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
    def relation(self) -> RELATION:
        return self.__relation

    @property
    def about(self) -> str:
        return self.__about

    @property
    def city_id(self) -> int:
        return self.__city_id

    @property
    def city_title(self) -> str:
        return self.__city_title

    @property
    def country_id(self) -> int:
        return self.__country_id

    @property
    def country_title(self) -> str:
        return self.__country_title

    @property
    def can_access_closed(self) -> bool:
        return self.__can_access_closed

    @property
    def is_closed(self) -> bool:
        return self.__is_closed

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

