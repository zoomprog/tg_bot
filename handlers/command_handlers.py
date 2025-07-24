from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import get_main_keyboard
from states.states import MenuStates

async def cmd_start(message: types.Message, state: FSMContext):
    welcome_text = "Здравствуйте, что бы вы хотели узнать?"
    await message.answer(welcome_text, reply_markup=get_main_keyboard())
    await state.set_state(MenuStates.main_menu)
