import re
import nekos
import pyrogram.errors
from pyrogram import Client, filters
from ..helper.utils import send_image

commands = [
    '8ball', 'anal', 'avatar', 'baka', 'bj', 'blowjob',
    'boobs', 'classic', 'cuddle', 'cum', 'cum_jpg', 'ero',
    'erofeet', 'erok', 'erokemo', 'eron', 'eroyuri', 'feed',
    'feet', 'feetg', 'femdom', 'fox_girl', 'futanari', 'gasm',
    'gecg', 'goose', 'hentai', 'holo', 'holoero', 'hololewd', 'hug',
    'kemonomimi', 'keta', 'kiss', 'kuni', 'les', 'lewd', 'lewdk',
    'lewdkemo', 'lizard', 'neko', 'ngif', 'nsfw_avatar', 'nsfw_neko_gif',
    'pat', 'poke', 'pussy', 'pussy_jpg', 'pwankg', 'random_hentai_gif',
    'slap', 'smallboobs', 'smug', 'solo', 'solog', 'spank', 'tickle', 'tits',
    'trap', 'waifu', 'wallpaper', 'woof', 'yuri'
]


format_imgs = ["png", "jpg", "jpeg"]


@Client.on_message(filters.command([i for i in commands]))
async def __nekos__(bot, update):
    print(update)
    chat_id = update.chat.id
    text = re.sub(r"/", "", update.text)
    n = nekos.img(text)
    print(n)
    if n.split(".")[-1] in format_imgs:
        try:
            dats = (bot, chat_id)
            await send_image(dats, n)
            # await bot.send_photo(chat_id,
            #                      photo=n)
        except pyrogram.errors.exceptions.bad_request_400.WebpageCurlFailed:
            dats = (bot, chat_id)
            await send_image(dats, n)
    elif n.split(".")[-1] == "gif":
        await bot.send_animation(chat_id,
                                 animation=n)

