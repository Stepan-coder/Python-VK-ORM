"""
:authors: Stepan Borodin
:license: CC-BY-NC
:copyright: (c) 2022 Stepan-coder
:link: https://github.com/Stepan-coder/Quanario_VK
"""


import os
import vk_api
import ffmpeg
from pydub import AudioSegment
from vk_api import VkApi
from vk_api.upload import VkUpload, FilesOpener
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class Upload:
    """
    :ru Класс реализующий  загрузку медиаконтента на сервера `ВКонтакте`, для дальнейшей отправки пользователям.
    :en A class that implements uploading media content to servers `VKontakte`, for further sending to users.
    """
    def __init__(self, vk: vk_api.vk_api.VkApiMethod):
        self.__vk = vk

    def voice(self, user_id: int, path_to_voice: str) -> str:
        """
        ru: Этот метод позволяет получить 'attachment' для аудиофайла для отправки его пользователю.
        en: This method allows you to get an 'attachment' for an audio file to send it to the user.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param path_to_voice:ru Путь к аудиофайлу, который необходимо загрузить.
        :param path_to_voice:en The path to the audio file to upload.
        :type path_to_voice: str
        """
        if not os.path.exists(path_to_voice):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        converted_path = Upload.convert_audio(path_to_audio=path_to_voice, to_format='ogg')
        audio = upload.audio_message(converted_path, peer_id=user_id)
        os.remove(converted_path)
        return f"audio_message{audio['audio_message']['owner_id']}_{audio['audio_message']['id']}"

    def photo(self, user_id: int, path_to_photo: str) -> str:
        """
        ru: Этот метод позволяет получить 'attachment' для картинки для отправки её пользователю.
        en: This method allows you to get an 'attachment' for an image to send it to the user.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param path_to_photo:ru Путь к изображению, которое необходимо загрузить.
        :param path_to_photo:en The path to the image file to upload.
        :type path_to_photo: str
        """
        if not os.path.exists(path_to_photo):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        photo = upload.photo_messages(path_to_photo)
        return f"photo{photo[0]['owner_id']}_{photo[0]['id']}_{photo[0]['access_key']}"

    def file(self, user_id: int, path_to_file: str) -> str:
        """
        ru: Этот метод позволяет получить 'attachment' для фйла для отправки его пользователю.
        en: This method allows you to get an 'attachment' for the file to send it to the user.

        :param user_id:ru Уникальный id пользователя в социальной сети ВКонтакте.
        :param user_id:en Unique user id in the VKontakte social network.
        :type user_id: int

        :param path_to_file:ru Путь к файлу, который необходимо загрузить.
        :param path_to_file:en The path to the file to upload.
        :type path_to_file: str
        """
        if not os.path.exists(path_to_file):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        document = upload.document_message(doc=path_to_file,
                                           title=str(os.path.basename(path_to_file)).split(".")[0],
                                           peer_id=user_id)
        return f"doc{document['doc']['owner_id']}_{document['doc']['id']}"

    @staticmethod
    def convert_audio(path_to_audio: str, to_format: str) -> str:
        """
        :ru У социальной сети ВКонтакте есть странность при отправке аудиофайла как голосового сообщения - аудиофайл
         обязательно должен быть моноканальныи и в формате .ogg. Именно эту проблему и решает этот метод. Важное
         уточнение - для корректной работы этого метода требуется обязательная установка пакета 'ffmpeg', а так же
         добавить его в переменные среды.
        :en The VKontakte social network has an oddity when sending an audio file as a voice message - an audio file
         it must be single-channel and in .ogg format. This is exactly the problem that this method solves. Important
         clarification - for the correct operation of this method, the mandatory installation of the 'ffmpeg' package is
         required, as well as add it to the environment variables.

        :param path_to_audio:ru Путь к аудиофайлу, который необходимо преобразовать.
        :param path_to_audio:en The path to the audio file to be converted.
        :type path_to_audio: str

        :param to_format:ru Формат, к которому необходимо привести входной аудиофайл.
        :param to_format:en The format to which the input audio file should be converted.
        :type to_format: str
        """
        if not os.path.exists(path_to_audio):
            raise Exception('The specified file path does not exist!')
        name = ".".join(os.path.basename(path_to_audio).split(".")[:1])
        format = ".".join(os.path.basename(path_to_audio).split(".")[1:])
        dir = os.path.dirname(os.path.abspath(path_to_audio))
        if format not in ['ogg', 'mp3', 'wav', 'raw']:
            raise Exception(f"'{format}' is an unsupported format for an audio file")
        if to_format not in ['ogg', 'mp3', 'wav', 'raw']:
            raise Exception(f"'{to_format}' is an unsupported format for an audio file")
        sound = AudioSegment.from_file(file=path_to_audio, format=format)
        sound.set_channels(1)
        sound.export(out_f=os.path.join(dir, f"{name}.{to_format}"), format=to_format)
        return os.path.join(dir, f"{name}.{to_format}")




