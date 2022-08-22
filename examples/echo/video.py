import os
from quanario.bot import *


def echo_video(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():   # :ru Проверяем, есть ли вложения к сообщению от пользователя
                                        # :en Check if there are attachments to the message from the user
        if message.is_videos():   # :ru Проверяем, есть ли во вложениях видеозаписи
                                  # :en Check if there are videos in the attachments
            attachments = []
            for video in message.get_videos():  # :ru В цикле, перебираем все видео
                                                # :en In the loop, we go through all the videos
                attachments.append(video.get_attachment())  # :ru Сохраняем уже готовый 'attachment'
                                                            # :en Saving a ready-made 'attachment'
            bot.send.video(user_id=message.user_id,  # :ru Передаём уникальный идентификатор пользователя
                                                     # :en Transmitting a unique user ID
                           attachment=attachments)  # :ru Передаём вложение в аргумент 'attachments'
                                                    # :en Passing the attachment to the 'attachments' argument


TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

# :ru Создаём экземпляр класса Bot, передаём в него полученный токен и идентификатор сообщества
# :en Create an instance of the Bot class, pass the received token and community ID to it
bot = Bot(token=TOKEN, app_id=APP_ID)

# :ru В методе 'run' передаём название метода, который хотим сделать вызываемым при каждом сообщении пользователя
# :en In the 'run' method, we pass the name of the method that we want to make called with each user message
bot.run(init_method=echo_video)