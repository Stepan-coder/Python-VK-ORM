import os
from quanario.bot import *


def echo_voice_audio(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():   # :ru Проверяем, есть ли вложения к сообщению от пользователя
                                        # :en Check if there are attachments to the message from the user
        if message.is_voices():   # :ru Проверяем, есть ли во вложениях голосовые сообщения
                                  # :en Check if there are voice messages in the attachments
            attachments = []
            for voice in message.get_voices():  # :ru В цикле, перебираем все голосовые сообщения
                                                # :en In the loop, we go through all the voice messages
                path = os.path.join(os.getcwd(), f"{voice.id}.ogg")  # :ru Указываем путь, для сохранения
                                                                     # :en Specify the path to save
                # voice.save_mp3(path_to_save=path)
                voice.save_ogg(path_to_save=path)  # :ru Предпочтительно сохранять голосовые в формате '.ogg'
                                                   # :en It is preferable to save voice messages in the '.ogg' format
                # :ru Загружаем файлы на сервера Вк и добавляем полученную строку в список 'attachments'
                # :en Upload the files to the Vk servers and add the resulting string to the list of 'attachments'
                attachments.append(bot.upload.voice(user_id=message.user_id, path_to_voice=path))
            bot.send.voice(user_id=message.user_id,  # :ru Передаём уникальный идентификатор пользователя
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
bot.run(init_method=echo_voice_audio)