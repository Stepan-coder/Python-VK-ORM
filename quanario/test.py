from quanario.bot import *


def send_carousel(bot: Bot, message: Message, args: tuple = None):
    # bot.send.message(user_id=message.user_id,
    #                  message=message.text)

    if message.is_have_attachments():
        if message.is_photos():
            attachments = []
            for photo in message.get_photos():
                path_to_photo = os.path.join(os.getcwd(), f"{photo.id}.png")
                photo.save(path_to_save=path_to_photo)
                attachments.append(bot.upload.photo(user_id=message.user_id, path_to_photo=path_to_photo))
            bot.send.photo(user_id=message.user_id,
                           attachment=attachments)

    if message.is_have_attachments():
        if message.is_files():
            attachments = []
            for file in message.get_files():
                path = os.path.join(os.getcwd(), f"{file.id}.{file.extension}")
                file.save(path_to_save=path)
                attachments.append(bot.upload.file(user_id=message.user_id, path_to_file=path))
            bot.send.file(user_id=message.user_id,
                          attachment=attachments)

    if message.is_have_attachments():
        # if message.is_audio():
        #     for audio in message.get_audios():
        if message.is_voices():
            attachments = []
            for voice in message.get_voices():
                path = os.path.join(os.getcwd(), f"{voice.id}.ogg")
                # voice.save_mp3(path_to_save=path)
                voice.save_ogg(path_to_save=path)
                attachments.append(bot.upload.voice(user_id=message.user_id, path_to_voice=path))
            bot.send.voice(user_id=message.user_id,
                           attachment=attachments)

    if message.is_have_attachments():
        if message.is_videos():
            attachments = []
            for video in message.get_videos():
                attachments.append(video.get_attachment())
            bot.send.video(user_id=message.user_id,
                           attachment=attachments)


TOKEN = "acc6b6f00d67fe61afc26d1527898ce49510532e229601ceeb2b781c26b44794fe756f9dd58634c48de21"
APP_ID = 196221606


bot = Bot()
bot.TOKEN = TOKEN
bot.APP_ID = APP_ID
bot.run(init_method=send_carousel)