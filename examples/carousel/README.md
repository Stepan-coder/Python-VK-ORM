# Отправка карусели пользователю (Sending the keyboard to the user)

Для начала, создадим шаблон кода для реализации бота в социальной сети `Вконтакте`. Для этого, импортируем библиотеку `quanario`, создадим экземпляр класса `Bot` и передадим ему токен и идентификатор сообщества для авторизации. *(Подробнее об авторизации в оффициальной документации ВКонтакте)* Далее, в аргументе `init_method` метода `run` передаём название метода, который хотим сделать вызываемым при каждом сообщении полученном от пользователя. Шаблон для бота готов!

> *To begin with, let's create a code template for implementing a bot on the Vkontakte social network. To do this, import the `quanario` library, create an instance of the `Bot` class and give it a token and a community identifier for authorization. *((For more information about authorization in the official documentation of VKontakte)* Next, in the `init_method` argument of the `run` method, we pass the name of the method that we want to make called with each message received from the user. The template for the bot is ready!*
```Python3
from quanario.bot import *


def send_carousel(bot: Bot, message: Message, args: tuple = None):
    pass

TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

bot = Bot(token=TOKEN, app_id=APP_ID)
bot.run(init_method=send_carousel)
```
---
Карусель - это новый формат взаимодействия пользователя с ботом, представленный компанией `ВКонтакте`. Карусель состоит из нескольких карточек состоящих из: картинки, заголовка карточки, описания карточки и кнопок клавиатуры. Для отправки карусели пользователю, её необходимо сгенерировать. Для этого вызовем метод `create_carousel()` экземпляра класса `bot`.
>*Carousel is a new format of user interaction with a bot, presented by `VKontakte`. The carousel consists of several cards consisting of: picture, card title, card description and keyboard buttons. To send a carousel to the user, it must be generated. To do this, call the `create_carousel()` method of an instance of the `bot` class.*
```Python3
def send_carousel(bot: Bot, message: Message, args: tuple = None):
    carousel = bot.create_carousel()
```
---
Теперь, когда экземпляр карусели получен, можем перейти к добавлению карточек в неё. Каждая карточка добавляется и настраивается отдельно. **Всего, в одной карусели, максимально может быть не более 10 карточек**!
>*Now that an instance of the carousel has been received, we can proceed to adding cards to it. Each card is added and configured separately. **In total, there can be no more than 10 cards in one carousel**!*
#### Клавиатура (Keyboard)
Клавиатура для карточек карусели не является обязательной, но это крайне удобное место для размещения кнопок, т.к. пользователь наглядно может увидеть продукт/товар/услугу, на которую он соглашается. (Подробнее о клавиатурах см. Клавиатура). Но есть одно важное замечание - **количество кнопок во всех карточках обязательно должно быть одинаковым, либо не быть вообще**.
>*A keyboard for carousel cards is not mandatory, but it is an extremely convenient place to place buttons, because the user can clearly see the product / product / service to which he agrees. (For more information about keyboards, see Keyboard). But there is one important note - **the number of buttons in all cards must necessarily be the same, or not at all**.*
```Python3
    card_keyboard = bot.create_keyboard()
    card_keyboard.add_button(text="PRIMARY",
                             button_type=VkKeyboardButton.DEFAULT,
                             color=VkKeyboardColor.PRIMARY)
    card_keyboard.add_button(text="Open google.com",
                             button_type=VkKeyboardButton.OPENLINK,
                             payload="https://www.google.ru")
    card_keyboard.add_line()
    card_keyboard.add_button(button_type=VkKeyboardButton.LOCATION)
```

Если с заголовком карточки, её описанием и клавиатурой, в целом всё понятно, то с прикреплением картинки могут возникнуть вопросы. Как её прикрепить? И куда её прикреплять? Ответ простой: напрямую - никак! Аргумент `attachment` метода `add_element()` ожидает получить строку-идентификатор изображения, она присылается `API ВКонтакте` в ответ на загрузку картинки на их сервер. Поэтому для прикрепления изображения, необходимо воспользоваться встроенным в библиотеку функционалом `bot.upload.photo()`, куда необходимо передать путь до картинки, а также уникальный идентификатор пользователя ВКонтакте кому необходимо отправить её.  
*Уточнение, такой подход кажется бессмысленным на первый взгляд: зачем разделять загрузку картинок от функционала, который это использует?*  
**Ответ простой - зачастую картинки в диалогах с ботом часто повторяются, а следовательно их проще 1 раз загрузить и больше не тратить на это время**.
>*If everything is clear with the title of the card, its description and the keyboard, then questions may arise with the attachment of the picture. How to attach it? And where to attach it? The answer is simple - no way directly! The `attachment` argument of the `add_element()` method expects to receive an image ID string, it is sent to the `API VKontakte` in response to uploading the image to their server. Therefore, to attach an image, you need to use the built-in library functionality `bot.upload.photo()`, where you need to pass the path to the image, as well as the unique identifier of the VKontakte user to whom you need to send it.  
 *Clarification, this approach seems pointless at first glance: why separate the loading of images from the functionality that uses it?  
 **The answer is simple - often the pictures in the dialogues with the bot are often repeated, and therefore it is easier to download them 1 time and not waste any more time on it**.*
```Python3
    carousel.add_element(title="Card №1 title", 
                         description="Card №1 description", 
                         attachment=bot.upload.photo(user_id=message.user_id,
                                                     path_to_photo="image.png"),
                         keyboard=card_keyboard)
```
По аналогии примера выше, можно добавить в карусель до 10 карточек, с помощью метода `add_element()`...
>*By analogy with the example above, you can add up to 10 cards to the carousel using the `add_element()` method...*
---
Для отправки пользователю клавиатуры, её экземпляр необходимо передать в качестве аргумента методу `carousel`.
>*To send the keyboard to the user, its instance must be passed as an argument to the `carousel` method.*
```Python3  
    bot.send.carousel(user_id=message.user_id,
                      message="It's carousel", 
                      carousel=carousel)
```
---
По итогу получаем следующий код для бота, который в ответ на любое сообщение пользователя отправляет ему сообщение "It's carousel" и карусель состоящую из одной карточки.
>*As a result, we get the following code for the bot, which in response to any message from the user sends him a message "It's carousel" and a carousel consisting of one card.*
```Python3 
def send_carousel(bot: Bot, message: Message, args: tuple = None):
    carousel = bot.create_carousel()
    
    card_keyboard = bot.create_keyboard()
    card_keyboard.add_button(text="PRIMARY",
                             button_type=VkKeyboardButton.DEFAULT,
                             color=VkKeyboardColor.PRIMARY)
    card_keyboard.add_button(text="Open google.com",
                             button_type=VkKeyboardButton.OPENLINK,
                             payload="https://www.google.ru")
    card_keyboard.add_button(button_type=VkKeyboardButton.LOCATION)

    carousel.add_element(title="Card №1 title",
                         description="Card №1 description", 
                         attachment=bot.upload.photo(user_id=message.user_id,
                                                     path_to_photo="image.png"),
                         keyboard=card_keyboard)

    bot.send.carousel(user_id=message.user_id,
                      message="It's carousel", 
                      carousel=carousel)


TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

bot = Bot(token=TOKEN, app_id=APP_ID)
bot.run(init_method=send_carousel)
```
---
### P.S. 
Подробнее ознакомиться с работой `карусели` можно [тут](../../quanario/message_extensions/carousel.py) 
>*You can learn more about the work of the `carousel` [here](../../quanario/message_extensions/carousel.py)*