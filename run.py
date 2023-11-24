from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from main import swap_weth_to_token
import logging

TOKEN = '6700289875:AAGqh_8GCOkv1Q51lInUBoCs1xLRgy2MAEc'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    input_data = message.text.split(',')
    if len(input_data) == 4:
        private_key, coin, amount, proxy = map(str.strip, input_data)
        try:
            await message.reply('В процессе...')
            await swap_weth_to_token(private_key, coin, amount, proxy)
        except Exception as e:
            await message.reply(f"Error: {e}")
    else:
        await message.reply("Please send the data in the following format: 'private_key, coin, amount, proxy'. Format `proxy` must be: http://login:password@38.0.101.76:59100")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp)
