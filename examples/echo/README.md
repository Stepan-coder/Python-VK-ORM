# Создание эхо бота (Creating an echo bot)

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
### Текст (Text)
Для создания простейшего так называемого эхо-бота, нам нужно отправить пользователю тот же текст, что он отправил нам. Для этого, получаем строку от пользователя через свойство `text` класса `message`. И через метод `message` отправляем сообщение пользователю с `id` равным `user_id` класса `message` и текстом `message.text`. Пример можно посмотреть [здесь](text.py).
>*To create the simplest so-called echo bot, you need to send the user the same text that he sent to us. To do this, we get a string from the user through the `text` property of the `message` class. And through the `message` method, we send a message to the user with an `id` equal to the `user_id` of the `message` class and the text `message.text`. An example can be viewed [here](text.py).*
```Python3
def echo_text(bot: Bot, message: Message, args: tuple = None):
    bot.send.message(user_id=message.user_id, 
                     message=message.text)
```
---
### Изображение (Image)
Идём дальше, теперь задача сложнее, надо отправить пользователю картинку, которую он нам прислал. Поэтому, для начала проверим, прислал ли нам пользователь какое-нибудь вложение (картинку, видео, файл, голосовое сообщение), сделать это можно через вызов метода `is_have_attachments()`. Хорошо, мы убедились, что вложения всё-таки есть, но так как пока мы хотим работать только с изображениями, надо проверить есть ли они во вложениях, проверим с помощью метода `is_photos()`. Получим список вложений типа `картинка` через `get_photos()`. Пройдёмся по нему циклом, сохраним изображения и загрузим их на сервера `Вконтакте`, в ответ получим идентификаторы, которые используем для отправки пользователю картинок. Отправляем пользователю картинки вызовом метода `bot.send.photo()`. Пример можно посмотреть [здесь](photo.py).
>*Let's move on, now the task is more complicated, we need to send the user the picture that he sent us. Therefore, first of all, let's check if the user has sent us any attachment (picture, video, file, voice message), this can be done by calling the `is_have_attachments()` method. Well, we made sure that there are attachments after all, but since we want to work only with images so far, we need to check if they are in the attachments, we will check using the `is_photos()` method. We will get a list of attachments of the `picture` type via `get_photos()`. Let's cycle through it, save the images and upload them to the servers `Vkontakte`, in response we will receive identifiers that we use to send images to the user. We send images to the user by calling the `bot.send' method.photo()`. An example can be viewed [here](photo.py).*
```Python3
def echo_photo(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments(): 
        if message.is_photos():
            attachments = []
            for photo in message.get_photos():
                path_to_photo = os.path.join(os.getcwd(), f"{photo.id}.png") 
                photo.save(path_to_save=path_to_photo)
                attachments.append(bot.upload.photo(user_id=message.user_id, path_to_photo=path_to_photo))
            bot.send.photo(user_id=message.user_id,
                           attachment=attachments)
```
---
### Файл (File)
С отправкой файлов всё обстоит точно так же. Проверили что есть вложения, проверили, что это именно файлы, скачали, залили на сервер `Вконтакте`, отправили пользователю. Смотрим! Пример можно посмотреть [здесь](file.py).
>*Everything is exactly the same with sending files. We checked that there are attachments, checked that these are files, downloaded them, uploaded them to the Vkontakte server, and sent them to the user. We are looking! An example can be viewed [here](file.py).*
```Python3
def echo_file(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():
        if message.is_files():
            attachments = []
            for file in message.get_files():
                path = os.path.join(os.getcwd(), f"{file.id}.{file.extension}")
                file.save(path_to_save=path)
                attachments.append(bot.upload.file(user_id=message.user_id, path_to_file=path))
            bot.send.file(user_id=message.user_id,
                          attachment=attachments)
```
---
### Голосовое сообщение|Аудио файл (Voice message|Audio file)
При работе с голосовыми сообщениями и аудиофайлами могут возникнуть некоторые трудности. Важно понять, что **голосовые сообщения и аудиофайлы это кардинально разные сущности!**. Для проверки наличия и получения голосовых сообщений, вы можете воспользоваться методами `is_voices()` и `get_voices()`, а для их скачивания в формате `.mp3` и `.ogg` методами `save_mp3()` и `save_ogg()` соответственно. Для аудиофайлов, следует воспользоваться теми же методами, которые предназначены для обычных файлов. Но загрузка на сервер `ВКонтакте` голосового сообщения и аудиофайла производится одним и тем же методом `bot.upload.voice()`, так же, абсолютно одинаково производится и отправка пользователю, через метод `bot.send.voice()`.  Пример можно посмотреть [здесь](audio.py).
>*There may be some difficulties when working with voice messages and audio files. It is important to understand that **voice messages and audio files are fundamentally different entities!**. To check for and receive voice messages, you can use the `is_voices()' methods`and `get_voices()`, and for downloading them in `.mp3` and `.ogg` format using 'save_mp3()' methods` and `save_ogg()` accordingly. For audio files, you should use the same methods that are intended for regular files. But uploading a voice message and an audio file to the VKontakte server is done using the same `bot.upload' method.voice()` is also sent to the user in exactly the same way, via the `bot.send` `method.voice()`. An example can be viewed [here](audio.py).*
```Python3
def echo_voice_audio(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments():
        if message.is_voices(): 
            attachments = []
            for voice in message.get_voices(): 
                path = os.path.join(os.getcwd(), f"{voice.id}.ogg")
                # voice.save_mp3(path_to_save=path)
                voice.save_ogg(path_to_save=path)
                attachments.append(bot.upload.voice(user_id=message.user_id, path_to_voice=path))
            bot.send.voice(user_id=message.user_id,
                           attachment=attachments)
```
---
### Видео (Video)
~~Вот мы и добрались до сомого интересного~~. Так получилось, что `ВКонтакте` запретили загружать видео на свою платформу от лица сообщества, т.е. от чат-ботов тоже. _Но есть один лайфхак_, для того, чтобы использовать видео в своих целях, можно его отправить боту и получить для него уже готовый `attachment`. А дальше использовать его как угодно:) Пробуем! Пример можно посмотреть [здесь](video.py)
>*~~So we got to the most interesting~~. It so happened that VKontakte was banned from uploading videos to its platform on behalf of the community, i.e. from chatbots too. _No there is one life hack_, in order to use the video for your own purposes, you can send it to the bot and get a ready-made `attachment' for it. And then use it as you like :) We're trying! An example can be viewed [here](video.py)*
```Python3
def echo_video(bot: Bot, message: Message, args: tuple = None):
    if message.is_have_attachments(): 
        if message.is_videos():
            attachments = []
            for video in message.get_videos():  
                attachments.append(video.get_attachment())
            bot.send.video(user_id=message.user_id,
                           attachment=attachments) 
```
---
## Заключение (Conclusion)
В этом примере у нас получилось реализовать различных эхо-ботов, которые могут получать, сохранять и пересылать пользователю его же сообщения. Конечно, непосредственно сами эхо-боты бесполезны, но они показывают возможности библиотеки и примеры их реализации. Впоследствии, вы можете сами модифицировать эти примеры под свои нужды:)
>*In this example, we managed to implement various echo bots that can receive, save and forward messages to the user. Of course, the echo bots themselves are useless, but they show the library's capabilities and examples of their implementation. Afterwards, you can modify these examples yourself to suit your needs:)*