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
### Project structure
|-> `quanario` - root folder of the project.  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `bot.py` - the main class of the module. [Learn more.](#botpy)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `send.py` - class for sending messages and attachments to the user. [Learn more.](#sendpy)     
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `upload.py` - class for uploading attachments to the `VKontakte` server. [Learn more.](#uploadpy)  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `message_extensions`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `carousel.py` - class that implements the functionality of the `carousel` element. [Learn more.](#message_extensions--carouselpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `keyboard.py` - class that implements the functionality of the `keyboard` element. [Learn more.](#message_extensions--keyboardpy)  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `input_message`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `message.py` - main class for processing messages from the user, including attachments. [Learn more.](#input_message--messagepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `voice.py` - class for working with attachments of the `voice message` type. [Learn more.](#input_message--voicepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `audio.py` - class for working with attachments of the `audio` or `music` types. [Learn more.](#input_message--audiopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `photo.py` - class for working with attachments of the `photo` type. [Learn more.](#input_message--photopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `video.py` - class for working with attachments of the `video` type. [Learn more.](#input_message--videopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `file.py` - class for working with attachments of the `file` or `document` types. [Learn more.](#input_message--filepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `geoposition.py` - class for working with attachments of the `geo` type. [Learn more.](#input_message--geopositionpy)  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `user`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `user.py` - main class for processing user information. [Learn more.](#user--userpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `career.py` - class with information about fields from the `Career` section. [Learn more.](#user--careerpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `contacts.py` - class with information about fields from the `Contacts` section. [Learn more.](#user--contactspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `counters.py` - class with information about the number of different objects the user has. [Learn more.](#user--counterspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `interests.py` - class with information about fields from the `Interests` section. [Learn more.](#user--interestspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `last_seen.py` - a class with information about the user's last visit. [Learn more.](#user--last_seenpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `lifeposition.py` - class with information about fields from the `Life position` section. [Learn more.](#user--lifepositionpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `military.py` - class with information about fields from the `Military` section. [Learn more.](#user--militarypy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `occupation.py` - class with information about the user's current occupation. [Learn more.](#user--occupationpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `params.py` - class with information about fields from the `Params` section. [Learn more.](#user--paramspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `education`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `education.py` - main class for processing user information about his education. [Learn more.](#user--education--educationpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `schools.py` - class with information about which `schools` the user attended. [Learn more.](#user--education--schoolspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `universities.py` - class with information about which `universities` the user attended. [Learn more.](#user--education--universitiespy)

---

### [bot.py](bot.py)
><details><summary>Class `Bot` -The main class of the library is `quanario`, which combines all the available functions for receiving and sending messages to users.</summary><p>
>
>* `TOKEN`: [str](#botpy) - _Property_ for getting a community TOKEN.
>* `TOKEN`: [None](#botpy) - _Property_ `setter` for getting a community TOKEN.
>* `APP_ID`: [int](#botpy) - _Property_ for getting a community ID.
>* `APP_ID`: [None](#botpy) - _Property_ `setter`  for getting a community ID.
>* `vk`: [vk_api.vk_api.VkApiMethod](#botpy) - _Property_ for getting the main bot object.
>* `longpoll`: [vk_api.bot_longpoll.VkBotLongPoll](#botpy) - _Property_ for getting a long poll object (needed for interacting with VKontakte servers).
>* `send`: [Send](#sendpy) - _Property_ for getting an instance of the `Send` class. This class implements the functionality of sending various types of messages to the user.
>* `upload`: [Upload](#uploadpy) - _Property_ for getting an instance of the `Upload` class. This class implements the functionality of publishing content on vkontakte server.
>* `run()`: [None](#botpy) - The main method of the `Bot` class. It launches a call to the `init_method` method in an eternal loop to receive and process messages from the user.
>* `get_user_info()`: [User](#user--userpy) - This method makes a request in VKontakte to get information about the user, in response it receives json, which is converted into an instance of the `User` class.
>* `create_keyboard()`: [Keyboard](#message_extensions--keyboardpy) - Static method of the `Bot` class that allows you to get an instance of the `Keyboard` class to create a keyboard.
>* `create_carousel()`: [Carousel](#message_extensions--carouselpy) - Static method of the `Bot` class that allows you to get an instance of the `Carousel` class to create a carousel.
>* *`__bot_boot()`: [None](#botpy) - A `private` method of the `Bot` class that authorizes the bot in VKontakte.*
>
></p></details>
---
### [send.py](send.py)
><details><summary>Class `Send` - A class that implements sending media content to users.</summary><p>
>
>* `message()`: [None](#sendpy) - This method allows you to send a message with the text `message` to a user with the id `user_id`, if necessary, it is possible to attach a keyboard with buttons - `keyboard`. For more information about `keyboard`, see the [documentation](message_extensions/keyboard.py).
>* `carousel()`: [None](#sendpy) - This method allows you to send a message with the text `message` to a user with the id `user_id`, if necessary, it is possible to attach a carousel - `carousel`. For more information about `carousel`, see the [documentation](message_extensions/carousel.py).
>* `sticker()`: [None](#sendpy) - This method allows you to send a `sticker` with the number `sticker_id` to a user with the id `user_id`.
>* `voice()`: [None](#sendpy) - This method allows you to send an `audio` file to a user with the id `user_id` as a voice message.
>* `photo()`: [None](#sendpy) - This method allows you to send a `photo` to a user with the id `user_id`.
>* `video()`: [None](#sendpy) - This method allows you to send `video` file to a user with the id `user_id`.
>* `file()`: [None](#sendpy) - This method allows you to send `file` or `document` to a user with the id `user_id`.
>
></p></details>
---
### [upload.py](upload.py)
><details><summary>Class `Upload` - A class that implements uploading media content to servers `VKontakte`, for further sending to users.</summary><p>
>
>* `voice()`: [str](#uploadpy) - This method allows you to get an `attachment` for an `audio file` to send it to the user.
>* `photo()`: [str](#uploadpy) - This method allows you to get an `attachment` for an `image` to send it to the user.
>* `file()`: [str](#uploadpy) - This method allows you to get an `attachment` for the `file` to send it to the user.
>* `convert_audio()`: [str](#uploadpy) - The `VKontakte` social network has an oddity when sending an `audio file` as a `voice` message - an audio file it must be `single-channel` and in `.ogg` format. This is exactly the problem that this method solves. Important clarification - for the correct operation of this method, the mandatory installation of the `ffmpeg` package is required, as well as add it to the environment variables.
>
></p></details>
---
### [message_extensions](message_extensions) / [carousel.py](message_extensions/carousel.py)
><details><summary>Class `Carousel` - The main class for creating attachments of the `Carousel` type. The difference between the carousel and ordinary messages is its unusual appearance, the carousel consists of blocks (maximum 10 pcs.), each block has a title, description and picture. Subsequently, it is possible to attach to each block unique keyboard. It is important that the number of buttons matches in all blocks!!!</summary><p>
>
>* `count`: [int](#message_extensions--carouselpy) - This _Property_ contains the number of elements in the carousel.
>* `last_element`: [CarouselElement](#message_extensions--carouselpy) - This _Property_ contains the `last element` added to the `carousel`, thereby opening the possibility of its editing, for example, to change the description or change the photo.
>* `add_element()`: [None](#message_extensions--carouselpy) - This method `creates a new block` for the `carousel` and adds it to the existing ones.
>* `get_carousel()`: [json](#message_extensions--carouselpy) - This method `builds` the entire `carousel`, for later sending it to the user.
>
></p></details>

><details><summary>Class `CarouselElement` - A class representing a single `carousel' element.</summary><p>
>
>* `title`: [str](#message_extensions--carouselpy) - This _Property_ contains the block header.
>* `title`: [None](#message_extensions--carouselpy) - The `setter` for the `title` _Property_ allows you to set a new value for the _Property_.
>* `description`: [str](#message_extensions--carouselpy) - This _Property_ contains the block description.
>* `description`: [None](#message_extensions--carouselpy) - The `setter` for the `description` _Property_ allows you to set a new value for the _Property_.
>* `attachment`: [str](#message_extensions--carouselpy) - This _Property_ contains a link to the block image.
>* `attachment`: [None](#message_extensions--carouselpy) - The `setter` for the `attachment` _Property_ allows you to set a new value for the _Property_.
>* `keyboard`: [json](#message_extensions--carouselpy) - This _Property_ contains json with buttons for the element.
>* `keyboard`: [None](#message_extensions--carouselpy) - The `setter` for the `keyboard` _Property_ allows you to set a new value for the _Property_.
>* `compile()`: [Dict](#message_extensions--carouselpy)[[str](#message_extensions--carouselpy), [Any](#message_extensions--carouselpy)] - This method performs the `assembly` of the carousel block, for subsequent sending it to the user.
>* *`__check_length()`: [str](#message_extensions--carouselpy) - This `privat` method shortens the input string to the specified `count` length.*
>* *`__cut_attachment()`: [str](#message_extensions--carouselpy) - This `private` method allocates a unique image id from the input `attachment`*
>* *`__extract_keyboard_buttons`: [json](#message_extensions--carouselpy) - This `private` method allows you to prepare the keyboard for adding it to the `carousel` block. It is necessary because the keyboard for the `carousel` cannot contain several buttons `in a row`.*
>
></p></details>
---
### [message_extensions](message_extensions) / [keyboard.py](message_extensions/keyboard.py)
><details><summary>Class `Keyboard` - The keyboard in messengers is a special type of attachment, unlike ordinary text messages, it is a tool for interactive user interaction with a bot. By clicking on the button, the user gives the system various commands: if these are ordinary buttons, then when clicking on them, the user gives the command to send the text to the community that is written on the button (i.e., the typing process is accelerated), if it is a link or a geo-location, then the system performs these actions outside of a conversation with the bot (sends to the site, sends a placemark on the map).</summary><p>
>
>* `add_button()`: [None](#message_extensions--keyboardpy) - This method adds a button with the type `button_type`, the color `color`, the attachment `payload` and the text `text` at the `right`, to the existing keyboard.
>* `add_line()`: [None](#message_extensions--keyboardpy) - This method moves the `cursor` of the buttons one cell down. I.e., by default, the buttons are added to the row, to the right.
>* `get_keyboard()`: [str](#message_extensions--keyboardpy) - This is json by mind, but it return in the format of a regular string.
>* `get_empty_keyboard()`: [str](#message_extensions--keyboardpy) - This is json by mind, but it return in the format of a regular string.
>
></p></details>

><details><summary>Enum `VkKeyboardButton`</summary><p>
>
>* `DEFAULT`
>* `OPENLINK`
>* `CALLBACK`
>* `LOCATION`
>
></p></details>
---
### [input_message](input_message) / [message.py](input_message/message.py)
><details><summary>Class `Message` - The main class for processing messages received from the user by the bot. Its main task is to represent the received attachments (voice messages, music, photos, videos, geo-positions) in the form of objects with which it is convenient to interact.</summary><p>
>
>* `type`: [VkBotEventType](#input_message--messagepy) - _Property_ for getting the message type.
>* `text`: [str](#input_message--messagepy) - _Property_ for receiving the text of the message sent by the user.
>* `user_id`: [int](#input_message--messagepy) - _Property_ for getting the message type.
>* `attachments`: [Optional](#input_message--messagepy)[[Dict](#input_message--messagepy)[[str](#input_message--messagepy), [Any](#input_message--messagepy)]] - _Property_ for getting a list of attachments.
>* `is_have_attachments()`: [bool](#input_message--messagepy) - Method for getting information about the presence of attachments in a message from a user.
>* `is_voices()`: [bool](#input_message--messagepy) - A method for getting information about the presence of `voice` messages in attachments to a message from a user.
>* `is_audio()`: [bool](#input_message--messagepy) - A method for getting information about the presence of `music` in attachments to a message from a user.
>* `is_photos()`: [bool](#input_message--messagepy) - Method for getting information about the presence of `photos` in attachments to a message from the user.
>* `is_videos()`: [bool](#input_message--messagepy) - Method for getting information about the presence of `video` recordings in attachments to a message from a user.
>* `is_files()`: [bool](#input_message--messagepy) - Method for getting information about the presence of `files` or `documents` in attachments to a message from the user.
>* `is_geo()`: [bool](#input_message--messagepy) - Method for getting information about sending a geo position by the user.
>* `get_voices()`: [List](#input_message--messagepy)[[Voice](#input_message--voicepy)] - This method returns a list of instances of the `Voice` class.
>* `get_audios()`: [List](#input_message--messagepy)[[Audio](#input_message--audiopy)] - This method returns a list of instances of the `Audio` class.
>* `get_photos()`: [List](#input_message--messagepy)[[Photo](#input_message--photopy)] - This method returns a list of instances of the `Photo` class.
>* `get_videos()`: [List](#input_message--messagepy)[[Video](#input_message--videopy)] - This method returns a list of instances of the `Video` class.
>* `get_files()`: [List](#input_message--messagepy)[[File](#input_message--filepy)] - This method returns a list of instances of the `File` class.
>* `get_geo()`: [Geo](#input_message--geopositionpy) - This method returns a list of instances of the `Geo` class.
>
></p></details>
---
### [input_message](input_message) / [voice.py](input_message/voice.py)
><details><summary>Class `Voice` - A class for processing voice messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#input_message--voicepy) - _Property_ for getting a unique file identifier.
>* `duration`: [int](#input_message--voicepy) - _Property_ for getting the duration of an audio file.
>* `url_mp3`: [str](#input_message--voicepy) - _Property_ for getting a link to download a file in the `.mp3` format.
>* `url_ogg`: [str](#input_message--voicepy) - _Property_ for getting a link to download a file in the `.ogg` format.
>* `waveform`: [List](#input_message--voicepy)[[int](#input_message--voicepy)] - _Property_ for getting a graph of file volume changes.
>* `owner_id`: [int](#input_message--voicepy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#input_message--voicepy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `save_mp3()`: [None](#input_message--voicepy) - A method for saving a file in the system in `.mp3` format.
>* `save_ogg()`: [None](#input_message--voicepy) - A method for saving a file in the system in `.ogg` format.
>
></p></details>
---
### [input_message](input_message) / [audio.py](input_message/audio.py)
><details><summary>Class `Audio` - A class for processing audio messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#input_message--audiopy) - _Property_ for getting a unique file identifier.
>* `title`: [str](#input_message--audiopy) - _Property_ for getting the name of the audio file.
>* `artist`: [str](#input_message--audiopy) - _Property_ for getting the artist's name.
>* `date`: [int](#input_message--audiopy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `duration`: [int](#input_message--audiopy) - _Property_ for getting the duration of an audio.
>* `url_mp3`: [str](#input_message--audiopy) - _Property_ for getting a link to download a file.
>* `is_explicit`: [bool](#input_message--audiopy) - _Property_ is outdated or undefined.
>* `is_focus_track`: [bool](#input_message--audiopy) - _Property_ is outdated or undefined.
>* `owner_id`: [int](#input_message--audiopy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `track_code`: [str](#input_message--audiopy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `save_mp3()`: [None](#input_message--audiopy) - A method for saving a file in the system in `.mp3` format.
>
></p></details>
---
### [input_message](input_message) / [photo.py](input_message/photo.py)
><details><summary>Class `Photo` - A class for processing photo messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#input_message--photopy) - _Property_ for getting a unique file identifier.
>* `width`: [int](#input_message--photopy) - _Property_ for getting the width of the photo.
>* `height`: [int](#input_message--photopy) - _Property_ for getting the height of the photo.
>* `url`: [str](#input_message--photopy) - _Property_ for getting a link to download a file.
>* `album_id`: [int](#input_message--photopy) - _Property_ for getting the album where the file is placed.
>* `date`: [int](#input_message--photopy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `post_id`: [int](#input_message--photopy) - _Property_ for getting the post ID.
>* `owner_id`: [int](#input_message--photopy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#input_message--photopy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `get_attachment()`: [str](#input_message--photopy) - Method for getting the file ID string.
>* `save()`: [None](#input_message--photopy) - A method for saving a file in the system.
>* *`__get_image`: [Tuple](#input_message--photopy)[[int](#input_message--photopy), [int](#input_message--photopy), [str](#input_message--photopy)] - A private method for finding the highest file resolution.*
>
></p></details>
---
### [input_message](input_message) / [video.py](input_message/video.py)
><details><summary>Class `Video` - A class for processing video messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#input_message--videopy) - _Property_ for getting a unique file identifier.
>* `width`: [int](#input_message--videopy) - _Property_ for getting the width of the video.
>* `height`: [int](#input_message--videopy) - _Property_ for getting the height of the video.
>* `title`: [str](#input_message--videopy) - _Property_ for getting the full name of the file.
>* `url`: [str](#input_message--videopy) - _Property_ for getting a link to download a file.
>* `date`: [int](#input_message--videopy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `description`: [str](#input_message--videopy) - _Property_ for getting a description of the video.
>* `duration`: [int](#input_message--videopy) - _Property_ for getting the duration of an video.
>* `views`: [tin](#input_message--videopy) - _Property_ for getting the number of views of a video recording.
>* `can_edit`: [int](#input_message--videopy) - _Property_ for getting the number of views of a video recording.
>* `can_add`: [int](#input_message--videopy) - _Property_ for getting information whether the user can record a video to himself.
>* `can_attach_link`: [int](#input_message--videopy) - _Property_ for getting information whether a user can attach an action button to a video.
>* `comments`: [int](#input_message--videopy) - _Property_ for getting the number of comments on the video.
>* `is_favorite`: [bool](#input_message--videopy) - _Property_ for getting information about adding an object to bookmarks from the current user.
>* `owner_id`: [int](#input_message--videopy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#input_message--videopy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `get_attachment()`: [str](#input_message--videopy) - Method for getting the file ID string.
>
></p></details>
---
### [input_message](input_message) / [file.py](input_message/file.py)
><details><summary>Class `File` - A class for processing files sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#input_message--filepy) - _Property_ for getting a unique file identifier.
>* `type`: [int](#input_message--filepy) - _Property_ for getting a unique file ID.
>* `title`: [str](#input_message--filepy) - _Property_ for getting the full name of the file.
>* `extension`: [str](#input_message--filepy) - _Property_ for getting the file extension, for example: `.png` or `.pdf`.
>* `size`: [str](#input_message--filepy) - _Property_ for getting the file size in bytes. (How much space does it take up on disk)
>* `url`: [str](#input_message--filepy) - _Property_ for getting a link to download a file.
>* `date`: [int](#input_message--filepy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `owner_id`: [int](#input_message--filepy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#input_message--filepy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `get_attachment()`: [str](#input_message--filepy) - Method for getting the file ID string.
>* `save()`: [None](#input_message--filepy) -Method for saving a file in the system.
>
></p></details>
---
### [input_message](input_message) / [geoposition.py](input_message/geoposition.py)
><details><summary>Class `Geo` - A class for processing user geoposition sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#input_message--geopositionpy) - _Property_ for getting the unique identifier of the placemark on the map.
>* `from_id`: [int](#input_message--geopositionpy) - _Property_ for getting the unique identifier of the user who sent the tag.
>* `date`: [int](#input_message--geopositionpy) - _Property_ for getting the date of sending the geo position.
>* `out`: [int](#input_message--geopositionpy) - 
>* `latitude`: [float](#input_message--geopositionpy) - _Property_ for getting the geographical `latitude` of the starting point, set in degrees.
>* `longitude`: [float](#input_message--geopositionpy) - _Property_ for getting the geographical `longitude` of the starting point, set in degrees.
>* `location_type`: [str](#input_message--geopositionpy) - _Property_ for getting the type of the label sent by the user.
>* `title`: [str](#input_message--geopositionpy) - _Property_ for getting the location name as a string.
>* `country`: [str](#input_message--geopositionpy) - _Property_ for getting the country where the label is located.
>* `city`: [str](#input_message--geopositionpy) - _Property_ for getting the city where the label is located.
>
></p></details>
---

### [user](user) / [user.py](user/user.py)
><details><summary>Class `User` - The main class for presenting information about the user in a convenient format of nested classes containing personal information about his various fields of activity..</summary><p>
>
>* `user_id`: [int](#user--userpy) - _Property_ for getting the user ID.
>* `domain`: [str](#user--userpy) - _Property_ for getting a short page address. A string containing the short address of the page is returned (for example, andrew). If it is not assigned, "id"+user_id is returned, for example, id35828305.
>* `screen_name`: [str](#user--userpy) - _Property_ for getting a short page name.
>* `first_name`: [str](#user--userpy) - _Property_ for getting the user name.
>* `last_name`: [str](#user--userpy) - _Property_ for getting the user's last name.
>* `birthday`: [str](#user--userpy) - _Property_ for getting the user's date of birth, in the format YYYY-MM-DD.
>* `sex`: [Sex](#user--userpy) - _Property_ for getting the user's gender. For more information, see `person_enum.Sex`.
>* `relation`: [Relation](#user--userpy) - _Property_ for getting information about the marital status of the user. For more information, see `person_enum.Relation`.
>* `online`: [Online](#user--userpy) - _Property_ for getting information about whether the user is currently on the site.
>* `count`: [Optional](#user--userpy)[[Counters](#user--counterspy)] - _Property_ for getting information about the number of different objects from the user.
>* `occupation`: [Optional](#user--userpy)[[Occupation](#user--occupationpy)] - _Property_ for getting information about user activity.
>* `contacts`: [Optional](#user--userpy)[[Contacts](#user--contactspy)] - _Property_ for getting information about the user's contact information
>* `interests`: [Optional](#user--userpy)[[Interests](#user--interestspy)] - _Property_ for getting information about fields from the `Life position` section
>* `education`: [Optional](#user--userpy)[[Education](#user--education--educationpy)] - _Property_ for obtaining educational institutions in which the user studied.
>* `career`: [Optional](#user--userpy)[[List](#user--userpy)[[Career](#user--careerpy)]] - _Property_ for getting a list of schools where the user studied. Array of instances of the `School` class.
>* `military`: [Optional](#user--userpy)[[List](#user--userpy)[[Military](#user--militarypy)]] - _Property_ for getting information about the user's military service.
>* `life_position`: [Optional](#user--userpy)[[LifePosition](#user--lifepositionpy)] - _Property_ for getting information about fields from the `Life position` section.
>* `params`: [Optional](#user--userpy)[[Params](#user--paramspy)] - _Property_ for getting information about additional user fields.
>* `get_json()`: [json](#user--userpy) - This method generates a json object from the fields of the `User` class.
>* *`__convert_birthdate()`: [str](#user--userpy) - This private method brings the date of birth of the user received from VKontakte to the standardized form `YYYY-MM-DD`* 
>* *`__decode_sex()`: [Sex](#user--userpy) - This private method converts the numeric representation of the value `sex` to Enum `Sex`.*
>* *`__decode_online()`: [Online](#user--userpy) - This private method converts the numeric representation of the value `online` to Enum `Online`.*
>* *`__decode_relation()`: [Relation](#user--userpy) - This private method converts the numeric representation of the value `relation` to Enum `Relation`.*
>
></p></details>

><details><summary>Enum `Sex`</summary><p>
>
>* `NOT_SPECIFIED`
>* `FEMALE`
>* `MALE`
>
></p></details>

><details><summary>Enum `Relation`</summary><p>
>
>* `NOT_SPECIFIED`
>* `NOT_MARRIED`
>* `HAVE_FRIEND`
>* `ENGAGED`
>* `EVERYTHING_IS_COMPLICATED`
>* `ACTIVE_SEARCH`
>* `IN_LOVE`
>* `CIVIL_MARRIAGE`
> 
></p></details>

><details><summary>Enum `Online`</summary><p>
>
>* `ONLINE`
>* `NOT_ONLINE`
>
></p></details>
---
### [user](user) / [career.py](user/career.py)
><details><summary>Class `Career` - Information about fields from the user 'Career' section.</summary><p>
>
>* `group_id`: [int](#user--careerpy) - _Property_ for getting the community ID (if available, otherwise company).
>* `company`: [str](#user--careerpy) - _Property_ for getting the company name (if available, otherwise group_id).
>* `city_id`: [str](#user--careerpy) - Everything to get the ids of the city, city (if is available, otherwise city_name).
>* `city_name`: [str](#user--careerpy) - _Property_ for getting the name of the city.
>* `country_id`: [int](#user--careerpy) - _Property_ for getting the country ID.
>* `work_from`: [int](#user--careerpy) - _Property_ for getting the year of the start of work.
>* `work_until`: [int](#user--careerpy) - _Property_ for getting the year of completion of work.
>* `position`: [str](#user--careerpy) - _Property_ for getting the title of the position
>* `get_json()`: [json](#user--careerpy) - This method generates a json object from the fields of the `Career` class.
>
></p></details>
---
### [user](user) / [contacts.py](user/contacts.py)
><details><summary>Class `Contacts` - Information about fields from the user 'Contacts' section.</summary><p>
>
>* `site`: [str](#user--contactspy) - _Property_ for getting the site address specified in the profile.
>* `connections`: [Dict](#user--contactspy)[[str](#user--contactspy), [Any](#user--contactspy)] - _Property_ for getting data about the user's services specified in the profile, such as: skype, livejournal. A separate string field containing the user's nickname is returned for each service. For example, "skype": "username".
>* `home_town`: [str](#user--contactspy) - _Property_ for getting the name of the hometown.
>* `city_id`: [int](#user--contactspy) - _Property_ for getting the user's city ID, which can be used to get it names using the `database` `method.getCitiesById`.
>* `city_name`: [str](#user--contactspy) - _Property_ for getting the name of the city where the user is located.
>* `country_id`: [int](#user--contactspy) - _Property_ for getting the user's country ID, which can be used to get it names using the `database` `method.getCitiesById`.
>* `country_name`: [str](#user--contactspy) - _Property_ for getting the name of the country in which the user is located.
>* `get_json()`: [json](#user--contactspy) - This method generates a json object from the fields of the `Contacts` class.
>
></p></details>
---
### [user](user) / [counters.py](user/counters.py)
><details><summary>Class `Counters` - Information about the number of different objects the user has.</summary><p>
>
>* `notes`: [int](#user--counterspy) - _Property_ for getting the number of `notes from the user.
>* `pages`: [int](#user--counterspy) - _Property_ for getting the number of `subscribers from the user.
>* `audios`: [int](#user--counterspy) - _Property_ for getting the number of `audio recordings from the user.
>* `albums`: [int](#user--counterspy) - _Property_ for getting the number of `photo albums from the user.
>* `photos`: [int](#user--counterspy) - _Property_ for getting the number of `photos from the user.
>* `videos`: [int](#user--counterspy) - _Property_ for getting the number of `videos from the user.
>* `user_videos`: [int](#user--counterspy) - _Property_ for getting the number of `videos with user`.
>* `clips_followers`: [int](#user--counterspy) - _Property_ for getting the number of `clips with  user`.
>* `groups`: [int](#user--counterspy) - _Property_ for getting the number of community subscribers from the user.
>* `friends`: [int](#user--counterspy) - _Property_ for getting the number of friends a user has.
>* `followers`: [int](#user--counterspy) - _Property_ for getting the number of `subscribers` from the user.
>* `subscriptions`: [int](#user--counterspy) - _Property_ for getting the number of `subscriptions` from the user.
>* `online_friends`: [int](#user--counterspy) - _Property_ for getting the number of `online friends` of the user.
>* `get_json()`: [json](#user--counterspy) - This method generates a json object from the fields of the `Counters` class.
>
></p></details>
---
### [user](user) / [interests.py](user/interests.py)
><details><summary>Class `Interests` - Information about fields from the user 'Interests' section.</summary><p>
>
>* `about`: [str](#user--interestspy) - _Property_ for getting the contents of the `About me` field from the profile.
>* `status`: [str](#user--interestspy) - _Property_ for getting user status. Returns a string containing the `status` text located in profile under the name.
>* `activities`: [str](#user--interestspy) - _Property_ for getting the contents of the `Activity` field from the profile.
>* `interests`: [str](#user--interestspy) - _Property_ for getting the contents of the `Interests` field from the profile.
>* `music`: [str](#user--interestspy) - _Property_ for getting the contents of the `Favorite music` field from the profile.
>* `movies`: [str](#user--interestspy) - _Property_ for getting the contents of the `Favorite movies` field from the profile.
>* `tv`: [str](#user--interestspy) - _Property_ for getting the contents of the `Favorite TV shows` field from the profile.
>* `books`: [str](#user--interestspy) - _Property_ for getting the contents of the `Favorite books` field from the profile.
>* `games`: [str](#user--interestspy) - _Property_ for getting the contents of the `Favorite games` field from the profile.
>* `quotes`: [str](#user--interestspy) - _Property_ for getting the contents of the `Favorite quotes` field from the profile.
>* `get_json()`: [json](#user--interestspy) - This method generates a json object from the fields of the 'Interests' class.
>
></p></details>
---
### [user](user) / [last_seen.py](user/last_seen.py)
><details><summary>Class `LastSeen` - The time of the user last visit.</summary><p>
>
>* `time`: [datetime](#user--last_seenpy) - _Property_ for getting the number of notes from the user.
>* `platform`: [Platform](#user--last_seenpy) - _Property_ for getting the number of subscribers from the user.
>* `get_json()`: [json](#user--last_seenpy) - This method generates a json object from the fields of the 'LastSeen' class.
>* *`__convert_platform()`: [Platform](#user--last_seenpy) - This private method converts the numeric representation of the value `platform` to Enum `Platform`.*
>
></p></details>

><details><summary>Enum `Platform`</summary><p>
>
>* `MOBILE_SITE`
>* `IPHONE_APP`
>* `IPAD_APP`
>* `ANDROID_APP`
>* `WINPHONE_APP`
>* `WINDOWS10_APP`
>* `FULL_SITE`
>
></p></details>
---
### [user](user) / [lifeposition.py](user/lifeposition.py)
><details><summary>Class `LifePosition` - Information about fields from the user `Life position` section.</summary><p>
>
>* `political`: [Political](#user--lifepositionpy) - _Property_ for getting information from the `Political Preferences` field.
>* `langs`: [List](#user--lifepositionpy)[[str](#user--lifepositionpy)] - _Property_ for getting information from the `Political Preferences` field.
>* `religion`: [str](#user--lifepositionpy) - _Property_ for getting information from the `Worldview` field.
>* `inspired_by`: [str](#user--lifepositionpy) - _Property_ for getting information from the field `Sources of inspiration`.
>* `people_main`: [PeopleMain](#user--lifepositionpy) - _Property_ for getting information from the field `The main thing in people`.
>* `life_main`: [LifeMain](#user--lifepositionpy) - _Property_ for getting information from the `Main thing in life` field.
>* `smoking`: [Position](#user--lifepositionpy) - _Property_ for getting information from the `Smoking Attitude` field.
>* `alcohol`: [Position](#user--lifepositionpy) - _Property_ for getting information from the `Attitude to alcohol` field.
>* `get_json()`: [json](#user--lifepositionpy) - This method generates a json object from the fields of the `LifePosition` class.
>* *`__convert_political()`: [Political](#user--lifepositionpy) - This private method converts the numeric representation of the value `political` to Enum `Political`.*
>* *`__convert_people_main()`: [PeopleMain](#user--lifepositionpy) - This private method converts the numeric representation of the value `people_main` to Enum `PeopleMain`.*
>* *`__convert_life_main()`: [LifeMain](#user--lifepositionpy) - This private method converts the numeric representation of the value `life_main` to Enum `LifeMain`.*
>* *`__convert_position()`: [Position](#user--lifepositionpy) - This private method converts the numeric representation of the value `position` to Enum `Position`.*
>
></p></details>

><details><summary>Enum `Political`</summary><p>
>
>* `COMMUNIST`
>* `SOCIALIST`
>* `MODERATE`
>* `LIBERAL`
>* `CONSERVATIVE`
>* `MONARCHICAL`
>* `ULTRACONSERVATIVE`
>* `INDIFFERENT`
>* `LIBERTARIAN`
>
></p></details>

><details><summary>Enum `PeopleMain`</summary><p>
>
>* `INTELLIGENCE_AND_CREATIVITY`
>* `KINDNESS_AND_HONESTY`
>* `BEAUTY_AND_HEALTH`
>* `POWER_AND_WEALTH`
>* `COURAGE_AND_PERSEVERANCE`
>* `HUMOR_AND_LOVE_OF_LIFE`
>
></p></details>

><details><summary>Enum `LifeMain`</summary><p>
>
>* `FAMILY_AND_CHILDREN`
>* `CAREER_AND_MONEY`
>* `ENTERTAINMENT_AND_RECREATION`
>* `SCIENCE_AND_RESEARCH`
>* `IMPROVING_THE_WORLD`
>* `SELF_DEVELOPMENT`
>* `BEAUTY_AND_ART`
>* `FAME_AND_INFLUENCE`
>
></p></details>

><details><summary>Enum `Position`</summary><p>
>
>* `SHARPLY_NEGATIVE`
>* `NEGATIVE`
>* `COMPROMISE`
>* `NEUTRAL`
>* `POSITIVE`
>
></p></details>
---
### [user](user) / [military.py](user/military.py)
><details><summary>Class `Military` - Information about fields from the user 'Military' section.</summary><p>
>
>* `unit`: [str](#user--militarypy) - _Property_ for getting the number of a military unit.
>* `unit_id`: [int](#user--militarypy) - _Property_ for getting the part ID in the database.
>* `country_id`: [int](#user--militarypy) - _Property_ for getting the ID of the country where the part is located.
>* `military_from`: [int](#user--militarypy) - _Property_ for getting the year of service start.
>* `military_until`: [int](#user--militarypy) - _Property_ for getting the end of service year.
>* `get_json()`: [json](#user--militarypy) - This method generates a json object from the fields of the `Military` class.
>
></p></details>
---
### [user](user) / [occupation.py](user/occupation.py) 
><details><summary>Class `Occupation` - Information about the user's current occupation.</summary><p>
>
>* `id`: [int](#user--occupationpy) - _Property_ for getting the activity ID.
>* `name`: [str](#user--occupationpy) - _Property_ for getting the name of the activity.
>* `type`: [OccupationType](#user--occupationpy) - _Property_ for getting the type of activity.
>* `get_json()`: [json](#user--occupationpy) - This method generates a json object from the fields of the `Occupation` class.
>* `__convert_occupation_type()`: [OccupationType](#user--occupationpy) - This private method converts the numeric representation of the value `occupation_type` to Enum `Platform`.
>
></p></details>

><details><summary>Enum `OccupationType`</summary><p>
>
>* `WORK`
>* `SCHOOL`
>* `UNIVERSITY`
>
></p></details>
---
### [user](user) / [params.py](user/params.py)
><details><summary>Class `Params` - Information about fields from the user `Params` section.</summary><p>
>
>* `can_access_closed`: [bool](#user--paramspy)  - _Property_ for getting information about the user's ability to see the profile when is_closed = 1 (for example, he is in friends).
>* `is_closed`: [bool](#user--paramspy) - _Property_ for getting information about whether the user's profile is hidden by privacy settings.
>* `has_mobile`: [bool](#user--paramspy) - _Property_ for getting information about whether the user's mobile phone number is known.
>* `has_photo`: [bool](#user--paramspy) - _Property_ for getting information about whether the user has set a profile photo.
>* `is_no_index`: [bool](#user--paramspy) - _Property_ for getting information about whether the profile is indexed by search sites.
>* `is_trending`: [bool](#user--paramspy) - _Property_ for getting information about whether the profile is indexed by search sites.
>* `is_verified`: [bool](#user--paramspy) - _Property_ for getting information about whether the user's page has been verified.
>* `is_wall_privat`: [bool](#user--paramspy) - _Property_ for getting information about whether the user's page is open.
>* `timezone`: [str](#user--paramspy) - _Property_ for getting information about the user's time zone.
>* `last_seen`: [Optional](#user--paramspy)[[LastSeen](#user--last_seenpy)] - _Property_ for getting information about the user's last visit.
>* `get_json()`: [json](#user--paramspy) - This method generates a json object from the fields of the `Params` class.
>
></p></details>
---
### [user](user) / [education](user/education) / [education.py](user/education/education.py)
><details><summary>Class `Education` - Information about fields from the user `Education` section.</summary><p>
>
>* `schools`: [Optional](#user--education--educationpy)[[List](#user--education--educationpy)[[School](#user--education--schoolspy)]] - _Property_ for getting a list of schools where the user studied. Array of instances of the `School` class.
>* `universities`: [Optional](#user--education--educationpy)[[List](#user--education--educationpy)[[University](#user--education--universitiespy)]]  - _Property_ for getting a list of universities where the user studied. Array of instances of the `University` class.
>
></p></details>
---
### [user](user) / [education](user/education) / [schools.py](user/education/schools.py)
><details><summary>Class `School` - Information about fields from the user `School` section.</summary><p>
>
>* `id`: [int](#user--education--schoolspy) - _Property_ for getting the school ID.
>* `name`: [str](#user--education--schoolspy) - _Property_ for getting the name of the school.
>* `city`: [int](#user--education--schoolspy) - _Property_ for getting the ID of the city where the school is located.
>* `country`: [int](#user--education--schoolspy) - _Property_ for getting the ID of the country where the school is located.
>* `year_from`: [int](#user--education--schoolspy) - _Property_ for getting the year of starting school.
>* `year_to`: [int](#user--education--schoolspy) - _Property_ for getting the year of graduation from school.
>* `year_graduated`: [int](#user--education--schoolspy) - _Property_ for getting the year of graduation from school.
>* `school_class`: [str](#user--education--schoolspy) - _Property_ for getting a class letter.
>* `speciality`: [str](#user--education--schoolspy) - _Property_ for getting a class specialization at school.
>* `school_type`: [SchoolType](#user--education--schoolspy) - _Property_ for getting the school ID.
>* `get_json()`: [json](#user--education--schoolspy) - This method generates a json object from the fields of the `School` class.
>* *`__convert_school_type()`: [SchoolType](#user--education--schoolspy) - This private method converts the numeric representation of the value `school_type` to Enum `SchoolType`.*
>
></p></details>

><details><summary>Enum `SchoolType`</summary><p>
>
>* `SCHOOL` 
>* `GYMNASIUM`
>* `LYCEUM`
>* `BOARDING_SCHOOL`
>* `EVENING_SCHOOL` 
>* `MUSIC_SCHOOL`
>* `SPORTS_SCHOOL`
>* `ART_SCHOOL`
>* `COLLAGE`
>* `PROFESSIONAL_LYCEUM`
>* `TECHNICAL_SCHOOL`
>* `VOCATIONAL_SCHOOL`
>* `UCHILISHE`
>* `SCHOOL_OF_ARTS`
>
></p></details>
---
### [user](user) / [education](user/education) / [universities.py](user/education/universities.py)
><details><summary>Class `University` - Information about fields from the user `University` section.</summary><p>
>
>* `id`: [int](#user--education--universitiespy) - _Property_ for getting the university ID.
>* `name`: [str](#user--education--universitiespy) - _Property_ for getting the name of the university.
>* `city`: [int](#user--education--universitiespy) - _Property_ for getting the ID of the city where the university is located.
>* `country`: [int](#user--education--universitiespy) - _Property_ for obtaining the ID of the country in which the university is located.
>* `faculty_id`: [int](#user--education--universitiespy) - _Property_ for getting the faculty ID.
>* `faculty_name`: [str](#user--education--universitiespy) - _Property_ for getting the name of the faculty.
>* `chair_id`: [int](#user--education--universitiespy) - _Property_ for getting the department ID.
>* `chair_name`: [str](#user--education--universitiespy) - _Property_ for getting the name of the department.
>* `graduation`: [int](#user--education--universitiespy) - _Property_ for getting the end year.
>* `education_form`: [str](#user--education--universitiespy) - _Property_ for obtaining a form of training.
>* `education_status`: [str](#user--education--universitiespy) - _Property_ for getting the training status.
>* `get_json()`: [json](#user--education--universitiespy) - This method generates a json object from the fields of the `School` class.
>
></p></details>