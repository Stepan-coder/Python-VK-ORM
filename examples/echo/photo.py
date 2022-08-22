import os
from quanario.bot import *


def echo_photo(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():   # :ru Проверяем, есть ли вложения к сообщению от пользователя
                                        # :en Check if there are attachments to the message from the user
        if message.is_photos():   # :ru Проверяем, есть ли во вложениях изображения
                                  # :en Check if there are images in the attachments
            attachments = []
            for photo in message.get_photos():  # :ru В цикле, перебираем все изображения
                                                # :en In the loop, we iterate through all the images
                path_to_photo = os.path.join(os.getcwd(), f"{photo.id}.png")  # :ru Указываем путь, для сохранения
                                                                              # :en Specify the path to save
                photo.save(path_to_save=path_to_photo)  # :ru Сохраняем изображение
                                                        # :en Saving the image
                # :ru Загружаем изображение на сервера Вк и добавляем полученную строку в список 'attachments'
                # :en Upload the image to the Vk servers and add the resulting string to the list of 'attachments'
                attachments.append(bot.upload.photo(user_id=message.user_id, path_to_photo=path_to_photo))
            bot.send.photo(user_id=message.user_id,  # :ru Передаём уникальный идентификатор пользователя
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
bot.run(init_method=echo_photo)