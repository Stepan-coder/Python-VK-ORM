import vk_api
from VKBOT.photo import *


class Message:
    def __init__(self, event: vk_api):
        self.__event = event

    @property
    def type(self):
        return self.__event.type

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
    def text(self) -> str:
        return self.__event.message.text

    def get_images(self):
        if not self.have_attachments:
            raise Exception('There are no images in this message!')
        return [Photo(photo=attachment['photo']) for attachment in self.attachments if attachment['type'] == 'photo']



