import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import dialogue
from handlers import handlers_start
from handlers_json import handlers_json
from admin_panely import handlers_admin

BOT_TOKEN = '6862881309:AAGb2D4bXWM7rKbnU_zzUbDp6BqneJqrDRI'

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(handlers_start.router,handlers_json.router,handlers_admin.router,dialogue.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
  
