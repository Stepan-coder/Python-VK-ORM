import os
import vk_api
import ffmpeg
from pydub import AudioSegment
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class Upload:
    def __init__(self, vk: vk_api.vk_api.VkApiMethod):
        self.__vk = vk

    def voice(self, user_id: int, path_to_audio: str) -> str:
        if not os.path.exists(path_to_audio):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        if not os.path.basename(path_to_audio).endswith('ogg'):
            converted_path = Upload.convert_audio(path_to_audio=path_to_audio, to_format='ogg')
            audio = upload.audio_message(converted_path, peer_id=user_id)
            os.remove(converted_path)
        else:
            audio = upload.audio_message(path_to_audio, peer_id=user_id)
        return f"audio_message{audio['audio_message']['owner_id']}_{audio['audio_message']['id']}"

    def photo(self, user_id: int, path_to_photo: str) -> str:
        if not os.path.exists(path_to_photo):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        photo = upload.photo_messages(path_to_photo)
        return f"photo{photo[0]['owner_id']}_{photo[0]['id']}_{photo[0]['access_key']}"

    def audio(self, user_id: int, path_to_audio: str) -> str:
        if not os.path.exists(path_to_audio):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        audio = upload.audio_message(path_to_audio, peer_id=user_id)
        return f"audio_message{audio['audio_message']['owner_id']}_{audio['audio_message']['id']}"

    def video(self, user_id: int, path_to_video: str) -> str:
        if not os.path.exists(path_to_video):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        video = upload.video(path_to_video)
        return f"audio_message{video['audio_message']['owner_id']}_{video['audio_message']['id']}"

    def document(self, user_id: int, path_to_document: str) -> str:
        if not os.path.exists(path_to_document):
            raise Exception('The specified file path does not exist!')
        upload = VkUpload(self.__vk)
        document = upload.document_message(doc=path_to_document,
                                           title=str(os.path.basename(path_to_document)).split(".")[0],
                                           peer_id=user_id)
        return f"doc{document['doc']['owner_id']}_{document['doc']['id']}"

    @staticmethod
    def convert_audio(path_to_audio: str, to_format: str) -> str:
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




