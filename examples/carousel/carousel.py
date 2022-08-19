from quanario.bot import *


def send_carousel(bot: Bot, message: Message, args: tuple = None):
    # :ru Карусель - это новый формат взаимодействия пользователя с ботом, представленный компанией `ВКонтакте`.
    #  Карусель состоит из нескольких карточек состоящих из: картинки, заголовка карточки, описания карточки и кнопок
    #  клавиатуры.  Для отправки карусели пользователю, её необходимо сгенерировать. Для этого вызовем метод
    #  `create_carousel()` экземпляра класса `bot`.

    # :en Carousel is a new format of user interaction with a bot, presented by `VKontakte`. The carousel consists of
    #  several cards consisting of: picture, card title, card description and keyboard buttons. To send a carousel to
    #  the user, it must be generated. To do this, call the `create_carousel()` method of an instance of the `bot`
    #  class.

    carousel = bot.create_carousel()

    # :ru Клавиатура для карточек карусели не является обязательной, но это крайне удобное место для размещения кнопок,
    #  т.к. пользователь наглядно может увидеть продукт/товар/услугу, на которую он соглашается.
    #  (Подробнее о клавиатурах см. Клавиатура). Но есть одно важное замечание - количество кнопок во всех карточках
    #  обязательно должно быть одинаковым, либо не быть вообще.

    # :en A keyboard for carousel cards is not mandatory, but it is an extremely convenient place to place buttons,
    #  because the user can clearly see the product / product / service to which he agrees.
    #  (For more information about keyboards, see Keyboard). But there is one important note - the number of buttons in
    #  all cards must necessarily be the same, or not at all.

    card_keyboard = bot.create_keyboard()
    card_keyboard.add_button(text="PRIMARY",
                             button_type=VkKeyboardButton.DEFAULT,
                             color=VkKeyboardColor.PRIMARY)
    card_keyboard.add_button(text="Open google.com",
                             button_type=VkKeyboardButton.OPENLINK,
                             payload="https://www.google.ru")
    card_keyboard.add_line()
    card_keyboard.add_button(button_type=VkKeyboardButton.LOCATION)

    # :ru Если с заголовком карточки, её описанием и клавиатурой, в целом всё понятно, то с прикреплением картинки могут
    #  возникнуть вопросы. Как её прикрепить? И куда её прикреплять? Ответ простой - напрямую никак!
    #  Аргумент `attachment` метода `add_element()` ожидает получить строку-идентификатор изображения, она присылается
    #  `API ВКонтакте` в ответ на загрузку картинки на их сервер. Поэтому для прикрепления изображения, необходимо
    #  воспользоваться встроенным в библиотеку функционалом `bot.upload.photo()`, куда необходимо передать путь до
    #  картинки, а также уникальный идентификатор пользователя ВКонтакте кому необходимо отправить её.
    #  Уточнение, такой подход кажется бессмысленным на первый взгляд: зачем разделять загрузку картинок от функционала,
    #  который это использует? Ответ простой - зачастую картинки в диалогах с ботом часто повторяются, а следовательно
    #  их проще 1 раз загрузить и больше не тратить на это время.

    # :en If everything is clear with the title of the card, its description and the keyboard, then questions may arise
    #  with the attachment of the picture. How to attach it? And where to attach it? The answer is simple - no way
    #  directly! The `attachment` argument of the `add_element()` method expects to receive an image ID string, it is
    #  sent to the `API VKontakte` in response to uploading the image to their server. Therefore, to attach an image,
    #  you need to use the built-in library functionality `bot.upload.photo()`, where you need to pass the path to the
    #  image, as well as the unique identifier of the VKontakte user to whom you need to send it. Clarification, this
    #  approach seems pointless at first glance: why separate the loading of images from the functionality that uses it?
    #  The answer is simple - often the pictures in the dialogues with the bot are often repeated, and therefore it is
    #  easier to download them 1 time and not waste any more time on it**.*

    carousel.add_element(title="Card №1 title",  # :ru Заголовок карточки, рекомендуемая длина - 30 символов.
                                                 # :en The title of the card, the recommended length is 30 characters.
                         description="Card №1 description",  # :ru Описание карточки, рекомендуемая длина - 80 символов.
                                                             # :en Description of the card, the recommended length is
                                                             #  80 characters.
                         attachment=bot.upload.photo(user_id=message.user_id,  # :ru Добавляем картинку к карточке.
                                                                               # :en Adding a picture to the card.
                                                     path_to_photo="image.png"),
                         keyboard=card_keyboard  # :ru Прикрепляем клавиатуру к карточке
                                                 # :en Attach the keyboard to the card
                         )

    bot.send.carousel(user_id=message.user_id,  # :ru Передаём уникальный идентификатор пользователя
                                                # :en Transmitting a unique user ID
                      message="It's carousel",  # :ru Передаём текст, который хотим отправить
                                                # :en Passing the text we want to send
                      carousel=carousel  # :ru Передаём карусель
                                         # :en Passing the carousel
                      )


TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

# :ru Создаём экземпляр класса Bot, передаём в него полученный токен и идентификатор сообщества
# :en Create an instance of the Bot class, pass the received token and community ID to it
bot = Bot(token=TOKEN, app_id=APP_ID)

# :ru В методе 'run' передаём название метода, который хотим сделать вызываемым при каждом сообщении пользователя
# :en In the 'run' method, we pass the name of the method that we want to make called with each user message
bot.run(init_method=send_carousel)