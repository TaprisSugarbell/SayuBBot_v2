import re
import nekos
from pyrogram import Client, filters

commands = [
        'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
        'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
        'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron',
        'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
        'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo',
        'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg',
        'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom',
        'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif',
        'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof'
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
        await bot.send_photo(chat_id,
                             photo=n)
    elif n.split(".")[-1] == "gif":
        await bot.send_animation(chat_id,
                                 animation=n)

