# Quanario_VK - Module for the development of chatbots in the social network `VKontakte`

## Table of contents

* [Introduction](#introduction)
* [Project structure](#project-structure)
* [Project Installation](#installation)
* [Usage](#usage)
* [Demo](#demo)
* [FAQ](#faq)
* [License](#license)
* [Commerical inquiries](#commerical-inquiries)
* [Further reading](#further-reading)
* [Alternatives](#alternatives)


## Introduction 

&nbsp;&nbsp;&nbsp;&nbsp;In 2019, I wanted to make a chatbot for learning foreign languages, I do not know exactly why, but I really wanted to. But I liked the idea that you can make some kind of resource that is accessed through a messenger. In general, in my opinion, resources should be divided into two types: exclusively `informational` and `design`. For example, I would refer `Wikipedia` or the `library's website` to the `informational` ones, and an `online store`, a website `apple.com` to the `design`. This approach organizes resources according to their purpose.  
&nbsp;&nbsp;&nbsp;&nbsp;To create my own bot, I began to study the Internet for what and how to do. Of course, the first thing I came across was instructions for creating bots in telegram. But only in my opinion `telegram` is already overloaded with all kinds of bots and, unfortunately, does not have the resources to popularize the group ~~with the exception of paid advertising in other groups~~.  
&nbsp;&nbsp;&nbsp;&nbsp;Later, I came across the [vk_api](https://github.com/python273/vk_api) library from `python273`. I liked it for its simplicity and convenience. Having added my own features to the project code, I implemented the project [LinguisticBot](https://vk.me/linguisticbot).  
&nbsp;&nbsp;&nbsp;&nbsp;But as the project developed and scaled, I realized that the current capabilities of the library are not enough and it needs quite serious refinement. Therefore, in the format of a pet project, I decided to bring it to mind! Now, this project is a serious rethinking of the principles of the original library, as well as the appearance of new features: 
- clear `typing`,
- `castomisation`, 
- `asynchrony`, 
- adequate operation of the `keyboard`, 
- the appearance of the `carousel` object, 
- the ability to receive and process `attachments` from the user _(including geo-location)_   
- and much more!
---

## [Project structure](quanario)
 
|->`quanario` - root folder of the project.  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `bot.py` - the main class of the module. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#botpy)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `send.py` - class for sending messages and attachments to the user. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#sendpy)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ `upload.py` - class for uploading attachments to the `VKontakte` server. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#uploadpy)  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `message_extensions`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `carousel.py` - class that implements the functionality of the `carousel` element. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#message_extensions--carouselpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `keyboard.py` - class that implements the functionality of the `keyboard` element. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#message_extensions--keyboardpy)  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `input_message`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `message.py` - main class for processing messages from the user, including attachments. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#input_message--messagepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `voice.py` - class for working with attachments of the `voice message` type. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#input_message--voicepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `audio.py` - class for working with attachments of the `audio` or `music` types. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#input_message--audiopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `photo.py` - class for working with attachments of the `photo` type. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#input_message--photopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `video.py` - class for working with attachments of the `video` type. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#input_message--videopy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `file.py` - class for working with attachments of the `file` or `document` types. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#input_message--filepy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `geoposition.py` - class for working with attachments of the `geo` type. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#input_message--geopositionpy)  
&nbsp;&nbsp;&nbsp;&nbsp; |-> `user`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `user.py` - main class for processing user information. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--userpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `career.py` - class with information about fields from the `Career` section. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--careerpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `contacts.py` - class with information about fields from the `Contacts` section. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--contactspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `counters.py` - class with information about the number of different objects the user has. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--counterspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `interests.py` - class with information about fields from the `Interests` section. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--interestspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `last_seen.py` - a class with information about the user's last visit. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--last_seenpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `lifeposition.py` - class with information about fields from the `Life position` section. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--lifepositionpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `military.py` - class with information about fields from the `Military` section. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--militarypy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `occupation.py` - class with information about the user's current occupation. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--occupationpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `params.py` - class with information about fields from the `Params` section. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--paramspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |-> `education`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `education.py` - main class for processing user information about his education. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--education--educationpy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `schools.py` - class with information about which `schools` the user attended. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--education--schoolspy)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∟ `universities.py` - class with information about which `universities` the user attended. [Learn more.](https://github.com/Stepan-coder/Quanario/tree/master/quanario#user--education--universitiespy)  

---
## **Installation**

Will be soon... But for now, you can just add the `quanario` folder to the root of your project and use it as a regular library.

## **Usage**

To start development, you need to install the module (see the [installation](#installation) section) and import it into your project. An example of the simplest echo bot:

<details><summary>See an example</summary><p>

```Python3
from quanario.bot import *


def send_keyboard(bot: Bot, message: Message, args: tuple = None):
    pass

TOKEN = "*YOUR TOKEN*"
APP_ID = 000000000

bot = Bot(token=TOKEN, app_id=APP_ID)
bot.run(init_method=send_keyboard)
```

</p></details>

You also have the opportunity to get acquainted with other, more complex examples, to do this, follow one of the links below.  
|-> [Echo](examples/echo)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `text` example, click [here](examples/echo/text.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `audio` example, click [here](examples/echo/audio.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `photo` example, click [here](examples/echo/photo.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `video` example, click [here](examples/echo/video.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `file` example, click [here](examples/echo/file.py).  
|-> [Keyboard](examples/keyboard)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `keyboard` example, click [here](examples/keyboard/keyboard.py).  
|-> [Carousel](examples/carousel)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `carousel` example, click [here](examples/carousel/carousel.py).  
|-> [Geoposition](examples/geoposition)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `geoposition` example, click [here](examples/geoposition/geoposition.py). 

## **Demo**

![LinguisticBotLogo](https://sun9-41.userapi.com/impg/GTqw8HgGArjBXm2TYsUhpXSvP0zc6BLwgwahmg/t51vIX4ts2g.jpg?size=2560x2560&quality=95&sign=d82fead7ad72554a5d3eb5a24a4826a6&type=album)

As an example, I can demonstrate the community on VKontakte - [LinguisticBot](https://vk.me/linguisticbot ). This is my community for learning foreign languages for everyone. It implements all the modules of this educational school website. The bot provides 6 types of interactive tasks to increase the user's vocabulary, as well as an audition task. In addition, as an example, a store has been implemented in which you can buy tips and sections with listening. This project has been running nonstop for 2 years. During this period, a huge number of bugs and bugs in the library have been fixed [Quanario_VK](https://github.com/Stepan-coder/Quanario_VK)

## **FAQ**

I'm just launching this project, but if you have any questions, you can always ask in `issues` or in our [telegram](https://t.me/+-awnUbOP1l41MjAy) chat or [VKontakte](https://vk.com/quanario_vk) group.

# **License**

![сс-nc-by-license](https://static.wixstatic.com/media/342407_05e016f9f44240429203c35dfc8df63b~mv2.png/v1/fill/w_563,h_200,al_c,lg_1,q_80/342407_05e016f9f44240429203c35dfc8df63b~mv2.webp)

CC-BY-NC and commercial usage available after agreement with `Quanario_VK` authors.

## **Commerical inquiries**

- Via email - stepan.borodin2016@bk.ru
- Via VK - via this [link](https://vk.com/stepanborodin)
- Via telegram - via this [link](https://t.me/StepanBorodin)

## **Further reading**

Will be soon... 

## Alternatives

Of course, I'am not the first to decide to make a library for ourselves, so I give alternatives, perhaps you will find them more convenient for yourself:  
* [vkwave](https://github.com/fscdev/vkwave)
* [vkbottle](https://github.com/vkbottle/vkbottle)
* [LiteVkApi](https://github.com/Ma-Mush/LiteVkApi)
* [vk_maria](https://github.com/lxstvayne/vk_maria)


### I believe that using my development will be pleasant for you!