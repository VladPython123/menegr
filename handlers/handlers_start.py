from aiogram import  Router, types , F ,Bot
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup , State
from aiogram.fsm.context import FSMContext
from keyboardmy.keyboard_users import (buttons1
, buttons2 , buttons3 , buttons4)

router = Router()

chat_id = "-1002000016944"

dialogue = {}
language = {}
user_id1 = None

class Form (StatesGroup):
    text1 = State()
    text2 = State()

@router.message(Command("start"))
async def start_handler(msg: Message):
    global language
    user_id1 = msg.from_user.id
    if user_id1 not in language:
        language[user_id1]={'langeage1':0}
    if language[user_id1]['langeage1'] == 0:
        keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons1,resize_keyboard=True,)
        await msg.answer("Choose a language", reply_markup=keyboard1)
    elif language[user_id1]['langeage1'] == 1:
           keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons3,resize_keyboard=True,)
           await msg.answer("Если вам нужно связаться с менеджером, то нажмите на кнопку", reply_markup=keyboard2)
    elif language[user_id1]['langeage1'] == 2:
          keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=buttons2,resize_keyboard=True,)
          await msg.answer("If you need to contact the manager, click on the button", reply_markup=keyboard3)  
    
    
    
@router.callback_query(F.data == "Сообщить менеджеру")    
@router.callback_query(F.data == "Русский")
async def Russian(call: types.CallbackQuery , state: FSMContext):
    global language
    user_id1 = call.from_user.id
    language[user_id1]['langeage1'] =+ 1
    await state.set_state(Form.text1)
    await call.message.edit_text("Видите ваши проблемы :")
    
 
@router.message(Form.text1)
async def text_ru(msg: types.Message, state: FSMContext, bot: Bot):
    global user_id1 , dialogue
    text1 = msg.text.strip()
    text2 = len(text1)
    if text2 < 10:
         await msg.answer("Напиши еще что-нибудь интересное")
    else:
        user_id1 = msg.from_user.id
        print (user_id1)
        user_id = user_id1
        name = msg.from_user.first_name
        username = msg.from_user.username
        profile_link = f"https://t.me/{username}" 
        if user_id1 not in dialogue:
             dialogue[user_id1]={
            "id_users": user_id1,
            "id_meneger": None,
            "name": f"{name}",
            "status": "True",
        }
        await state.clear()
        keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons4,resize_keyboard=True,)
        await bot.send_message(chat_id , text=f"{user_id} \n\n {name} \n\n Русский \n\n {profile_link} \n\n {text1}",reply_markup=keyboard1)
        await msg.answer("Мы вас сообщим, если менеджер вам ответит")
             
        
    
@router.callback_query(F.data == "Notify_manager")    
@router.callback_query(F.data == "English")
async def English(call: types.CallbackQuery , state: FSMContext):
    global language
    user_id1 = call.from_user.id
    language[user_id1]['langeage1'] =+ 2
    await state.set_state(Form.text2)
    await call.message.edit_text("Write your problems :")
    
    
@router.message(Form.text2)
async def text_eng(msg: types.Message, state: FSMContext, bot: Bot):
    global dialogue ,user_id1
    text = msg.text.strip()
    text1 = len(text)
    if text1 < 10:
         await msg.answer("Write something else interesting")
    else:
        user_id1 = msg.from_user.id
        name = msg.from_user.first_name
        username = msg.from_user.username
        profile_link = f"https://t.me/{username}"
        if user_id1 not in dialogue:
             dialogue[user_id1]={
            "id_users": user_id1,
            "id_meneger": None,
            "name": f"{name}",
            "status": "True",
        }   
        await state.clear()
        keyboard1 = types.InlineKeyboardMarkup(inline_keyboard=buttons4,resize_keyboard=True,)
        await bot.send_message(chat_id , text=f"{user_id1} \n\n {name} \n\n English \n\n {profile_link} \n\n{text}",reply_markup=keyboard1)
        await msg.answer("We will notify you if the manager responds to you")
            
