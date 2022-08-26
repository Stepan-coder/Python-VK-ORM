# Отправка клавиатуры пользователю (Sending the keyboard to the user)

Для начала, создадим шаблон кода для реализации бота в социальной сети `Вконтакте`. Для этого, импортируем библиотеку `quanario`, создадим экземпляр класса `Bot` и передадим ему токен и идентификатор сообщества для авторизации. *(Подробнее об авторизации в оффициальной документации ВКонтакте)* Далее, в аргументе `init_method` метода `run` передаём название метода, который хотим сделать вызываемым при каждом сообщении полученном от пользователя. Шаблон для бота готов!

> *To begin with, let's create a code template for implementing a bot on the Vkontakte social network. To do this, import the `quanario` library, create an instance of the `Bot` class and give it a token and a community identifier for authorization. *((For more information about authorization in the official documentation of VKontakte)* Next, in the `init_method` argument of the `run` method, we pass the name of the method that we want to make called with each message received from the user. The template for the bot is ready!*
```Python3
from quanario.bot import *


def send_keyboard(bot: Bot, message: Message, args: tuple = None):
    pass

TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

bot = Bot(token=TOKEN, app_id=APP_ID)
bot.run(init_method=send_keyboard)
```
---
Для отправки клавиатуры пользователю, её необходимо сгенерировать. Для этого вызовем метод `create_keyboard()` экземпляра класса `bot`. Вообще, клавиатуры бывают двух типов: `обычные` и так называемые `inline`. Inline клавиатуры отличаются от обычных тем, что располагаются в беседе, в то время, как обычные клавиатуры, прикрепляются к нижней части экрана... Аргумент `one_time`, необходим для сохранения текущей клавиатуры у пользователя, до отправки следующей. (Ради интереса можете поэкспериментировать с параметрами `inline` и `one_time`)
>*To send the keyboard to the user, it must be generated. To do this, call the `create_keyboard()` method of the `bot` class instance. In general, there are two types of keyboards: `regular` and the so-called `inline`. Inline keyboards differ from regular keyboards in that they are located in a conversation, while regular keyboards are attached to the bottom of the screen... The `one_time` argument is required to save the user's current keyboard before sending the next one. (For the sake of interest, you can experiment with the parameters `inline` and `one_time`)*
```Python3
def send_keyboard(bot: Bot, message: Message, args: tuple = None):
    keyboard = bot.create_keyboard(inline=False,
                                   one_time=False)
```

Теперь, когда экземпляр клавиатуры получен, можем перейти к добавлению кнопок в клавиатуру (ну, а для чего же она ещё нужна). Каждая кнопка добавляется и настраивается отдельно. Всего, есть возможность создать 3 типа кнопок: обычная текстовая, она бывает 4-х разных цветов - `белая`, `синяя`, `красная` и `зелёная` (DEFAULT), кнопка-ссылка, для отправки пользователю ссылок на различные интернет ресурсы (OPENLINK) и кнопка, для отправки пользователем своей геопозиции боту (LOCATION), обратите внимание, что **кнопка `LOCATION` должна располагаться единственной в ряду**.
> *Now that an instance of the keyboard has been received, we can proceed to adding buttons to the keyboard (well, what else is it needed for). Each button is added and configured separately. In total, it is possible to create 3 types of buttons: plain text, it comes in 4 different colors - `white`, `blue`, `red` and `green` (DEFAULT), a link button to send the user links to various Internet resources (OPENLINK) and a button to send the user his geo-location to the bot (LOCATION), please note that **the `LOCATION` button should be the only one in the row**.*
```Python3
def send_keyboard(bot: Bot, message: Message, args: tuple = None):
    keyboard = bot.create_keyboard(inline=False,
                                   one_time=False)
    keyboard.add_button(text="PRIMARY",
                        button_type=VkKeyboardButton.DEFAULT, 
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
```
Вообще, при добавлении кнопок, они добавляются `в ряд`, поэтому, для переноса на следующую строку, нужно вызвать метод `add_line()`.
>*In general, when adding buttons, they are added `in a row`, so to move to the next line, you need to call the `add_line()` method.*
```Python3
    keyboard.add_line()
```

Добавим кнопку-ссылку, с её помощью можно отправить пользователя на какой-то внешний интернет ресурс. **Обратите внимание, что мы не указываем цвет кнопки, т.к. кнопка ссылка может быть только белой**.
>*Let's add a link button, with its help you can send the user to some external Internet resource. **Please note that we do not specify the color of the button, because the link button can only be white**.*
```Python3
    keyboard.add_button(text="Open this link",  
                        button_type=VkKeyboardButton.OPENLINK, 
                        payload="https://www.google.ru")
```

Давайте сделаем это еще раз переместим кнопки на клавиатуре
>*Let's do it again by moving the buttons on the keyboard*
```Python3
    keyboard.add_line()
```

Добавим кнопку для получения `геолокации` пользователя. **Обратите внимание, что мы не указываем ни цвет кнопки, ни текст на ней, т.к. эта кнопка уже обладает полностью готовым дизайном от Вконтакте**.
>*Add a button to get the user's `geolocation`. **Please note that we do not specify either the color of the button or the text on it, because this button already has a completely ready-made design from Vkontakte**.*
```Python3   
    keyboard.add_button(button_type=VkKeyboardButton.LOCATION)
```
---
Для отправки пользователю клавиатуры, её экземпляр необходимо передать в качестве аргумента методу `message`.
>*To send the keyboard to the user, its instance must be passed as an argument to the `message` method.*
```Python3  
    bot.send.message(user_id=message.user_id,
                     message="Message text",
                     keyboard=keyboard)
```
---
По итогу получаем следующий код для бота, который в ответ на любое сообщение пользователя отправляет ему сообщение "Message text" с клавиатурой.
>*As a result, we get the following code for the bot, which in response to any message from the user sends him a message "Message text" with a keyboard.*
```Python3 
from quanario.bot import *


def send_keyboard(bot: Bot, message: Message, args: tuple = None):
    keyboard = bot.create_keyboard(inline=False,
                                   one_time=False)
    keyboard.add_button(text="PRIMARY",
                        button_type=VkKeyboardButton.DEFAULT, 
                        color=VkKeyboardColor.PRIMARY)
    keyboard.add_button(text="SECONDARY",
                        button_type=VkKeyboardButton.DEFAULT,
                        color=VkKeyboardColor.SECONDARY)
    keyboard.add_button(text="POSITIVE",
                        button_type=VkKeyboardButton.DEFAULT,
                        color=VkKeyboardColor.POSITIVE)
    keyboard.add_button(text="NEGATIVE",
                        button_type=VkKeyboardButton.DEFAULT,
                        color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button(text="Open this link",  
                        button_type=VkKeyboardButton.OPENLINK, 
                        payload="https://www.google.ru")
    keyboard.add_line()
    keyboard.add_button(button_type=VkKeyboardButton.LOCATION)
    bot.send.message(user_id=message.user_id,
                 message="Message text",
                 keyboard=keyboard)

TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

bot = Bot(token=TOKEN, app_id=APP_ID)
bot.run(init_method=send_keyboard)
```

Ещё одно важное уточнение, максимально, в клавиатуре может быть 10 кнопок, при этом, в ряду должно быть не более 4-х.
>*Another important clarification, as much as possible, there can be 10 buttons in the keyboard, at the same time, there should be no more than 4 in a row.*
---
### P.S. 
Подробнее ознакомиться с работой `клавиатуры` можно [тут](../../quanario/message_extensions/keyboard.py) 
>*You can learn more about the `keyboard` operation [here](../../quanario/message_extensions/keyboard.py)*
