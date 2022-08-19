from quanario.bot import *


def send_keyboard(bot: Bot, message: Message, args: tuple = None):
    # :ru Для отправки клавиатуры пользователю, её необходимо сгенерировать. Для этого вызовем метод 'create_keyboard'
    #  класса 'bot'. Вообще, клавиатуры бывают двух типов: обычные и так называемые 'inline'. Inline клавиатуры
    #  отличаются от обычных тем, что располагаются в беседе, в то время, как обычные клавиатуры, прикрепляются к
    #  нижней части экрана... Аргумент 'one_time', необходим для сохранения текущей клавиатуры у пользователя, до
    #  отправки следующей. (Ради интереса можете поэксперементировать с параметрами 'inline' и 'one_time')

    # :en To send the keyboard to the user, it must be generated. To do this, call the 'create_keyboard' method of the
    #  'bot' class. In general, there are two types of keyboards: regular and so-called 'inline'. Inline keyboards
    #  differ from regular keyboards in that they are located in a conversation, while regular keyboards are attached to
    #  the bottom of the screen... The 'one_time' argument is required to save the user's current keyboard before
    #  sending the next one. (For the sake of interest, you can experiment with the parameters 'inline' and 'one_time')

    keyboard = bot.create_keyboard(inline=False,
                                   one_time=False)
    # :ru Теперь, когда экземпляр клавиатуры получен, можем перейти к добавлению кнопок в клавиатуру (ну, а для чего же
    #  она ещё нужна). Каждая кнопка добавляется добавляется и настраивается отдельно. Всего, есть возможнось создать 3
    #  типа кнопок: обычная текстовая, она бывает 4-х разных цветов - белая, синяя, красная и зелёная (DEFAULT),
    #  кнопка-ссылка, для отправки пользователю ссылок на различные интернет ресурсы (OPENLINK) и кнопка, для отправки
    #  пользователем своей геопозиции боту (LOCATION), обратите внимание, что кнопока "LOCATION" должена
    #  распологаться единственной в ряду.

    # :ут Now that the keyboard instance has been received, we can proceed to adding buttons to the keyboard (well,
    #  what else is it needed for). Each button is added added and configured separately. In total, it is possible to
    #  create 3 types of buttons: plain text, it comes in 4 different colors - white, blue, red and green (DEFAULT),
    #  a link button to send the user links to various Internet resources (OPENLINK) and a button to send the user his
    #  geo-location to the bot (LOCATION), please note note that the "LOCATION" button should be the only one
    #  in the row.

    keyboard.add_button(text="PRIMARY",  # :ru Текст, который будет отображён на кнопке
                                         # :en The text that will be displayed on the button
                        button_type=VkKeyboardButton.DEFAULT,  # :ru Указываем, что это обычная кнопка
                                                               # :en We indicate that this is a regular button
                        color=VkKeyboardColor.PRIMARY)  # Белая кнопка (White button)
    keyboard.add_button(text="SECONDARY",
                        button_type=VkKeyboardButton.DEFAULT,
                        color=VkKeyboardColor.SECONDARY)  # Синяя кнопка (Blue button)
    keyboard.add_button(text="POSITIVE",
                        button_type=VkKeyboardButton.DEFAULT,
                        color=VkKeyboardColor.POSITIVE)  # Зелёная кнопка (Green button)
    keyboard.add_button(text="NEGATIVE",
                        button_type=VkKeyboardButton.DEFAULT,
                        color=VkKeyboardColor.NEGATIVE)  # Красная кнопка (Green button)

    # :ru Вообще, при добавлении кнопок, они добавляются "в ряд", поэтому, для переноса, нужно вызвать метод 'add_line'
    # :en In general, when adding buttons, they are added "in a row", therefore, to transfer, you need to call
    #  the 'add_line' method
    keyboard.add_line()

    # :ru Добавим кнопку-ссылку, с её помощью можно отправить пользователя на какой то внешний интернет ресурс.
    #  Обратите внимание, что мы не указываем цвет кнопки, т.к. кнопка ссылка может быть только белой
    # :en Let's add a link button, with its help you can send the user to some external Internet resource.
    #  Please note that we do not specify the color of the button, because the link button can only be white
    keyboard.add_button(text="Open this link",  # Текст, который будет отображен на кнопке
                                                # The text that will be displayed on the button
                        button_type=VkKeyboardButton.OPENLINK,  # :ru Указываем, что это кнопка-ссылка
                                                                # :en We indicate that this is a link button
                        payload="https://www.google.ru"  # :ru Указываем, ресурс, на который нужно отправть пользователя
                                                         # :en Specify the resource to which you want to send the user
                        )

    # :ru Давайте сделаем это еще раз переместим кнопки на клавиатуре
    # :en Let's do it again by moving the buttons on the keyboard
    keyboard.add_line()

    # :ru Добавим кноку для получения геолокации пользователя. Обратите внимание, что мы не указываем ни цвет кнопки,
    #  ни текст на ней, т.к. эта кнопка уже обладает полностью готовым дизайном от Вконтакт.
    # :en Add a button to get the user's geolocation. Please note that we do not specify either the color of the button
    #  or the text on it, because this button already has a completely ready-made design from Vkontakte.
    keyboard.add_button(button_type=VkKeyboardButton.LOCATION)

    # :ru Для отправки пользователю клавиатуры, её экземпляр необходимо передать в качестве аргумента методу 'message'.
    # :en To send the keyboard to the user, its instance must be passed as an argument to the 'message' method.
    bot.send.message(user_id=message.user_id,  # :ru Передаём уникальный идентификатор пользователя
                                               # :en Transmitting a unique user ID
                     message="Message text",  # :ru Передаём текст, который хотим отправить
                                              # :ru Passing the text we want to send
                     keyboard=keyboard  # :ru Передаём клавиатуру
                                        # :en Passing the keyboard
                     )

    # :ru Ещё одно важное уточнение, максимально, в клавиатуре может быть 10 кнопок, при этом, в ряду должно быть
    #  не более 4-х
    # :en Another important clarification, as much as possible, there can be 10 buttons in the keyboard, at the same
    #  time, there should be no more than 4 in a row


TOKEN = "acc6b6f00d67fe61afc26d1527898ce49510532e229601ceeb2b781c26b44794fe756f9dd58634c48de21"
APP_ID = 196221606

# :ru Создаём экземпляр класса Bot, передаём в него полученный токен и идентификатор сообщества
# :en Create an instance of the Bot class, pass the received token and community ID to it
bot = Bot(token=TOKEN, app_id=APP_ID)

# :ru В методе 'run' передаём название метода, который хотим сделать вызываемым при каждом сообщении пользователя
# :en In the 'run' method, we pass the name of the method that we want to make called with each user message
bot.run(init_method=send_keyboard)