import copy

from vkbox.bot import *


def some_method(bot: Bot, message: Message, args: tuple = None):
    keyboard = bot.create_keyboard()
    keyboard.add_button(text="Кнопка 1",
                        button=VkKeyboardButton.DEFAULT,
                        color=VkKeyboardColor.PRIMARY)
    keyboard.add_button(text="Кнопка 2",
                        button=VkKeyboardButton.OPENLINK,
                        color=VkKeyboardColor.PRIMARY,
                        payload="https://vk.com/im?sel=156967955")
    keyboard.add_line()
    keyboard.add_button(text="Кнопка 3",
                        button=VkKeyboardButton.LOCATION,
                        color=VkKeyboardColor.PRIMARY)


    carousel = bot.create_carousel()
    carousel.add_element(title="Какой-то заголовок слова ещё какой то текст можно добавить ещё текста",
                         description="Какое-то описание",
                         attachment=bot.upload.photo(user_id=message.user_id,
                                                     path_to_photo="Слова.png"),
                         keyboard=keyboard)
    carousel.add_element(title="Какой-то заголовок аудирование",
                         description="Какое-то описание",
                         attachment=bot.upload.photo(user_id=message.user_id,
                                                     path_to_photo="Аудирование.png"),
                         keyboard=keyboard)
    carousel.add_element(title="Какой-то заголовок игра",
                         description="Какое-то описание",
                         attachment=bot.upload.photo(user_id=message.user_id,
                                                     path_to_photo="Игра.png"),
                         keyboard=keyboard)
    carousel.add_element(title="Какой-то заголовок магазин",
                         description="Какое-то описание",
                         attachment=bot.upload.photo(user_id=message.user_id,
                                                     path_to_photo="Магазин.png"),
                         keyboard=keyboard)
    bot.send.carousel(user_id=message.user_id,
                      message="Отправляем клавиатуру и карусель",
                      carousel=carousel)


TOKEN = "acc6b6f00d67fe61afc26d1527898ce49510532e229601ceeb2b781c26b44794fe756f9dd58634c48de21"
APP_ID = 196221606


bot = Bot()
bot.TOKEN = TOKEN
bot.APP_ID = APP_ID
bot.run(init_method=some_method)