import asyncio
import logging
import sys
from environs import Env

from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType
from aiogram.utils.markdown import hbold
from test import find_stories

from aiogram.client.session.aiohttp import AiohttpSession

env = Env()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = env.str("TOKEN")
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.username)}!Напишите никнейм человека которого хотите скачать Stories")




@dp.message()
async def echo_handler(message: types.Message) -> None:
    username = message.text
    await message.reply('Kut..')
    try:
        stories = find_stories(username)
        for i in stories:
            media_type = i['Type']
            if media_type == 'Story-Video':
                await message.answer_video(video=i['media'], caption='Story Video')
            elif media_type == 'Story-Image':
                await message.answer_photo(photo=i['media'], caption='Story Photo')
    except:
        await message.answer("Topilmadi")



async def main() -> None:
    session = AiohttpSession(proxy="http://proxy.server:3128")
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML, session=session)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
