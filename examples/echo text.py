from quanario.bot import *


def some_method(bot: Bot, message: Message, args: tuple = None):
    user = bot.get_user_info(user_id=message.user_id)
    bot.upload.video(user_id=message.user_id,
                     path_to_video=r"C:\Users\stepa\Downloads\Прости мой старый друг, я должен разбудить тебя! [Савва. Сердце воина].mp4",
                     name="Присти мой старый друг",
                     description="Просто видео")

TOKEN = "acc6b6f00d67fe61afc26d1527898ce49510532e229601ceeb2b781c26b44794fe756f9dd58634c48de21"
APP_ID = 196221606


bot = Bot()
bot.TOKEN = TOKEN
bot.APP_ID = APP_ID
bot.run(init_method=some_method)
