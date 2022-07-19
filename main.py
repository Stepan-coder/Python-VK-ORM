import vk_api
from vk_api import VkApi

from vk_api.upload import VkUpload
from vk_api.vk_api import VkApiMethod
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from person import *

TOKEN = "acc6b6f00d67fe61afc26d1527898ce49510532e229601ceeb2b781c26b44794fe756f9dd58634c48de21"
APP_ID = 196221606


class Bot:
    def __init__(self, TOKEN: str, APP_ID: int):
        self.__TOKEN = TOKEN
        self.__APP_ID = APP_ID
        self.__vk_session = VkApi(token=self.__TOKEN)
        self.__vk_session.RPS_DELAY = 1 / 100
        self.__longpoll = VkBotLongPoll(self.__vk_session, self.__APP_ID)
        self.__vk = self.__vk_session.get_api()

    @property
    def token(self) -> str:
        return self.__TOKEN

    @property
    def app_id(self) -> int:
        return self.__APP_ID

    @property
    def vk(self) -> vk_api.vk_api.VkApiMethod:
        return self.__vk

    def get_user_info(self, user_id) -> Person:
        result = self.__vk.users.get(user_ids=user_id,
                                   fields="about, bdate, sex, city, country, last_seen, online, domain, relation")[0]
        return Person(person_json=result)

    def run(self):
        while True:
            try:
                for event in self.__longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        print(self.get_user_info(user_id=event.object.message['peer_id']).sex)
                        # send_message(vk=self.vk, peer_id=event.object.message['peer_id'], message="Привет")
                        # self.done_order(event.object.message['peer_id'], event)


            except Exception as e:
                pass
                # print(traceback.format_exc())





def send_message(vk, peer_id, message):
    vk.messages.send(
        peer_id=peer_id,
        message=message,
        random_id=get_random_id()
    )


bot = Bot(TOKEN=TOKEN, APP_ID=APP_ID)
bot.run()