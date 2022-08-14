from quanario.bot import *


def some_method(bot: Bot, message: Message, args: tuple = None):

    if message.have_attachments:
        print(message.attachments)

        if message.have_photos:
            for photo in message.get_photos():
                print(photo.id)
                print(photo.owner_id)
                print(photo.access_key)
                print(photo.get_attachment())
                bot.send.photo(user_id=message.user_id,
                               attachment=photo.get_attachment())

        if message.have_videos:
            for video in message.get_videos():
                print(video.id)
                print(video.owner_id)
                print(video.access_key)
                print(video.get_attachment())
                bot.send.video(user_id=message.user_id,
                               attachment=video.get_attachment())

        if message.have_files:
            for video in message.get_files():
                print(video.id)
                print(video.owner_id)
                print(video.access_key)
                print(video.get_attachment())
                bot.send.file(user_id=message.user_id,
                               attachment=video.get_attachment())





TOKEN = "acc6b6f00d67fe61afc26d1527898ce49510532e229601ceeb2b781c26b44794fe756f9dd58634c48de21"
APP_ID = 196221606


bot = Bot()
bot.TOKEN = TOKEN
bot.APP_ID = APP_ID
bot.run(init_method=some_method)