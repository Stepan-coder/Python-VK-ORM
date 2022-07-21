from VKBOT.bot import *


TOKEN = "acc6b6f00d67fe61afc26d1527898ce49510532e229601ceeb2b781c26b44794fe756f9dd58634c48de21"
APP_ID = 196221606


bot = Bot(TOKEN=TOKEN, APP_ID=APP_ID)


while True:  # Этот бот тоже периодически ловит таймаут, но спокойно перезапускается таким образом
    try:
        for event in bot.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:

                message_text = event.message.text  # - тут лежит текст сообщения от пользователя

                # event.object.message['peer_id'] - уникальный айдишник пользователя
                # Получаем класс с инифой о пользователе
                user = bot.get_user_info(user_id=event.object.message['peer_id'])  # На выходе получаем класс с инфой о пользователе

                # Отправляем пользователю с user_id простое сообщение
                bot.send_message(user_id=event.object.message['peer_id'],
                                 message="Просто сообщение")

                # Отправляем стикер (где то была таблица со стикерами)
                bot.send_sticker(user_id=event.object.message['peer_id'], sticker_id=63)

                # Отправляем пользователю картинку
                bot.send_photo(user_id=event.object.message['peer_id'], path_to_photo="123.jpg", message="some")

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
                bot.send_message(user_id=event.object.message['peer_id'],
                                 message="Сообщение с клавиатурой)",
                                 keyboard=keyboard.get_keyboard())
    except Exception as e:
        print(traceback.format_exc())

