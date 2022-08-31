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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `carer.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `contacts.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `counters.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `interests.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `last_seen.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `lifeposition.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `military.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `occupation.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `params.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `education`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `education.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `schools.py` - main class for processing user information. [Learn more.]()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `universities.py` - main class for processing user information. [Learn more.]()


