from aiogram import Router 
from aiogram.filters import Command
from aiogram.types import Message
from handlers import handlers_start
from handlers.handlers_start import dialogue 
from handlers.dialogue import meneger_info 

router = Router()


@router.message(Command("admin"))
async def Admin_handlers(msg: Message):
 try:
    global dialogue, meneger_info
    new_id = msg.from_user.id
    if new_id in meneger_info:
        dialogues_count1 = meneger_info[new_id]['namber']
        name = dialogue[handlers_start.user_id1]["name"]
    else:
        await msg.answer('У вас нету поки диалогов')    
    await msg.answer(f"""
                     {new_id} \n\n
                     количество ваших диалогов : {dialogues_count1} 
                     \n\n
                     Активные диалоги: \n{name}
                     """)
 except:
     return None  

    

