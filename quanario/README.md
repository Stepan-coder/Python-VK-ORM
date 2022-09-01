# Documentation

## Introduction

&nbsp;&nbsp;&nbsp;&nbsp;In 2019, I wanted to make a chatbot for learning foreign languages, I do not know exactly why, but I really wanted to. But I liked the idea that you can make some kind of resource that is accessed through a messenger. In general, in my opinion, resources should be divided into two types: exclusively `informational` and `design`. For example, I would refer `Wikipedia` or the `library's website` to the `informational` ones, and an `online store`, a website `apple.com` to the `design`. This approach organizes resources according to their purpose.  
&nbsp;&nbsp;&nbsp;&nbsp;To create my own bot, I began to study the Internet for what and how to do. Of course, the first thing I came across was instructions for creating bots in telegram. But only in my opinion `telegram` is already overloaded with all kinds of bots and, unfortunately, does not have the resources to popularize the group ~~with the exception of paid advertising in other groups~~.  
&nbsp;&nbsp;&nbsp;&nbsp;Later, I came across the [vk_api](https://github.com/python273/vk_api) library from `python273`. I liked it for its simplicity and convenience. Having added my own features to the project code, I implemented the project [LinguisticBot](https://vk.com/linguisticbot).  
&nbsp;&nbsp;&nbsp;&nbsp;But as the project developed and scaled, I realized that the current capabilities of the library are not enough and it needs quite serious refinement. Therefore, in the format of a pet project, I decided to bring it to mind! Now, this project is a serious rethinking of the principles of the original library, as well as the appearance of new features: 
- clear `typing`,
- `castomisation`, 
- `asynchrony`, 
- adequate operation of the `keyboard`, 
- the appearance of the `carousel` object, 
- the ability to receive and process `attachments` from the user _(including geo-location)_   
- and much more!
---
## Project structure
|-> `quanario` - root folder of the project.  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `bot.py` - the main class of the module. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `send.py` - class for sending messages and attachments to the user. [Learn more.]()     
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `upload.py` - class for uploading attachments to the `VKontakte` server. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `message_extensions`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `carousel.py` - class that implements the functionality of the `carousel` element. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `keyboard.py` - class that implements the functionality of the `keyboard` element. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `input_message`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `message.py` - main class for processing messages from the user, including attachments. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `voice.py` - class for working with attachments of the `voice message` type. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `audio.py` - class for working with attachments of the `audio` or `music` types. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `photo.py` - class for working with attachments of the `photo` type. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `video.py` - class for working with attachments of the `video` type. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `file.py` - class for working with attachments of the `file` or `document` types. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `geoposition.py` - class for working with attachments of the `geo` type. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `user`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `user.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `carer.py` - class with information about fields from the `Career` section. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `contacts.py` - class with information about fields from the `Contacts` section. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `counters.py` - class with information about the number of different objects the user has. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `interests.py` - class with information about fields from the `Interests` section. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `last_seen.py` - a class with information about the user's last visit. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `lifeposition.py` - class with information about fields from the `Life position` section. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `military.py` - class with information about fields from the `Military` section. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `occupation.py` - class with information about the user's current occupation. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `params.py` - class with information about fields from the `Params` section. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `education`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `education.py` - main class for processing user information about his education. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `schools.py` - class with information about which `schools` the user attended. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `universities.py` - class with information about which `universities` the user attended. [Learn more.]()
---

### bot.py
><details><summary>Class `Bot`</summary><p>
>
>* `TOKEN` - Property for getting a community TOKEN.
>* `APP_ID` - Property for getting a community ID.
>* `vk` - Property for getting the main bot object.
>* `longpoll` - Property for getting a long poll object (needed for interacting with VKontakte servers).
>* `send` - Property for getting an instance of the `Send` class. This class implements the functionality of sending various types of messages to the user.
>* `upload` - Property for getting an instance of the `Upload` class. This class implements the functionality of publishing content on vkontakte server.
>* `run()` - The main method of the `Bot` class. It launches a call to the `init_method` method in an eternal loop to receive and process messages from the user.
>* `get_user_info()` - This method makes a request in VKontakte to get information about the user, in response it receives json, which is converted into an instance of the `User` class.
>* `create_keyboard()` - Static method of the `Bot` class that allows you to get an instance of the `Keyboard` class to create a keyboard.
>* `create_carousel()` - Static method of the `Bot` class that allows you to get an instance of the `Carousel` class to create a carousel.
>* *`__bot_boot()` - A `private` method of the `Bot` class that authorizes the bot in VKontakte.*
>
></p></details>
---
### send.py
><details><summary>Class `Send`</summary><p>
>
>* `message()` - This method allows you to send a message with the text `message` to a user with the id `user_id`, if necessary, it is possible to attach a keyboard with buttons - `keyboard`. For more information about `keyboard`, see the [documentation](message_extensions/keyboard.py).
>* `carousel()` - This method allows you to send a message with the text `message` to a user with the id `user_id`, if necessary, it is possible to attach a carousel - `carousel`. For more information about `carousel`, see the [documentation](message_extensions/carousel.py).
>* `sticker()` - This method allows you to send a `sticker` with the number `sticker_id` to a user with the id `user_id`.
>* `voice()` - This method allows you to send an `audio` file to a user with the id `user_id` as a voice message.
>* `photo()` - This method allows you to send a `photo` to a user with the id `user_id`.
>* `video()` - This method allows you to send `video` file to a user with the id `user_id`.
>* `file()` - This method allows you to send `file` or `document` to a user with the id `user_id`.
>
></p></details>
---
### upload.py
><details><summary>Class `Upload`</summary><p>
>
>* `voice()` - This method allows you to get an `attachment` for an `audio file` to send it to the user.
>* `photo()` - This method allows you to get an `attachment` for an `image` to send it to the user.
>* `file()` - This method allows you to get an `attachment` for the `file` to send it to the user.
>* `convert_audio()` - The `VKontakte` social network has an oddity when sending an `audio file` as a `voice` message - an audio file it must be `single-channel` and in `.ogg` format. This is exactly the problem that this method solves. Important clarification - for the correct operation of this method, the mandatory installation of the `ffmpeg` package is required, as well as add it to the environment variables.
>
></p></details>
---
### message_extensions/carousel.py
><details><summary>Class `Carousel` - The main class for creating attachments of the `Carousel` type. The difference between the carousel and ordinary messages is its unusual appearance, the carousel consists of blocks (maximum 10 pcs.), each block has a title, description and picture. Subsequently, it is possible to attach to each block unique keyboard. !!!It is important that the number of buttons matches in all blocks!!!</summary><p>
>
>* `count` - This property contains the number of elements in the carousel.
>* `last_element` - This property contains the `last element` added to the `carousel`, thereby opening the possibility of its editing, for example, to change the description or change the photo.
>* `add_element()` - This method `creates a new block` for the `carousel` and adds it to the existing ones.
>* `get_carousel` - This method `builds` the entire `carousel`, for later sending it to the user.
>
></p></details>

><details><summary>Class `CarouselElement`</summary><p>
>
>* `title` - This property contains the block header.
>* `title` - The `setter` for the `title` property allows you to set a new value for the property.
>* `description` - This property contains the block description.
>* `description` - The `setter` for the `description` property allows you to set a new value for the property.
>* `attachment` - This property contains a link to the block image.
>* `attachment` - The `setter` for the `attachment` property allows you to set a new value for the property.
>* `keyboard` - This property contains json with buttons for the element.
>* `keyboard` - The `setter` for the `keyboard` property allows you to set a new value for the property.
>* `compile()` - This method performs the `assembly` of the carousel block, for subsequent sending it to the user.
>* *`__check_length()` - This `privat` method shortens the input string to the specified `count` length.*
>* *`__cut_attachment()` - This `private` method allocates a unique image id from the input `attachment`*
>* *`__extract_keyboard_buttons` -*
>
></p></details>
---
### message_extensions/keyboard.py
><details><summary>Enum `VkKeyboardButton`</summary><p>
>
>* `DEFAULT` - 
>* `OPENLINK` - 
>* `CALLBACK` - 
>* `LOCATION` -
>
></p></details>


><details><summary>Class `Keyboard`</summary><p>
>
>* `add_button()` -
>* `add_line()` -
>* `get_keyboard()` - This is json by mind, but it return in the format of a regular string.
>* `get_empty_keyboard()` - This is json by mind, but it return in the format of a regular string.
>
></p></details>
---
### input_message/message.py
---
### input_message/voice.py
---
### input_message/audio.py
---
### input_message/photo.py
---
### input_message/video.py
---
### input_message/file.py
---
### input_message/geoposition.py


