"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import json
from enum import Enum
from typing import Dict, List, Any


class Political(Enum):
    COMMUNIST = "COMMUNIST"  # Коммунистические
    SOCIALIST = "SOCIALIST"  # Социалистические
    MODERATE = "MODERATE"  # Умеренные
    LIBERAL = "LIBERAL"  # Либеральные
    CONSERVATIVE = "CONSERVATIVE"  # Консервативные
    MONARCHICAL = "MONARCHICAL"  # Монархические
    ULTRACONSERVATIVE = "ULTRACONSERVATIVE"  # Ультраконсервативные
    INDIFFERENT = "INDIFFERENT"  # Индифферентные
    LIBERTARIAN = "LIBERTARIAN"  # Либертарианские


class PeopleMain(Enum):
    INTELLIGENCE_AND_CREATIVITY = "INTELLIGENCE_AND_CREATIVITY"  # Ум и креативность
    KINDNESS_AND_HONESTY = "KINDNESS_AND_HONESTY"  # Доброта и честность
    BEAUTY_AND_HEALTH = "BEAUTY_AND_HEALTH"  # Красота и здоровье
    POWER_AND_WEALTH = "POWER_AND_WEALTH"  # Власть и богатство
    COURAGE_AND_PERSEVERANCE = "COURAGE_AND_PERSEVERANCE"  # Смелость и упорство
    HUMOR_AND_LOVE_OF_LIFE = "HUMOR_AND_LOVE_OF_LIFE"  # Юмор и жизнелюбие


class LifeMain(Enum):
    FAMILY_AND_CHILDREN = "FAMILY_AND_CHILDREN"  # Семья и дети
    CAREER_AND_MONEY = "CAREER_AND_MONEY"  # Карьера и деньги
    ENTERTAINMENT_AND_RECREATION = "ENTERTAINMENT_AND_RECREATION"  # Развлечения и отдых
    SCIENCE_AND_RESEARCH = "SCIENCE_AND_RESEARCH"  # Наука и исследования
    IMPROVING_THE_WORLD = "IMPROVING_THE_WORLD"  # Совершенствование мира
    SELF_DEVELOPMENT = "SELF_DEVELOPMENT"  # Саморазвитие
    BEAUTY_AND_ART = "BEAUTY_AND_ART"  # Красота и искусство
    FAME_AND_INFLUENCE = "FAME_AND_INFLUENCE"  # Слава и влияние


class Position(Enum):
    SHARPLY_NEGATIVE = "SHARPLY_NEGATIVE"  # резко негативное
    NEGATIVE = "NEGATIVE"  # негативное
    COMPROMISE = "COMPROMISE"  # компромиссное
    NEUTRAL = "NEUTRAL"  # нейтральное
    POSITIVE = "POSITIVE"  # положительное


