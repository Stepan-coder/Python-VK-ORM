# Работа с геопозицией пользователя (Working with the user's geo location)

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
## Вступление (Introduction)
Геопозиция очень сильный инструмент для работы любого сообщества имеющего физический адрес, т.к. можно направить пользователя к себе в офис или сказать ему, как далеко он находится от того или иного объекта. В этом примере мы рассмотрим простейший пример работы с геопозицией пользователя.
>*Geo-location is a very powerful tool for any community with a physical address, because you can send a user to your office or tell him how far he is from a particular object. In this example, we will look at the simplest example of working with a user's geo-location.*
---
Допустим, мы хотим определить расстояние от пользователя до города Нью-Йорка. Для этого нам надо проверить прислал ли нам какие-нибудь вложения вместе с текстом сообщения, для этого с помощью метода `is_have_attachments()` проверим есть ли вообще вложения. Теперь нам важно понять, вложения от пользователя это карта с геопозицией или что-то другое, для этого воспользуемся методом `is_geo()`. Хорошо, теперь мы уверены, что вложения есть и что в них содержится карта с меткой пользователя. Получим эту метку от пользователя через метод `get_geo()`. У класса `Geo` есть достаточно много свойств, но нам, в этом примере, понадобятся только 2: географическая широта и долгота пользователя. Пока просто выведем их в консоль.
>*Let's say we want to determine the distance from the user to the city of New York. To do this, we need to check whether any attachments have been sent to us along with the message text, to do this, using the `is_have_attachments()` method, we will check if there are any attachments at all. Now it is important for us to understand whether the user's attachments are a map with a geo position or something else, for this we will use the `is_geo()` method. OK, now we are sure that there are attachments and that they contain a map with the user's label. We will get this label from the user via the `get_geo()` method. The `Geo` class has quite a lot of properties, but we, in this example, will need only 2: the geographical latitude and longitude of the user. For now, just output them to the console.*
```Python3
from quanario.bot import *


def geoposition(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():
        if message.is_geo():
            geo = message.get_geo()
            print(geo.longitude)
            print(geo.latitude)

TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

bot = Bot(token=TOKEN, app_id=APP_ID)
bot.run(init_method=geoposition)
```
Теперь, если отправить боту карту, то в консоли вы увидите свои точные географические координаты.
>*Now, if you send a map to the bot, then you will see your exact geographical coordinates in the console.*
---
Для нахождения кратчайшего расстояния между пользователем и Нью-Йорком воспользуемся библиотекой `geopy`, установить её можно командой `pip install geopy`, явно передадим ей географические координаты Нью-Йорка, а вместо вторых координат подставим поля нашего пользователя.
>*To find the shortest distance between the user and New York, we will use the `geopy` library, you can install it with the `pip install geopy` command, explicitly give it the geographical coordinates of New York, and substitute the fields of our user instead of the second coordinates.*
```Python3
from quanario.bot import *
from geopy.distance import geodesic as GD


def geoposition(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():
        if message.is_geo():
            geo = message.get_geo()
            New_York = (40.7128, 74.0060)
            distance = GD(New_York, (geo.longitude, geo.latitude)).km
            print(distance)

TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

bot = Bot(token=TOKEN, app_id=APP_ID)
bot.run(init_method=geoposition)
```
В результате мы получили желаемое расстояние в километрах (для выбора других единиц измерения см. официальную документацию `geopy`). В результате тестирования, у вас могут возникнуть возрадения "Оно работает неправильно!". Но эта библиотека рассчитывает наикратчайшее расстояние (в том числе через северный и южный полюса), поэтому внимательно проверяйте полученные данные! 
>*As a result, we got the desired distance in kilometers (for choosing other units of measurement, see the official documentation `geopy`). As a result of testing, you may have objections "It does not work correctly!". But this library calculates the shortest distance (including through the north and south poles), so check the data carefully!*  
---
### P.S. 
Подробнее ознакомиться с работой `геопозиции` можно [тут](../../quanario/input_message/geoposition.py) 
>*You can learn more about the work of `geo-positioning` [here](../../quanario/input_message/geoposition.py)*