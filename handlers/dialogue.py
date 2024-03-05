from aiogram import Router ,Bot ,F , types
from handlers import handlers_start



router = Router()

text1 = "Здравствуйте, меня зовут Алексей…"

text2 = "Hello, my name is Alexey..."


async def notify_inactive_user(user_id, bot: Bot):
    await bot.send_message(user_id, "У вас еще остались вопросы ?")


async def close_dialog(user_id, bot: Bot):
    await bot.send_message(user_id, "Спасибо за обращение !")


async def notify_inactive_user(user_id, bot: Bot):
    await bot.send_message(user_id, "Do you still have questions ?")


async def close_dialog(user_id, bot: Bot):
    await bot.send_message(user_id, "Thank you for reaching out !")

@router.callback_query(F.data == "Начать_деалог")
async def Russian(call: types.CallbackQuery , bot : Bot):
    
    await bot.send_message(call.from_user.id, "Деалог був запущен")
    
