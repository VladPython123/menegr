import json 
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router , types
from aiogram.fsm.state import StatesGroup , State
from aiogram.fsm.context import FSMContext


router = Router()

class Form (StatesGroup):
    ru = State()


@router.message(Command("greeting"))
async def start_handler(msg: Message, state: FSMContext):
      await state.set_state(Form.ru)
      await msg.answer("Напишите текст который будет отправляться пользователю если вы связаться с ним")
      
@router.message(Form.ru)
async def text_ru(msg: types.Message, state: FSMContext):
    text1 = msg.text.strip() 
    user_id = msg.from_user.id
    with open('handlers_json/meneger.json', 'r', encoding='utf-8') as file:
       data = json.load(file)
    data[f'{user_id}'] = f'{text1}'
    with open('handlers_json/meneger.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    await state.clear()  
    await msg.answer("Харашо текст был сохранён")
