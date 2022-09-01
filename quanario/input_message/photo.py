import os
import urllib.request
from typing import Tuple


class Photo:
    def __init__(self, photo: dict):
        self.__photo = photo
        self.__width, self.__height, self.__url = self.__get_image()

    @property
    def id(self) -> int:
        """
        :ru Свойство для получения уникального идентификатор файла.
        :en Property for getting a unique file identifier.
        """
        return self.__photo['id']

    @property
    def width(self) -> int:
        """
        :ru Свойство для получения ширины изображения.
        :en Property for getting the width of the photo.
        """
        return self.__width

    @property
    def height(self) -> int:
        """
        :ru Свойство для получения высоты изображения.
        :en Property for getting the height of the photo.
        """
        return self.__height

    @property
    def url(self) -> str:
        """
        :ru Свойство для получения ссылки для скачивания файла.
        :en Property for getting a link to download a file.
        """
        return self.__url

    @property
    def album_id(self) -> int:
        """
        :ru Свойство для получения альбома, где размещён файл.
        :en Property for getting the album where the file is placed.
        """
        return self.__photo['album_id']

    @property
    def date(self) -> int:
        """
        :ru Свойство для получения даты загрузки файла на сервер `ВКонтакте` (в формате Unix).
        :en Property for getting the file upload date to the `VKontakte` server (in Unix format).
        """
        return self.__photo['date']

    @property
    def post_id(self) -> int:
        """
        :ru Свойство для получения идентификатора поста.
        :en Property for getting the post ID.
        """
        return self.__photo['post_id']

    @property
    def owner_id(self) -> int:
        """
        :ru Свойство для получения идентификатора пользователя/сообщества, загрузившего файл.
        :en Property for getting the ID of the user/community who uploaded the file.
        """
        return self.__photo['owner_id']

    @property
    def access_key(self) -> str:
        """
        :ru Свойство для получения ключа доступа, для отправки файла другим пользователям.
        :en Property for obtaining an access key, for sending a file to other users.
        """
        return self.__photo['access_key']

    def get_attachment(self) -> str:
        """
        :ru Метод для получения строки идентификатора файла.
        :en Method for getting the file ID string.
        """
        return f"photo{self.owner_id}_{self.id}_{self.access_key}"

    def save(self, path_to_save: str) -> None:
        """
        :ru Метод для сохранения файла в системе.
        :en A method for saving a file in the system.
        """
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_save))):
            raise Exception('Invalid path to save the file!')
        urllib.request.urlretrieve(self.url, path_to_save)

    def __get_image(self) -> Tuple[int, int, str]:
        """
        :ru Приватный метод для поиска наибольшего разрешения файла.
        :en A private method for finding the highest file resolution.
        """
        sorted_photos = sorted(self.__photo['sizes'], key=lambda x: (x['width'], x['height']), reverse=True)
        return sorted_photos[0]['width'], sorted_photos[0]['height'], sorted_photos[0]['url']
