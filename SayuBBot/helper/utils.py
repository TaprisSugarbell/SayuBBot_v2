import os
import requests
import tempfile
from PIL import Image


async def file_recognize(filename, out="./"):
    images = ["jpg", "png", "webp"]
    videos = ["mp4", "mkv", "webm"]
    songs = ["mp3", "FLAC", "m4a", "ogg"]
    documents = ["zip", "rar", "apk"]
    direcs = {
        "photo": images,
        "video": videos,
        "audio": songs,
        "document": documents}
    try:
        ext = filename.split(".")[-1]
        if ext in direcs["image"]:
            file_type = "image"
        elif ext in direcs["video"]:
            file_type = "video"
        elif ext in direcs["song"]:
            file_type = "song"
        else:
            file_type = "document"
    except Exception as e:
        print(e)
        file_type = None
        ext = None
    return file_type


async def send_image(dats, url):
    bot, chat_id, = dats
    ext = url.split(".")[-1]
    temp_dir = f"{os.getcwd()}/temp/"
    img_file = tempfile.NamedTemporaryFile(suffix=f".{ext}", dir=temp_dir)
    img_file.write(requests.get(url).content)
    img = Image.open(img_file.name)
    await bot.send_photo(chat_id,
                         img)
