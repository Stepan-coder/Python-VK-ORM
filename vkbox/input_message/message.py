import vk_api
from typing import Optional
from vkbox.input_message.photo import *
from vkbox.input_message.video import *  # Недоделано (проблемы со скачиванием)
from vkbox.input_message.audio import *
from vkbox.input_message.document import *
from vkbox.input_message.geoposition import *


class Message:
    def __init__(self, event: vk_api):
        self.__event = event

    @property
    def type(self):
        return self.__event.type

    @property
    def text(self) -> str:
        return self.__event.message.text

    @property
    def user_id(self) -> int:
        return self.__event.object.message['peer_id']

    @property
    def attachments(self) -> Optional[dict]:
        if len(self.__event.object['message']['attachments']) > 0:
            return self.__event.object['message']['attachments']
        elif 'geo' in self.__event.object['message']:
            return self.__event.object['message']
        else:
            return {}

    @property
    def have_attachments(self) -> bool:
        return len(self.attachments) > 0 or 'geo' in self.__event.object['message']

    @property
    def have_images(self) -> bool:
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'photo':
                counter += 1
        return counter > 0 and self.have_attachments

    @property
    def have_voice_message(self) -> bool:
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'audio_message':
                counter += 1
        return counter > 0 and self.have_attachments

    @property
    def have_video(self) -> bool:
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'video':
                counter += 1
        return counter > 0 and self.have_attachments

    @property
    def have_document(self) -> bool:
        if len(self.__event.object['message']['attachments']) == 0:
            return False
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'doc':
                counter += 1
        return counter > 0 and self.have_attachments

    @property
    def have_geo(self) -> bool:
        return 'geo' in self.__event.object['message']

    def get_images(self) -> List[PhotoMessage]:
        if not self.have_attachments:
            raise Exception('There are no images in this input_message!')
        return [PhotoMessage(attachment['photo']) for attachment in self.attachments
                if attachment['type'] == 'photo']

    def get_voice_messages(self) -> List[AudioMessage]:
        if not self.have_attachments:
            raise Exception('There are no audio messages in this input_message!')
        return [AudioMessage(attachment['audio_message']) for attachment in self.attachments
                if attachment['type'] == 'audio_message']

    def get_videos(self) -> List[VideoMessage]:
        if not self.have_attachments:
            raise Exception('There are no video messages in this input_message!')
        return [VideoMessage(attachment['video']) for attachment in self.attachments
                if attachment['type'] == 'video']

    def get_documents(self) -> List[DocumentMessage]:
        if not self.have_attachments:
            raise Exception('There are no document messages in this input_message!')
        return [DocumentMessage(attachment['doc']) for attachment in self.attachments
                if attachment['type'] == 'doc']

    def get_geo(self):
        if not self.have_attachments:
            raise Exception('There are no geo messages in this input_message!')
        return [GeoMessage(self.__event.object['message'])]



