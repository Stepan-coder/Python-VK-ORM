import traceback
from VKBOT.bot import *


TOKEN = ""
APP_ID = 


bot = Bot()
bot.TOKEN = TOKEN
bot.APP_ID = APP_ID


while True:  # Этот бот тоже периодически ловит таймаут, но спокойно перезапускается таким образом
    try:
        for event in bot.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:

                # Эта строка обязательная, используемм объект input_message вместо event.input_message
                message = Message(event=event)

                print(message.attachments)

                # Теперь получить id пользователя можно этой командой
                print(message.text)

                # Теперь текст сообщения от пользователя лежит тут
                print(message.user_id)

                # Что бы получить от пользователя картинку нужно
                if message.have_attachments:  # Проверяем, что пользователь отправил вложение (хоть какое то)
                    if message.have_images:  # Проверяем, что в этих вложениях есть картинки
                        # input_message.get_images() - спискок с картинками от пользователя, поэтому можем по нему пройтись
                        for image in message.get_images():
                            # Для каждого изображения можно получить следующие параметры
                            print(image.id)  # Уникальный идентификационный номер картинки
                            print(image.date)  # Абсолютное время, когда картинка была создана
                            print(image.owner_id)
                            print(image.url)  # Прямую ссылку на изображение (ВКонтакте хостит все изображения)
                            print(image.width)  # Ширину картинки
                            print(image.height)  # Высоту картинки
                            # Такой командой можно сохранить картинку (обязательно указывать расширение файла)
                            image.save("photo.jpg")

                # Что бы получить от пользователя голосовое сообщение
                if message.have_attachments:  # Проверяем, что пользователь отправил вложение (хоть какое то)
                    print("message.have_voice_message", message.have_voice_message)
                    if message.have_voice_message:  # Проверяем, что в этих вложениях есть голосовые сообщения
                        # input_message.get_voice_messages() - спискок с голосовыми от пользователя, поэтому можем по нему пройтись
                        for voice_messages in message.get_voice_messages():
                            # Для каждого голосового можно получить следующие параметры
                            print(voice_messages.id)  # Уникальный идентификационный номер картинки
                            print(voice_messages.url_mp3)  # Прямую ссылку на голосовое в .mp3
                            print(voice_messages.url_oog)  # Прямую ссылку на голосовое в .oog
                            # Такой командой можно сохранить голосовое в .mp3
                            voice_messages.save_mp3("voice_messages.mp3")
                            voice_messages.save_oog('voice_messages.oog')

                # Получаем класс с инифой о пользователе
                user = bot.get_user_info(user_id=message.user_id)

                # Отправляем пользователю с user_id простое сообщение
                bot.send_message(user_id=message.user_id,
                                 message="Просто сообщение")

                # Отправляем стикер (где то была таблица со стикерами)
                bot.send_sticker(user_id=message.user_id, sticker_id=63)

                # Отправляем пользователю картинку
                bot.send_photo(user_id=message.user_id,
                               path_to_photo="some.jpg",
                               message="some")

                # создаём клавиатуру
                keyboard = bot.create_keyboard()

                # добавляем "обычную" кнопку (ниже пример с кнопкой-ссылкой)
                keyboard.add_button(text="PRIMARY",  # белая кнопка
                                    button=KeyboardButton.DEFAULT,
                                    color=VkKeyboardColor.PRIMARY)
                keyboard.add_button(text="SECONDARY",  # синяя кнопка
                                    button=KeyboardButton.DEFAULT,
                                    color=VkKeyboardColor.SECONDARY)
                keyboard.add_button(text="POSITIVE",  # зелёная кнопка
                                    button=KeyboardButton.DEFAULT,
                                    color=VkKeyboardColor.POSITIVE)
                keyboard.add_button(text="NEGATIVE",  # красная кнопка
                                    button=KeyboardButton.DEFAULT,
                                    color=VkKeyboardColor.NEGATIVE)

                # Делаем перенос. (максимально, в ширину моет быть только 4 кнопки,)
                keyboard.add_line()

                # добавляем кнопку-ссылку, сама ссылка прописывается в "payload"
                keyboard.add_button(text="Кнопка со ссылкой",
                                    button=KeyboardButton.OPENLINK,
                                    color=VkKeyboardColor.PRIMARY,
                                    payload="https://vk.com/stepanborodin")

                # Делаем перегрузку метода клавиатурой и отправляем
                bot.send_message(user_id=message.user_id,
                                 message="Сообщение с клавиатурой)",
                                 keyboard=keyboard.get_keyboard())
    except Exception as e:
        print(traceback.format_exc())

