from aiogram import Router ,Bot ,F , types
from aiogram.filters import Command
from aiogram.types import Message
from handlers import handlers_start
from handlers.handlers_start import dialogue , user_id1 , language
from handlers import handlers_start
import json 

router = Router()

meneger_info = {}

@router.callback_query(F.data == "Начать_деалог")
async def Start_dialoguelogue(call: types.CallbackQuery, bot : Bot):
    global dialogue ,user_id1 , meneger_info
    meneger_id = call.from_user.id
    new_status = 'False'
    if dialogue[handlers_start.user_id1]["status"] == "True":
         dialogue[handlers_start.user_id1]["status"] = new_status
         dialogue[handlers_start.user_id1]["id_meneger"] = meneger_id
         if user_id1 not in meneger_info:
              meneger_info[meneger_id]={'namber':0 , 'user': handlers_start.user_id1}
              meneger_info[meneger_id]['namber'] + 1
         with open('handlers_json/meneger.json', 'r', encoding='utf-8') as file:
               data = json.load(file)
               print(meneger_id)
               #print(data[meneger_id])  
         await bot.send_message(meneger_id , text="Диалог был начат")
         await bot.send_message(handlers_start.user_id1 , text="Диалог был начат между менеджером")
    elif dialogue[handlers_start.user_id1]["status"] == "False":
                await bot.send_message(meneger_id , text="К сожалению этот пользователь занят")
             
                
@router.message(Command("stop"))
async def stop_dialogue(msg: Message, bot : Bot):
    global dialogue, user_id1, meneger_info,language
    new_id = msg.from_user.id
    if new_id in meneger_info:
        if language[handlers_start.user_id1]['langeage1'] == 1:
            await bot.send_message(meneger_info[new_id]['user'], text="Диалог был закрыт менеджером")
        elif  language[handlers_start.user_id1]['langeage1'] == 2:
            await bot.send_message(meneger_info[new_id]['user'], text="The manager closed the dialogue.")
        del meneger_info[handlers_start.user_id1]
        del dialogue[handlers_start.user_id1]    
        await bot.send_message(new_id, text="Вы закрыли диалог")        
    else:
        return None
                
@router.message()
async def dialogue_handler(msg: types.Message, bot: Bot):
    global dialogue, user_id1, meneger_info
    text = msg.text.strip()
    new_id = msg.from_user.id
    if new_id in dialogue:
        await bot.send_message(dialogue[new_id]["id_meneger"], text=f"{text}")
    else:
        if new_id in meneger_info:
            await bot.send_message(meneger_info[new_id]['user'], text=f"{text}")
        else:
            return None
    
    
