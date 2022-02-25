from aiogram import Bot, types, Dispatcher, executor
from config import Token

bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply(f"Assalawma Aleykum {message.from_user.first_name}!\nMen User FAQ Bot pan.")

@dp.message_handler(commands='help')
async def start(message: types.Message):
    await message.reply(f"Assalawma Aleykum {message.from_user.first_name}!\nBottan paydalaniw ushin qa`legen so`z jiberin`.\n\nBuyriqlar:\n\t/start\n\t/help")

@dp.message_handler(commands='reklama')
async def start(message: types.Message):
    await message.reply("https://t.me/matematika_patsha/266")
    await message.reply("https://t.me/matematika_patsha/245")
    await message.reply("Eger sizde reklama bermekshi bolsan`iz adminge xabarlasin`.\n@Anvar_Janabaev")

@dp.message_handler()
async def start(message: types.Message):
    await message.reply(f"At: {message.from_user.first_name}\nFamiliya: {message.from_user.last_name}\nToliq: {message.from_user.full_name}\nusername: @{message.from_user.username}\nid: {message.chat.id}\nTil: {message.from_user.language_code}")
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
