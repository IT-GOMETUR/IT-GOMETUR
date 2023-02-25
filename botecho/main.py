from aiogram import Bot, types, Dispatcher, executor

import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands= 'start')
async def com_start(message: types.Message):
    await message.answer('Привет, Я эхо Бот \nНапиши мне что-нибудь!')

@dp.message_handler()
async def echo(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)        