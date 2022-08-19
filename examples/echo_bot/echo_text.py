from quanario.bot import *


def echo_text(bot: Bot, message: Message, args: tuple = None):
    # :ru Для создания простохо эхо бота нам необходимо отправить пользователю тот же текст, который отправил он нам.
    # :en To create an echo echo bot, we need to send the user the same text that he sent to us.
    bot.send.message(user_id=message.user_id,  # :ru Передаём уникальный идентификатор пользователя
                                               # :en Transmitting a unique user ID
                     message=message.text)  # Передаём текст, который нам отправил ользователь


TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

# :ru Создаём экземпляр класса Bot, передаём в него полученный токен и идентификатор сообщества
# :en Create an instance of the Bot class, pass the received token and community ID to it
bot = Bot(token=TOKEN, app_id=APP_ID)

# :ru В методе 'run' передаём название метода, который хотим сделать вызываемым при каждом сообщении пользователя
# :en In the 'run' method, we pass the name of the method that we want to make called with each user message
bot.run(init_method=echo_text)