class LifePosition:
    def __init__(self, personal: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Жизненная позиция'.
        :en Information about fields from the 'Life position' section.

        :param personal:ru Json объект полученный от 'Вконтакте'.
        :param personal:en Json object received from 'Vkontakte'.
        :type personal: Dict[str, Any]
        """
        self.__personal = personal

    @property
    def political(self) -> Political:
        """
        :ru Свойство для получения информации из поля 'Политические предпочтения'.
        :en Property for getting information from the 'Political Preferences' field.
        """
        return self.__convert_political(self.__personal['political']) if 'political' in self.__personal else None

    @property
    def langs(self) -> List[str]:
        """
        :ru Свойство для получения информации из поля 'Языки'.
        :en Property for getting information from the 'Political Preferences' field.
        """
        return self.__personal['langs'] if 'langs' in self.__personal else None

    @property
    def religion(self) -> str:
        """
        :ru Свойство для получения информации из поля 'Мировоззрение'.
        :en Property for getting information from the 'Worldview' field.
        """
        return self.__personal['religion'] if 'religion' in self.__personal else None

    @property
    def inspired_by(self) -> str:
        """
        :ru Свойство для получения информации из поля 'Источники вдохновения'.
        :en Property for getting information from the field 'Sources of inspiration'.
        """
        return self.__personal['inspired_by'] if 'inspired_by' in self.__personal else None

    @property
    def people_main(self) -> PeopleMain:
        """
        :ru Свойство для получения информации из поля 'Главное в людях'.
        :en Property for getting information from the field 'The main thing in people'.
        """
        return self.__convert_people_main(self.__personal['people_main']) if 'people_main' in self.__personal else None

    @property
    def life_main(self) -> LifeMain:
        """
        :ru Свойство для получения информации из поля 'Главное в жизни'.
        :en Property for getting information from the 'Main thing in life' field.
        """
        return self.__convert_life_main(self.__personal['life_main']) if 'life_main' in self.__personal else None

    @property
    def smoking(self) -> Position:
        """
        :ru Свойство для получения информации из поля 'Отношение к курению'.
        :en Property for getting information from the 'Smoking Attitude' field.
        """
        return self.__convert_position(self.__personal['smoking']) if 'smoking' in self.__personal else None

    @property
    def alcohol(self) -> Position:
        """
        :ru Свойство для получения информации из поля 'Отношение к алкоголю'.
        :en Property for getting information from the 'Attitude to alcohol' field.
        """
        return self.__convert_position(self.__personal['alcohol']) if 'alcohol' in self.__personal else None

    def get_json(self) -> json:
        """
        :ru Этот метод формирует json объект из полей класса 'LifePosition'.
        :en This method generates a json object from the fields of the 'LifePosition' class.
        """
        return {"political": self.political.value,
                "langs": self.langs,
                "religion": self.religion,
                "inspired_by": self.inspired_by,
                "people_main": self.people_main.value,
                "life_main": self.life_main.value,
                "smoking": self.smoking.value,
                "alcohol": self.alcohol.value}

    @staticmethod
    def __convert_political(political: int) -> Political:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'political' в Enum 'Political'.
        :en This private method converts the numeric representation of the value 'political' to Enum 'Political'.

        :param political:ru Числовое представление значения 'political'.
        :param political:en Numeric representation of the 'political' value.
        :type political: int
        """
        if political == 1:
            return Political.COMMUNIST  # Коммунистические
        elif political == 2:
            return Political.SOCIALIST  # Социалистические
        elif political == 3:
            return Political.MODERATE  # Умеренные
        elif political == 4:
            return Political.LIBERAL  # Либеральные
        elif political == 5:
            return Political.CONSERVATIVE  # Консервативные
        elif political == 6:
            return Political.MONARCHICAL  # Монархические
        elif political == 7:
            return Political.ULTRACONSERVATIVE  # Ультраконсервативные
        elif political == 8:
            return Political.INDIFFERENT  # Индифферентные
        elif political == 9:
            return Political.LIBERTARIAN  # Либертарианские
        else:
            raise Exception("Invalid value!")

    @staticmethod
    def __convert_people_main(people_main: int) -> PeopleMain:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'people_main' в Enum 'PeopleMain'.
        :en This private method converts the numeric representation of the value 'people_main' to Enum 'PeopleMain'.

        :param people_main:ru Числовое представление значения 'people_main'.
        :param people_main:en Numeric representation of the 'people_main' value.
        :type people_main: int
        """
        if people_main == 1:
            return PeopleMain.INTELLIGENCE_AND_CREATIVITY  # Ум и креативность
        elif people_main == 2:
            return PeopleMain.KINDNESS_AND_HONESTY  # Доброта и честность
        elif people_main == 3:
            return PeopleMain.BEAUTY_AND_HEALTH  # Красота и здоровье
        elif people_main == 4:
            return PeopleMain.POWER_AND_WEALTH  # Власть и богатство
        elif people_main == 5:
            return PeopleMain.COURAGE_AND_PERSEVERANCE  # Смелость и упорство
        elif people_main == 6:
            return PeopleMain.HUMOR_AND_LOVE_OF_LIFE  # Юмор и жизнелюбие
        else:
            raise Exception("Invalid value!")

    @staticmethod
    def __convert_life_main(life_main: int) -> LifeMain:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'life_main' в Enum 'LifeMain'.
        :en This private method converts the numeric representation of the value 'life_main' to Enum 'LifeMain'.

        :param life_main:ru Числовое представление значения 'life_main'.
        :param life_main:en Numeric representation of the 'life_main' value.
        :type life_main: int
        """
        if life_main == 1:
            return LifeMain.FAMILY_AND_CHILDREN  # Семья и дети
        elif life_main == 2:
            return LifeMain.CAREER_AND_MONEY  # Карьера и деньги
        elif life_main == 3:
            return LifeMain.ENTERTAINMENT_AND_RECREATION  # Развлечения и отдых
        elif life_main == 4:
            return LifeMain.SCIENCE_AND_RESEARCH  # Наука и исследования
        elif life_main == 5:
            return LifeMain.IMPROVING_THE_WORLD  # Совершенствование мира
        elif life_main == 6:
            return LifeMain.SELF_DEVELOPMENT  # Саморазвитие
        elif life_main == 7:
            return LifeMain.BEAUTY_AND_ART  # Красота и искусство
        elif life_main == 8:
            return LifeMain.FAME_AND_INFLUENCE  # Слава и влияние
        else:
            raise Exception("Invalid value!")

    @staticmethod
    def __convert_position(position: int) -> Position:
        """
        :ru Этот приватный метод конвертирует числовое представление значения 'position' в Enum 'Position'.
        :en This private method converts the numeric representation of the value 'position' to Enum 'Position'.

        :param position:ru Числовое представление значения 'position'.
        :param position:en Numeric representation of the 'position' value.
        :type position: int
        """
        if position == 1:
            return Position.SHARPLY_NEGATIVE  # Резко негативное
        elif position == 2:
            return Position.NEGATIVE  # Негативное
        elif position == 3:
            return Position.COMPROMISE  # Компромисное
        elif position == 4:
            return Position.NEUTRAL  # Нейтральное
        elif position == 5:
            return Position.POSITIVE  # Положительное
        else:
            raise Exception("Invalid value!")
