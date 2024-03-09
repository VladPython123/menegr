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
async def greeting_handler(msg: Message, state: FSMContext):
    await state.set_state(Form.ru)
    await msg.answer("Введите текст, который будет отправлен пользователю при связи с ним")

@router.message(Form.ru)
async def text_ru(msg: types.Message, state: FSMContext):
    text1 = msg.text.strip() 
    meneger_id = msg.from_user.id
    with open('handlers_json/meneger.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    if str(meneger_id) in data:
        data[str(meneger_id)] = text1
        message = "Текст успешно обновлен"
    else:
        data[str(meneger_id)] = text1
        message = "Новый текст успешно добавлен"
    with open('handlers_json/meneger.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    await state.clear()  
    await msg.answer(message)
