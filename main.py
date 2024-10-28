import asyncio
import logging
from bot.dispatcher import bot,dp
from  bot.handlers.start_handler import start_register


async def main():

    await start_register(dp,bot)
    await dp.start_polling(bot)
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())