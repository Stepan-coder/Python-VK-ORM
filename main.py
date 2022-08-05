# import traceback
#
# from vkbox.bot import *
#
#
# def some_method(bot: Bot, message: Message, args: tuple = None):
#     print("have attachments", message.have_attachments)
#
#     # Теперь получить id пользователя можно этой командой
#     print(message.text)
#
#     # Теперь текст сообщения от пользователя лежит тут
#     print(message.user_id)
#
#     # Что бы получить от пользователя картинку нужно
#     if message.have_attachments:  # Проверяем, что пользователь отправил вложение (хоть какое то)
#         if message.have_images:  # Проверяем, что в этих вложениях есть картинки
#             # input_message.get_images() - спискок с картинками от пользователя, поэтому можем по нему пройтись
#             for image in message.get_images():
#                 # Для каждого изображения можно получить следующие параметры
#                 print(image.id)  # Уникальный идентификационный номер картинки
#                 print(image.date)  # Абсолютное время, когда картинка была создана
#                 print(image.owner_id)
#                 print(image.url)  # Прямую ссылку на изображение (ВКонтакте хостит все изображения)
#                 print(image.width)  # Ширину картинки
#                 print(image.height)  # Высоту картинки
#                 # Такой командой можно сохранить картинку (обязательно указывать расширение файла)
#                 image.save("photo.jpg")
#
#     # Что бы получить от пользователя голосовое сообщение
#     if message.have_attachments:  # Проверяем, что пользователь отправил вложение (хоть какое то)
#         if message.have_voice_message:  # Проверяем, что в этих вложениях есть голосовые сообщения
#             # input_message.get_voice_messages() - спискок с голосовыми от пользователя, поэтому можем по нему пройтись
#             for voice_message in message.get_voice_messages():
#                 # Для каждого голосового можно получить следующие параметры
#                 print(voice_message.id)  # Уникальный идентификационный номер картинки
#                 print(voice_message.url_mp3)  # Прямую ссылку на голосовое в .mp3
#                 print(voice_message.url_oog)  # Прямую ссылку на голосовое в .oog
#                 # Такой командой можно сохранить голосовое в .mp3
#                 voice_message.save_mp3("voice_messages.mp3")
#                 voice_message.save_oog('voice_messages.oog')
#
#     # Что бы получить от пользователя голосовое сообщение
#     if message.have_attachments:  # Проверяем, что пользователь отправил вложение (хоть какое то)
#         if message.have_document:  # Проверяем, что в этих вложениях есть документы
#             # input_message.get_documents() - спискок с документами от пользователя, поэтому можем по нему пройтись
#             for document in message.get_documents():
#                 # Для каждого документа можно получить следующие параметры
#                 print(document.id)  # Уникальный идентификационный номер картинки
#                 print(document.date)  # Абсолютное время, когда документ был создан
#                 print(document.owner_id)
#                 print(document.url)  # Прямую ссылку на изображение (ВКонтакте хостит все изображения)
#                 print(document.extension)  # расширение файла
#                 print(document.size)  # Размер файла
#                 # Такой командой можно сохранить документ (имеется ввиду файл)
#                 document.save(f"new_document.edf")
#
#     # Что бы получить от пользователя голосовое сообщение
#     if message.have_attachments:  # Проверяем, что пользователь отправил вложение (хоть какое то)
#         if message.have_geo:  # Проверяем, что в этих вложениях есть карта
#             # input_message.get_geo() - спискок с документами от пользователя, поэтому можем по нему пройтись
#             for geo in message.get_geo():
#                 # Для каждого документа можно получить следующие параметры
#                 print(geo.id)  # Уникальный идентификационный номер картинки
#                 print(geo.date)  # Абсолютное время, когда документ был создан
#                 print(geo.latitude)  # Широта пользователя
#                 print(geo.longitude)  # Долгота пользователя
#                 print(geo.title)  # Описание координаты
#                 print(geo.country)  # Страна
#                 print(geo.city)  # Город
#
#     # Получаем класс с инифой о пользователе
#     user = bot.get_user_info(user_id=message.user_id)
#
#     # Отправляем пользователю с user_id простое сообщение
#     bot.send_message(user_id=message.user_id,
#                      message="Просто сообщение")
#
#     # Отправляем стикер (где то была таблица со стикерами)
#     bot.send_sticker(user_id=message.user_id, sticker_id=63)
#
#     # # Отправляем пользователю картинку
#     # bot.send_photo(user_id=message.user_id,
#     #                path_to_photo="some.jpg",
#     #                message="some")
#
#     # создаём клавиатуру
#     keyboard = bot.create_keyboard()
#
#     # добавляем "обычную" кнопку (ниже пример с кнопкой-ссылкой)
#     keyboard.add_button(text="PRIMARY",  # белая кнопка
#                         button=VkKeyboardButton.DEFAULT,
#                         color=VkKeyboardColor.PRIMARY)
#     keyboard.add_button(text="SECONDARY",  # синяя кнопка
#                         button=VkKeyboardButton.DEFAULT,
#                         color=VkKeyboardColor.SECONDARY)
#     keyboard.add_button(text="POSITIVE",  # зелёная кнопка
#                         button=VkKeyboardButton.DEFAULT,
#                         color=VkKeyboardColor.POSITIVE)
#     keyboard.add_button(text="NEGATIVE",  # красная кнопка
#                         button=VkKeyboardButton.DEFAULT,
#                         color=VkKeyboardColor.NEGATIVE)
#
#     # Делаем перенос. (максимально, в ширину моет быть только 4 кнопки,)
#     keyboard.add_line()
#
#     # добавляем кнопку-ссылку, сама ссылка прописывается в "payload"
#     keyboard.add_button(text="Кнопка со ссылкой",
#                         button=VkKeyboardButton.OPENLINK,
#                         color=VkKeyboardColor.PRIMARY,
#                         payload="https://vk.com/stepanborodin")
#     keyboard.add_line()
#     keyboard.add_button(text="text",
#                         button=VkKeyboardButton.LOCATION,
#                         color=VkKeyboardColor.PRIMARY)
#
#     # Делаем перегрузку метода клавиатурой и отправляем
#     bot.send_message(user_id=message.user_id,
#                      message="Сообщение с клавиатурой)",
#                      keyboard=keyboard.get_keyboard())
#
#
# TOKEN = "*YOUR TOKEN*"
# APP_ID = 000000000 # YOUR APP ID
#
#
# bot = Bot()
# bot.TOKEN = TOKEN
# bot.APP_ID = APP_ID
# bot.run(init_method=some_method)
#
#
#
#
#
#
#
