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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `carousel.py` - class that implements the functionality of the `carousel` element. [Learn more.](#message_extensionscarouselpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `keyboard.py` - class that implements the functionality of the `keyboard` element. [Learn more.](#message_extensionskeyboardpy)  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `input_message`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `message.py` - main class for processing messages from the user, including attachments. [Learn more.](#input_messagemessagepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `voice.py` - class for working with attachments of the `voice message` type. [Learn more.](#input_messagevoicepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `audio.py` - class for working with attachments of the `audio` or `music` types. [Learn more.](#input_messageaudiopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `photo.py` - class for working with attachments of the `photo` type. [Learn more.](#input_messagephotopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `video.py` - class for working with attachments of the `video` type. [Learn more.](#input_messagevideopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `file.py` - class for working with attachments of the `file` or `document` types. [Learn more.](#input_messagefilepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `geoposition.py` - class for working with attachments of the `geo` type. [Learn more.](#input_messagegeopositionpy)  
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
><details><summary>Class `Carousel` - The main class for creating attachments of the `Carousel` type. The difference between the carousel and ordinary messages is its unusual appearance, the carousel consists of blocks (maximum 10 pcs.), each block has a title, description and picture. Subsequently, it is possible to attach to each block unique keyboard. It is important that the number of buttons matches in all blocks!!!</summary><p>
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
><details><summary>Class `Keyboard` - The keyboard in messengers is a special type of attachment, unlike ordinary text messages, it is a tool for interactive user interaction with a bot. By clicking on the button, the user gives the system various commands: if these are ordinary buttons, then when clicking on them, the user gives the command to send the text to the community that is written on the button (i.e., the typing process is accelerated), if it is a link or a geo-location, then the system performs these actions outside of a conversation with the bot (sends to the site, sends a placemark on the map).</summary><p>
>
>* `add_button()` -
>* `add_line()` -
>* `get_keyboard()` - This is json by mind, but it return in the format of a regular string.
>* `get_empty_keyboard()` - This is json by mind, but it return in the format of a regular string.
>
></p></details>

><details><summary>Enum `VkKeyboardButton`</summary><p>
>
>* `DEFAULT` - 
>* `OPENLINK` - 
>* `CALLBACK` - 
>* `LOCATION` -
>
></p></details>
---
### input_message/message.py
><details><summary>Class `Message`</summary><p>
>
>* `type` - Property for getting the message type.
>* `text` - Property for receiving the text of the message sent by the user.
>* `user_id` - Property for getting the message type.
>* `attachments` - Property for getting a list of attachments.
>* `is_have_attachments()` - Method for getting information about the presence of attachments in a message from a user.
>* `is_voices()` - A method for getting information about the presence of `voice` messages in attachments to a message from a user.
>* `is_audio()` - A method for getting information about the presence of `music` in attachments to a message from a user.
>* `is_photos()` - Method for getting information about the presence of `photos` in attachments to a message from the user.
>* `is_videos()` - Method for getting information about the presence of `video` recordings in attachments to a message from a user.
>* `is_files()` - Method for getting information about the presence of `files` or `documents` in attachments to a message from the user.
>* `is_geo()` - Method for getting information about sending a geo position by the user.
>* `get_voices()` - This method returns a list of instances of the `Voice` class.
>* `get_audios()` - This method returns a list of instances of the `Audio` class.
>* `get_photos()` - This method returns a list of instances of the `Photo` class.
>* `get_videos()` - This method returns a list of instances of the `Video` class.
>* `get_files()` - This method returns a list of instances of the `File` class.
>* `get_geo()` - This method returns a list of instances of the `Geo` class.
>
></p></details>
---
### input_message/voice.py
><details><summary>Class `Voice`</summary><p>
>
>* `id` - Property for getting a unique file identifier.
>* `duration` - Property for getting the duration of an audio file.
>* `url_mp3` - Property for getting a link to download a file in the `.mp3` format.
>* `url_ogg` - Property for getting a link to download a file in the `.ogg` format.
>* `waveform` - Property for getting a graph of file volume changes.
>* `owner_id` - Property for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key` - Property for obtaining an access key, for sending a file to other users.
>* `save_mp3()` - A method for saving a file in the system in `.mp3` format.
>* `save_ogg()` - A method for saving a file in the system in `.ogg` format.
>
></p></details>
---
### input_message/audio.py
><details><summary>Class `Audio`</summary><p>
>
>* `id` - Property for getting a unique file identifier.
>* `title` - Property for getting the name of the audio file.
>* `artist` - Property for getting the artist's name.
>* `date` - Property for getting the file upload date to the `VKontakte` server (in Unix format).
>* `duration` - Property for getting the duration of an audio.
>* `url_mp3` - Property for getting a link to download a file.
>* `is_explicit` - 
>* `is_focus_track` - 
>* `owner_id` - Property for getting the ID of the `user` or `community` who uploaded the file.
>* `track_code` - Property for obtaining an access key, for sending a file to other users.
>* `save_mp3()` - A method for saving a file in the system in `.mp3` format.
>
></p></details>
---
### input_message/photo.py
><details><summary>Class `Photo`</summary><p>
>
>* `id` - Property for getting a unique file identifier.
>* `width` - Property for getting the width of the photo.
>* `height` - Property for getting the height of the photo.
>* `url` - Property for getting a link to download a file.
>* `album_id` - Property for getting the album where the file is placed.
>* `date` - Property for getting the file upload date to the `VKontakte` server (in Unix format).
>* `post_id` - Property for getting the post ID.
>* `owner_id` - Property for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key` - Property for obtaining an access key, for sending a file to other users.
>* `get_attachment()` - Method for getting the file ID string.
>* `save()` - A method for saving a file in the system.
>* *`__get_image` - A private method for finding the highest file resolution.*
>
></p></details>
---
### input_message/video.py
><details><summary>Class `Photo`</summary><p>
>
>* `id` - Property for getting a unique file identifier.
>* `width` - Property for getting the width of the video.
>* `height` - Property for getting the height of the video.
>* `title` - Property for getting the full name of the file.
>* `url` - Property for getting a link to download a file.
>* `date` - Property for getting the file upload date to the `VKontakte` server (in Unix format).
>* `description` - Property for getting a description of the video.
>* `duration` - Property for getting the duration of an video.
>* `views` - Property for getting the number of views of a video recording.
>* `can_edit` - Property for getting the number of views of a video recording.
>* `can_add` - Property for getting information whether the user can record a video to himself.
>* `can_attach_link` - Property for getting information whether a user can attach an action button to a video.
>* `comments` - Property for getting the number of comments on the video.
>* `is_favorite` - Property for getting information about adding an object to bookmarks from the current user.
>* `owner_id` - Property for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key` - Property for obtaining an access key, for sending a file to other users.
>* `get_attachment()` - Method for getting the file ID string.
>
></p></details>
---
### input_message/file.py
><details><summary>Class `Photo`</summary><p>
>
>* `id` - Property for getting a unique file identifier.
>* `type` - Property for getting a unique file ID.
>* `title` - Property for getting the full name of the file.
>* `extension` - Property for getting the file extension, for example: `.png` or `.pdf`.
>* `size` - Property for getting the file size in bytes. (How much space does it take up on disk)
>* `url` - Property for getting a link to download a file.
>* `date` - Property for getting the file upload date to the `VKontakte` server (in Unix format).
>* `owner_id` - Property for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key` - Property for obtaining an access key, for sending a file to other users.
>* `get_attachment` - Method for getting the file ID string.
>* `save` -Method for saving a file in the system.
>
></p></details>
---
### input_message/geoposition.py
><details><summary>Class `Photo`</summary><p>
>
>* `id` - Property for getting the unique identifier of the placemark on the map.
>* `from_id` - Property for getting the unique identifier of the user who sent the tag.
>* `date` - Property for getting the date of sending the geo position.
>* `out` - 
>* `latitude` - Property for getting the geographical `latitude` of the starting point, set in degrees.
>* `longitude` - Property for getting the geographical `longitude` of the starting point, set in degrees.
>* `location_type` - Property for getting the type of the label sent by the user.
>* `title` - Property for getting the location name as a string.
>* `country` - Property for getting the country where the label is located.
>* `city` - Property for getting the city where the label is located.
>
></p></details>
---

### user/user.py
><details><summary>Class `User` - Information about fields from the 'User' section.</summary><p>
>
>* `user_id`: [int]() - Property for getting the user ID.
>* `domain`: [str]() - Property for getting a short page address. A string containing the short address of the page is returned (for example, andrew). If it is not assigned, "id"+user_id is returned, for example, id35828305.
>* `screen_name`: [str]() - Property for getting a short page name.
>* `first_name`: [str]() - Property for getting the user name.
>* `last_name`: [str]() - Property for getting the user's last name.
>* `birthday`: [str]() - Property for getting the user's date of birth, in the format YYYY-MM-DD.
>* `sex`: [Sex](#useruserpy) - Property for getting the user's gender. For more information, see `person_enum.Sex`.
>* `relation`: [Relation](#useruserpy) - Property for getting information about the marital status of the user. For more information, see `person_enum.Relation`.
>* `online`: [Online](#useruserpy) - Property for getting information about whether the user is currently on the site.
>* `count`: Optional[[Counters](#useruserpy)] - Property for getting information about the number of different objects from the user.
>* `occupation` - Property for getting information about user activity.
>* `contacts` - Property for getting information about the user's contact information
>* `interests` - Property for getting information about fields from the `Life position` section
>* `education`: Optional[[Education](#-usereducationeducationpy)] - Property for obtaining educational institutions in which the user studied.
>* `career` - Property for getting a list of schools where the user studied. Array of instances of the `School` class.
>* `military` - Property for getting information about the user's military service.
>* `life_position` - Property for getting information about fields from the `Life position` section.
>* `params` - Property for getting information about additional user fields.
>* `get_json()` - This method generates a json object from the fields of the `User` class.
>* *`__convert_birthdate()` -* 
>* *`__decode_sex()` - This private method converts the numeric representation of the value `sex` to Enum `Sex`.*
>* *`__decode_online()` - This private method converts the numeric representation of the value `online` to Enum `Online`.*
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
### user/carer.py
><details><summary>Class `Career` - Information about fields from the 'Career' section.</summary><p>
>
>* `group_id`: [int](#usercarerpy) - Property for getting the community ID (if available, otherwise company).
>* `company`: [str](#usercarerpy) - Property for getting the company name (if available, otherwise group_id).
>* `city_id`: [str](#usercarerpy) - Everything to get the ids of the city, city (if is available, otherwise city_name).
>* `city_name`: [str](#usercarerpy) - Property for getting the name of the city.
>* `country_id`: [int](#usercarerpy) - Property for getting the country ID.
>* `work_from`: [int](#usercarerpy) - Property for getting the year of the start of work.
>* `work_until`: [int](#usercarerpy) - Property for getting the year of completion of work.
>* `position`: [str](#usercarerpy) - Property for getting the title of the position
>* `get_json()`: [json](#usercarerpy) - This method generates a json object from the fields of the `Career` class.
>
></p></details>
---
### user/contacts.py
><details><summary>Class `Contacts` - Information about fields from the 'Contacts' section.</summary><p>
>
>* `site`: [str](#usercontactspy) - Property for getting the site address specified in the profile.
>* `connections`: [Dict](#usercontactspy)[[str](#usercontactspy), [Any](#usercontactspy)] - Property for getting data about the user's services specified in the profile, such as: skype, livejournal. A separate string field containing the user's nickname is returned for each service. For example, "skype": "username".
>* `home_town`: [str](#usercontactspy) - Property for getting the name of the hometown.
>* `city_id`: [int](#usercontactspy) - Property for getting the user's city ID, which can be used to get it names using the `database` `method.getCitiesById`.
>* `city_name`: [str](#usercontactspy) - Property for getting the name of the city where the user is located.
>* `country_id`: [int](#usercontactspy) - Property for getting the user's country ID, which can be used to get it names using the `database` `method.getCitiesById`.
>* `country_name`: [str](#usercontactspy) - Property for getting the name of the country in which the user is located.
>* `get_json()`: [json](#usercontactspy) - This method generates a json object from the fields of the `Contacts` class.
>
></p></details>
---
### user/counters.py
><details><summary>Class `Counters` - Information about the number of different objects the user has.</summary><p>
>
>* `notes`: [int](#usercounterspy) - Property for getting the number of `notes from the user.
>* `pages`: [int](#usercounterspy) - Property for getting the number of `subscribers from the user.
>* `audios`: [int](#usercounterspy) - Property for getting the number of `audio recordings from the user.
>* `albums`: [int](#usercounterspy) - Property for getting the number of `photo albums from the user.
>* `photos`: [int](#usercounterspy) - Property for getting the number of `photos from the user.
>* `videos`: [int](#usercounterspy) - Property for getting the number of `videos from the user.
>* `user_videos`: [int](#usercounterspy) - Property for getting the number of `videos with user`.
>* `clips_followers`: [int](#usercounterspy) - Property for getting the number of `clips with  user`.
>* `groups`: [int](#usercounterspy) - Property for getting the number of community subscribers from the user.
>* `friends`: [int](#usercounterspy) - Property for getting the number of friends a user has.
>* `followers`: [int](#usercounterspy) - Property for getting the number of `subscribers` from the user.
>* `subscriptions`: [int](#usercounterspy) - Property for getting the number of `subscriptions` from the user.
>* `online_friends`: [int](#usercounterspy) - Property for getting the number of `online friends` of the user.
>* `get_json()`: [json](#usercounterspy) - This method generates a json object from the fields of the `Counters` class.
>
></p></details>
---
### user/interests.py
><details><summary>Class `Interests` - Information about fields from the 'Interests' section.</summary><p>
>
>* `about`: [str](#userinterestspy) - Property for getting the contents of the `About me` field from the profile.
>* `status`: [str](#userinterestspy) - Property for getting user status. Returns a string containing the `status` text located in profile under the name.
>* `activities`: [str](#userinterestspy) - Property for getting the contents of the `Activity` field from the profile.
>* `interests`: [str](#userinterestspy) - Property for getting the contents of the `Interests` field from the profile.
>* `music`: [str](#userinterestspy) - Property for getting the contents of the `Favorite music` field from the profile.
>* `movies`: [str](#userinterestspy) - Property for getting the contents of the `Favorite movies` field from the profile.
>* `tv`: [str](#userinterestspy) - Property for getting the contents of the `Favorite TV shows` field from the profile.
>* `books`: [str](#userinterestspy) - Property for getting the contents of the `Favorite books` field from the profile.
>* `games`: [str](#userinterestspy) - Property for getting the contents of the `Favorite games` field from the profile.
>* `quotes`: [str](#userinterestspy) - Property for getting the contents of the `Favorite quotes` field from the profile.
>* `get_json()`: [json](#userinterestspy) - This method generates a json object from the fields of the 'Interests' class.
>
></p></details>
---
### user/last_seen.py

---
### user/lifeposition.py

---
### user/military.py

---
### user/occupation.py

---
### user/params.py

---
### user/education/education.py

---
### user/education/schools.py

---
### user/education/universities.py


