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


bot = Bot()
bot.TOKEN = TOKEN
bot.APP_ID = APP_ID
bot.run(init_method=geoposition)