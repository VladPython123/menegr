from aiogram import Router ,Bot ,F , types
from aiogram.filters import Command
from aiogram.types import Message
from handlers import handlers_start
from handlers.handlers_start import dialogue , user_id1 , language
from handlers import handlers_start
from datetime import datetime, timedelta
import json , asyncio

router = Router()

time1 = 0
id_meneger = None

admin = {}

meneger_info = {}


async def check_activity(bot: Bot):
    global time1, id_meneger
    while True:
        await asyncio.sleep(600)
        for handlers_start.user_id1, data in list(dialogue.items()):
            last_activity = data.get("last_activity")
            if last_activity and datetime.now() - last_activity > timedelta(minutes=10):
                if language[handlers_start.user_id1]['langeage1'] == 1:
                    if time1 == 0:
                        time1 += 1
                        await bot.send_message(handlers_start.user_id1, "У вас еще остались вопросы ?")
                elif language[handlers_start.user_id1]['langeage1'] == 2:
                    if time1 == 0:
                        time1 += 1
                        await bot.send_message(handlers_start.user_id1, "Do you still have questions ?")
            elif last_activity and datetime.now() - last_activity < timedelta(minutes=10) and time1 != 0:
                time1 = 0  
            if last_activity and datetime.now() - last_activity > timedelta(minutes=20):
                if language[handlers_start.user_id1]['langeage1'] == 1:
                    await bot.send_message(handlers_start.user_id1, "Спасибо за обращение !")
                elif language[handlers_start.user_id1]['langeage1'] == 2:
                    await bot.send_message(handlers_start.user_id1, "Thanks for reaching out !")
                del dialogue[handlers_start.user_id1]
                del meneger_info[id_meneger]
  
                
                
@router.callback_query(F.data == "Начать_деалог")
async def Start_dialoguelogue(call: types.CallbackQuery, bot : Bot):
   try: 
    global dialogue ,user_id1 , meneger_info,admin,id_meneger ,time1 
    meneger_id = call.from_user.id
    id_meneger = meneger_id
    new_status = 'False'
    if dialogue[handlers_start.user_id1]["status"] == "True":
         dialogue[handlers_start.user_id1]["status"] = new_status
         dialogue[handlers_start.user_id1]["id_meneger"] = meneger_id
         if user_id1 not in meneger_info:
              meneger_info[meneger_id]={'namber':0 , 'user': handlers_start.user_id1}
              meneger_info[meneger_id]['namber'] =+ 1
         with open('handlers_json/meneger.json', 'r', encoding='utf-8') as file:
               data = json.load(file)
               meneger_id = (f'{meneger_id}')
               text1 = data[f"{meneger_id}"]
         await bot.send_message(meneger_id , text="Диалог был начат")
         await bot.send_message(handlers_start.user_id1 , text=text1)
         asyncio.create_task(check_activity(bot)) 
         dialogue[handlers_start.user_id1]["last_activity"] = datetime.now()
    elif dialogue[handlers_start.user_id1]["status"] == "False":
                await bot.send_message(meneger_id , text="К сожалению этот пользователь занят")
   except:
       return None            

            
                
@router.message(Command("stop"))
async def stop_dialogue(msg: Message, bot : Bot):
  try:
    global dialogue, user_id1, meneger_info,language
    new_id = msg.from_user.id
    if new_id in meneger_info:
        if language[handlers_start.user_id1]['langeage1'] == 1:
            await bot.send_message(meneger_info[new_id]['user'], text="Диалог был закрыт менеджером")
        elif  language[handlers_start.user_id1]['langeage1'] == 2:
            await bot.send_message(meneger_info[new_id]['user'], text="The manager closed the dialogue.")
        del meneger_info[new_id]
        del dialogue[handlers_start.user_id1]    
        await bot.send_message(new_id, text="Вы закрыли диалог")        
    else:
        return None
  except:
      return None  
                
@router.message()
async def dialogue_handler(msg: types.Message, bot: Bot):
    global dialogue, user_id1, meneger_info, time1
    text = msg.text.strip()
    new_id = msg.from_user.id
    if new_id in dialogue:
        if time1 == 1:
            time1 = 0
        asyncio.create_task(check_activity(bot))
        dialogue[new_id]["last_activity"] = datetime.now()    
        await bot.send_message(dialogue[new_id]["id_meneger"], text=f"{text}")
    else:
        if new_id in meneger_info:
            if "У вас еще остались вопросы ?" in text:
                time1 = 0
            else:
                await bot.send_message(meneger_info[new_id]['user'], text=f"{text}")
        else:
            return None
