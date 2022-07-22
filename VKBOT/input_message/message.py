import vk_api
from VKBOT.input_message.photo import *
from VKBOT.input_message.audio_message import *


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
    def attachments(self) -> dict:
        return self.__event.object['message']['attachments']

    @property
    def have_attachments(self) -> bool:
        return len(self.attachments) > 0

    @property
    def have_images(self) -> bool:
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'photo':
                counter += 1
        return counter > 0 and self.have_attachments

    @property
    def have_voice_message(self) -> bool:
        counter = 0
        for attachment in self.attachments:
            if attachment['type'] == 'audio_message':
                counter += 1
        return counter > 0 and self.have_attachments

    def get_images(self):
        if not self.have_attachments:
            raise Exception('There are no images in this input_message!')
        return [Photo(attachment['photo']) for attachment in self.attachments
                if attachment['type'] == 'photo']

    def get_voice_messages(self):
        if not self.have_attachments:
            raise Exception('There are no audio messages in this input_message!')
        return [AudioMessage(attachment['audio_message']) for attachment in self.attachments
                if attachment['type'] == 'audio_message']



