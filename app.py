import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers.command_handlers import cmd_start
from handlers.callback_handlers import handle_buttons

load_dotenv()
# Получение токена из переменной окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN provided")

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация хендлеров
dp.message.register(cmd_start, Command("start"))
dp.callback_query.register(handle_buttons)



def main():
    logging.info("Starting bot...")
    dp.run_polling(bot, skip_updates=True)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
    except Exception as e:
        logging.error(f"Bot stopped due to error: {e}")
        raise
