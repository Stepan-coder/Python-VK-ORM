# [Documentation](../) / Input_message


### [message.py](message.py)
><details><summary>Class `Message` - The main class for processing messages received from the user by the bot. Its main task is to represent the received attachments (voice messages, music, photos, videos, geo-positions) in the form of objects with which it is convenient to interact.</summary><p>
>
>* `type`: [VkBotEventType](#messagepy) - _Property_ for getting the message type.
>* `text`: [str](#messagepy) - _Property_ for receiving the text of the message sent by the user.
>* `user_id`: [int](#messagepy) - _Property_ for getting the message type.
>* `attachments`: [Optional](#messagepy)[[Dict](#messagepy)[[str](#messagepy), [Any](#messagepy)]] - _Property_ for getting a list of attachments.
>* `is_have_attachments()`: [bool](#messagepy) - Method for getting information about the presence of attachments in a message from a user.
>* `is_voices()`: [bool](#messagepy) - A method for getting information about the presence of `voice` messages in attachments to a message from a user.
>* `is_audio()`: [bool](#messagepy) - A method for getting information about the presence of `music` in attachments to a message from a user.
>* `is_photos()`: [bool](#messagepy) - Method for getting information about the presence of `photos` in attachments to a message from the user.
>* `is_videos()`: [bool](#messagepy) - Method for getting information about the presence of `video` recordings in attachments to a message from a user.
>* `is_files()`: [bool](#messagepy) - Method for getting information about the presence of `files` or `documents` in attachments to a message from the user.
>* `is_geo()`: [bool](#messagepy) - Method for getting information about sending a geo position by the user.
>* `get_voices()`: [List](#messagepy)[[Voice](#voicepy)] - This method returns a list of instances of the `Voice` class.
>* `get_audios()`: [List](#messagepy)[[Audio](#audiopy)] - This method returns a list of instances of the `Audio` class.
>* `get_photos()`: [List](#messagepy)[[Photo](#photopy)] - This method returns a list of instances of the `Photo` class.
>* `get_videos()`: [List](#messagepy)[[Video](#videopy)] - This method returns a list of instances of the `Video` class.
>* `get_files()`: [List](#messagepy)[[File](#filepy)] - This method returns a list of instances of the `File` class.
>* `get_geo()`: [Geo](#geopositionpy) - This method returns a list of instances of the `Geo` class.
>
></p></details>
---
### [voice.py](voice.py)
><details><summary>Class `Voice` - A class for processing voice messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#voicepy) - _Property_ for getting a unique file identifier.
>* `duration`: [int](#voicepy) - _Property_ for getting the duration of an audio file.
>* `url_mp3`: [str](#voicepy) - _Property_ for getting a link to download a file in the `.mp3` format.
>* `url_ogg`: [str](#voicepy) - _Property_ for getting a link to download a file in the `.ogg` format.
>* `waveform`: [List](#voicepy)[[int](#voicepy)] - _Property_ for getting a graph of file volume changes.
>* `owner_id`: [int](#voicepy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#voicepy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `save_mp3()`: [None](#voicepy) - A method for saving a file in the system in `.mp3` format.
>* `save_ogg()`: [None](#voicepy) - A method for saving a file in the system in `.ogg` format.
>
></p></details>
---
### [audio.py](audio.py)
><details><summary>Class `Audio` - A class for processing audio messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#audiopy) - _Property_ for getting a unique file identifier.
>* `title`: [str](#audiopy) - _Property_ for getting the name of the audio file.
>* `artist`: [str](#audiopy) - _Property_ for getting the artist's name.
>* `date`: [int](#audiopy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `duration`: [int](#audiopy) - _Property_ for getting the duration of an audio.
>* `url_mp3`: [str](#audiopy) - _Property_ for getting a link to download a file.
>* `is_explicit`: [bool](#audiopy) - _Property_ is outdated or undefined.
>* `is_focus_track`: [bool](#audiopy) - _Property_ is outdated or undefined.
>* `owner_id`: [int](#audiopy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `track_code`: [str](#audiopy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `save_mp3()`: [None](#audiopy) - A method for saving a file in the system in `.mp3` format.
>
></p></details>
---
### [photo.py](photo.py)
><details><summary>Class `Photo` - A class for processing photo messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#photopy) - _Property_ for getting a unique file identifier.
>* `width`: [int](#photopy) - _Property_ for getting the width of the photo.
>* `height`: [int](#photopy) - _Property_ for getting the height of the photo.
>* `url`: [str](#photopy) - _Property_ for getting a link to download a file.
>* `album_id`: [int](#photopy) - _Property_ for getting the album where the file is placed.
>* `date`: [int](#photopy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `post_id`: [int](#photopy) - _Property_ for getting the post ID.
>* `owner_id`: [int](#photopy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#photopy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `get_attachment()`: [str](#photopy) - Method for getting the file ID string.
>* `save()`: [None](#photopy) - A method for saving a file in the system.
>* *`__get_image`: [Tuple](#photopy)[[int](#photopy), [int](#photopy), [str](#photopy)] - A private method for finding the highest file resolution.*
>
></p></details>
---
### [video.py](video.py)
><details><summary>Class `Video` - A class for processing video messages sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#videopy) - _Property_ for getting a unique file identifier.
>* `width`: [int](#videopy) - _Property_ for getting the width of the video.
>* `height`: [int](#videopy) - _Property_ for getting the height of the video.
>* `title`: [str](#videopy) - _Property_ for getting the full name of the file.
>* `url`: [str](#videopy) - _Property_ for getting a link to download a file.
>* `date`: [int](#videopy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `description`: [str](#videopy) - _Property_ for getting a description of the video.
>* `duration`: [int](#videopy) - _Property_ for getting the duration of an video.
>* `views`: [tin](#videopy) - _Property_ for getting the number of views of a video recording.
>* `can_edit`: [int](#videopy) - _Property_ for getting the number of views of a video recording.
>* `can_add`: [int](#videopy) - _Property_ for getting information whether the user can record a video to himself.
>* `can_attach_link`: [int](#videopy) - _Property_ for getting information whether a user can attach an action button to a video.
>* `comments`: [int](#videopy) - _Property_ for getting the number of comments on the video.
>* `is_favorite`: [bool](#videopy) - _Property_ for getting information about adding an object to bookmarks from the current user.
>* `owner_id`: [int](#videopy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#videopy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `get_attachment()`: [str](#videopy) - Method for getting the file ID string.
>
></p></details>
---
### [file.py](file.py)
><details><summary>Class `File` - A class for processing files sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#filepy) - _Property_ for getting a unique file identifier.
>* `type`: [int](#filepy) - _Property_ for getting a unique file ID.
>* `title`: [str](#filepy) - _Property_ for getting the full name of the file.
>* `extension`: [str](#filepy) - _Property_ for getting the file extension, for example: `.png` or `.pdf`.
>* `size`: [str](#filepy) - _Property_ for getting the file size in bytes. (How much space does it take up on disk)
>* `url`: [str](#filepy) - _Property_ for getting a link to download a file.
>* `date`: [int](#filepy) - _Property_ for getting the file upload date to the `VKontakte` server (in Unix format).
>* `owner_id`: [int](#filepy) - _Property_ for getting the ID of the `user` or `community` who uploaded the file.
>* `access_key`: [str](#filepy) - _Property_ for obtaining an access key, for sending a file to other users.
>* `get_attachment()`: [str](#filepy) - Method for getting the file ID string.
>* `save()`: [None](#filepy) - Method for saving a file in the system.
>
></p></details>
---
### [geoposition.py](geoposition.py)
><details><summary>Class `Geo` - A class for processing user geoposition sent by a user to a chatbot.</summary><p>
>
>* `id`: [int](#geopositionpy) - _Property_ for getting the unique identifier of the placemark on the map.
>* `from_id`: [int](#geopositionpy) - _Property_ for getting the unique identifier of the user who sent the tag.
>* `date`: [int](#geopositionpy) - _Property_ for getting the date of sending the geo position.
>* `out`: [int](#geopositionpy) - 
>* `latitude`: [float](#geopositionpy) - _Property_ for getting the geographical `latitude` of the starting point, set in degrees.
>* `longitude`: [float](#geopositionpy) - _Property_ for getting the geographical `longitude` of the starting point, set in degrees.
>* `location_type`: [str](#geopositionpy) - _Property_ for getting the type of the label sent by the user.
>* `title`: [str](#geopositionpy) - _Property_ for getting the location name as a string.
>* `country`: [str](#geopositionpy) - _Property_ for getting the country where the label is located.
>* `city`: [str](#geopositionpy) - _Property_ for getting the city where the label is located.
>
></p></details>
