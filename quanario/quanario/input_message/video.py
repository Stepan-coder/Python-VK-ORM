"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import urllib.request
from typing import Tuple


class Video:
    def __init__(self, video: dict):
        self.__video = video

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения уникального идентификатор файла.
        :en Property for getting a unique file identifier.
        """
        return self.__video['id']

    @property
    def width(self) -> int:
        """
        :ru Свойство для получения ширины видео.
        :en Property for getting the width of the video.
        """
        return self.__video['width']

    @property
    def height(self) -> int:
        """
        :ru Свойство для получения высоты видео.
        :en Property for getting the height of the video.
        """
        return self.__video['height']

    @property
    def title(self) -> str:
        """
        :ru Свойство для получения полного названия файла.
        :en Property for getting the full name of the file.
        """
        return self.__video['title']

    @property
    def url(self) -> str:
        """
        :ru Свойство для получения ссылки для скачивания файла.
        :en Property for getting a link to download a file.
        """
        return self.__video['url']

    @property
    def date(self) -> int:
        """
        :ru Свойство для получения даты загрузки файла на сервер `ВКонтакте` (в формате Unix).
        :en Property for getting the file upload date to the `VKontakte` server (in Unix format).
        """
        return self.__video['date']

    @property
    def description(self) -> str:
        """
        :ru Свойство для получения описания видео.
        :en Property for getting a description of the video.
        """
        return self.__video['description']

    @property
    def duration(self) -> int:
        """
        :ru Свойство для получения длительности видео.
        :en Property for getting the duration of an video.
        """
        return self.__video['duration']

    @property
    def views(self) -> int:
        """
        :ru Свойство для получения количества просмотров видеозаписи.
        :en Property for getting the number of views of a video recording.
        """
        return self.__video['views']

    @property
    def can_edit(self) -> int:
        """
        :ru Свойство для получения количества просмотров видеозаписи.
        :en Property for getting the number of views of a video recording.
        """
        return self.__video['can_edit']

    @property
    def can_add(self) -> int:
        """
        :ru Свойство для получения информации может ли пользователь видеозапись к себе.
        :en Property for getting information whether the user can record a video to himself.
        """
        return self.__video['can_add']

    @property
    def can_attach_link(self) -> int:
        """
        :ru Свойство для получения информации может ли пользователь прикрепить кнопку действия к видео.
        :en Property for getting information whether a user can attach an action button to a video.
        """
        return self.__video['can_attach_link']

    @property
    def comments(self) -> int:
        """
        :ru Свойство для получения количества комментариев к видеозаписи.
        :en Property for getting the number of comments on the video.
        """
        return self.__video['comments']

    @property
    def is_favorite(self) -> bool:
        """
        :ru Свойство для получения информации о добавлении объекта в закладки у текущего пользователя.
        :en Property for getting information about adding an object to bookmarks from the current user.
        """
        return self.__video['is_favorite']

    @property
    def owner_id(self) -> int:
        """
        :ru Свойство для получения идентификатора пользователя/сообщества, загрузившего файл.
        :en Property for getting the ID of the user/community who uploaded the file.
        """
        return self.__video['owner_id']

    @property
    def access_key(self) -> str:
        """
        :ru Свойство для получения ключа доступа, для отправки файла другим пользователям.
        :ru Property for obtaining an access key, for sending a file to other users.
        """
        return self.__video['access_key']

    def get_attachment(self) -> str:
        """
        :ru Метод для получения строки идентификатора файла.
        :en Method for getting the file ID string.
        """
        return f"video{self.owner_id}_{self.id}_{self.access_key}"


