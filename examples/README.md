# Examples

To start development, you need to install the module (see the [installation](../#installation) section) and import it into your project. An example of the simplest echo bot:

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
|-> [Echo](echo)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `text` example, click [here](echo/text.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `audio` example, click [here](echo/audio.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `photo` example, click [here](echo/photo.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `video` example, click [here](echo/video.py).  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `file` example, click [here](echo/file.py).  
|-> [Keyboard](keyboard)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `keyboard` example, click [here](keyboard/keyboard.py).  
|-> [Carousel](carousel)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `carousel` example, click [here](carousel/carousel.py).  
|-> [Geoposition](geoposition)  
&nbsp;&nbsp;&nbsp;&nbsp; ∟ To view the `geoposition` example, click [here](geoposition/geoposition.py). 
