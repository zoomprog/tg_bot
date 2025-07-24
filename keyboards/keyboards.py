from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.data import (
    MAIN_MENU_BUTTONS, ONE_C_BUTTONS, RECLAMATIONS_BUTTONS, KB_BUTTONS,
    EQUIPMENT_SERVICING_BUTTONS, ABOUT_COMPANY_BUTTONS, TECH_SUPPORT_BUTTONS,
    NESTING_CHECK_BUTTONS
)

def build_keyboard(buttons: list[list[tuple[str, str]]]) -> InlineKeyboardMarkup:
    """
    Универсальная функция для создания InlineKeyboardMarkup.
    buttons: список строк, каждая строка — список пар (текст, callback_data)
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=data) for text, data in row]
            for row in buttons
        ]
    )

def get_main_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(MAIN_MENU_BUTTONS)

def get_1c_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(ONE_C_BUTTONS)

def get_reclamations_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(RECLAMATIONS_BUTTONS)

def get_knowledge_base_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(KB_BUTTONS)

def get_equipment_servicing_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(EQUIPMENT_SERVICING_BUTTONS)

def get_about_company_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(ABOUT_COMPANY_BUTTONS)

def get_tech_support_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(TECH_SUPPORT_BUTTONS)

def get_nesting_check_keyboard() -> InlineKeyboardMarkup:
    return build_keyboard(NESTING_CHECK_BUTTONS)

def get_menu_button_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Меню", callback_data="main_menu")]
        ]
    )

def get_subcategory_button_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ПодПодКатегория", callback_data="sub_sub_category")],
            [InlineKeyboardButton(text="2 ПодПодКатегория", callback_data="2_sub_sub_category")],
            [InlineKeyboardButton(text="Назад", callback_data="back_to_nesting")],
            [InlineKeyboardButton(text="Меню", callback_data="main_menu")]
        ]
    )

def get_sub_sib_category_button_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Еще вложеннее", callback_data="even_more_invested")],
            [InlineKeyboardButton(text="Назад", callback_data="back_to_subcategory")],
            [InlineKeyboardButton(text="Меню", callback_data="main_menu")]
        ]
    )
