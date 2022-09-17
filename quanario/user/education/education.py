"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


from .schools import *
from .universities import *
from typing import Dict, Any, List, Optional


class Education:
    def __init__(self, education: Dict[str, Any]):
        """
        :ru Информация о полях из раздела 'Образование'.
        :en Information about fields from the 'Education' section.

        :param education:ru Json объект полученный от 'Вконтакте'.
        :param education:en Json object received from 'Vkontakte'.
        :type education: Dict[str, Any]
        """
        self.__education = education

    @property
    def schools(self) -> Optional[List[School]]:
        """
        :ru Свойство для получения списка школ, в которых учился пользователь. Массив экземпляров класса 'University'.
        :en Property for getting a list of schools where the user studied. Array of instances of the 'School' class.
        """
        if 'schools' in self.__education:
            return [School(school=school) for school in self.__education['schools']]
        return None

    @property
    def universities(self) -> Optional[List[University]]:
        """
        :ru Свойство для получения списка вузов, в которых учился пользователь. Массив экземпляров класса 'University'.
        :en Property for getting a list of universities where the user studied.
         Array of instances of the 'University' class.
        """
        if 'universities' in self.__education:
            return [University(university=university) for university in self.__education['universities']]
        return None

