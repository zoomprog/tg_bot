from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.keyboards import (
    get_main_keyboard, get_1c_keyboard, get_reclamations_keyboard,
    get_knowledge_base_keyboard, get_equipment_servicing_keyboard,
    get_about_company_keyboard, get_tech_support_keyboard,
    get_nesting_check_keyboard, get_menu_button_keyboard,
    get_subcategory_button_keyboard, get_sub_sib_category_button_keyboard
)
from states.states import MenuStates
from utils.document_sender import send_document_with_caption
from data.data import (
    ACTION_NAMES, TEXT_reclamation_klon, TEXT_reclamation_masterglass,
    TEXT_reclamation_region50, TEXT_reclamation_metronom
)
from aiogram.exceptions import TelegramBadRequest

async def handle_buttons(callback: types.CallbackQuery, state: FSMContext):
    action = callback.data

    # Обработка кнопки назад для разных уровней меню
    if action == "back_to_nesting":
        await callback.message.edit_text(
            "Выберите подкатегорию",
            reply_markup=get_nesting_check_keyboard()
        )
        return

    elif action == "back_to_subcategory":
        await callback.message.edit_text(
            "Выберите подподкатегорию",
            reply_markup=get_subcategory_button_keyboard()
        )
        return

    elif action == "back_to_main":
        await callback.message.edit_text(
            "Здравствуйте, что бы вы хотели узнать?",
            reply_markup=get_main_keyboard()
        )
        await state.set_state(MenuStates.main_menu)
        return

    # Обработка основных разделов меню
    handlers = {
        "1c_menu": (get_1c_keyboard(), MenuStates.one_c_submenu),
        "reclamation": (get_reclamations_keyboard(), MenuStates.reclamations_submenu),
        "knowledge_base": (get_knowledge_base_keyboard(), MenuStates.knowledge_base_submenu),
        "equipment_servicing": (get_equipment_servicing_keyboard(), MenuStates.equipment_servicing_submenu),
        "about_the_company": (get_about_company_keyboard(), MenuStates.about_company_submenu),
        "technical_support": (get_tech_support_keyboard(), MenuStates.tech_support_submenu),
        "checking_nesting": (get_nesting_check_keyboard(), MenuStates.nesting_check_submenu),
    }

    if action in handlers:
        keyboard, new_state = handlers[action]
        await callback.message.edit_text(
            "Выберите подкатегорию",
            reply_markup=keyboard
        )
        await state.set_state(new_state)
        return

    # Обработка документов 1С
    documents_1c = {
        "1c_create_shipping": ("file/1c/Создание_отгрузочной_накладной.pdf", "Создание отгрузочной накладной"),
        "1c_return": ("file/1c/Возврат_от_покупателя.pdf", "Возврат от покупателя"),
        "1c_create_contractor": ("file/1c/Создание_контрагента.pdf", "Создание контрагента"),
        "1c_create_nomenclature": ("file/1c/Создание_номенклатуры.pdf", "Создание номенклатуры"),
        "1c_create_order": ("file/1c/Создание_Заказа_Покупателя_и_выставление_счёта.pdf", "Создание Заказа Покупателя и выставления"),
    }

    if action in documents_1c:
        file_path, caption_text = documents_1c[action]
        await callback.message.delete()
        await send_document_with_caption(
            callback.message,
            file_path,
            f"Вот документ для изучения: {caption_text}",
            get_menu_button_keyboard()
        )
        return

    # Обработка вложенных меню
    if action == "nesting_first":
        await callback.message.edit_text(
            'Выберите подподкатегорию',
            reply_markup=get_subcategory_button_keyboard()
        )
        return
    
    elif action == "nesting_second":
        try:
            await callback.message.edit_text(
                'Просто проверка, ничего важного',
                reply_markup=get_menu_button_keyboard()
            )
        except TelegramBadRequest as e:
            if "message is not modified" in str(e):
                await callback.message.answer('Просто проверка, ничего важного', reply_markup=get_menu_button_keyboard())
            else:
                raise
        return
    
    elif action == "nesting_third":
        try:
            await callback.message.edit_text(
                'Ожидайте... 😊',
            )
        except TelegramBadRequest as e:
            if "message is not modified" in str(e):
                await callback.message.answer('Ожидайте... 😊')
            else:
                raise
        return
    

    elif action == "sub_sub_category":
        await callback.message.edit_text(
            'Выберите подподкатегорию',
            reply_markup=get_sub_sib_category_button_keyboard()
        )
        return

    elif action == "2_sub_sub_category":
        await callback.message.edit_text(
            'Вы выбрали 2 ПодПодКатегория',
            reply_markup=get_menu_button_keyboard()
        )
        return

    # Обработка рекламаций
    reclamation_handlers = {
        "reclamation_klon": (TEXT_reclamation_klon, None),
        "reclamation_masterglass": (TEXT_reclamation_masterglass, None),
        "reclamation_region50": (TEXT_reclamation_region50, None),
        "reclamation_metronom": (TEXT_reclamation_metronom, None),
        "reclamation_restinternational": (None, ("file/COMPANY/Рестинтернешнл.docx", "Рестинтернешнл")),
    }

    if action in reclamation_handlers:
        text, file_info = reclamation_handlers[action]
        await callback.message.delete()
        if text:
            await callback.message.answer(text, reply_markup=get_menu_button_keyboard())
        elif file_info:
            file_path, caption_text = file_info
            await send_document_with_caption(
                callback.message,
                file_path,
                f"Вот документ для изучения {caption_text}",
                get_menu_button_keyboard()
            )
        return

    # Обработка базы знаний
    kb_documents = {
        "kb_syrups_toppings": ("file/KnowledgeBase/Сиропы,_топинги,_пюре.pdf", "Сиропы, топинги, пюре"),
        "kb_bar_inventory": ("file/KnowledgeBase/Барный_инвентарь.pdf", "Барный инвентарь"),
    }

    if action in kb_documents:
        file_path, caption_text = kb_documents[action]
        await callback.message.delete()
        await send_document_with_caption(
            callback.message,
            file_path,
            f"Вот документ для изучения {caption_text}",
            get_menu_button_keyboard()
        )
        return

    # Специальные действия
    if action == "main_menu":
        await callback.message.delete()
        await callback.message.answer(
            "Здравствуйте, что бы вы хотели узнать?",
            reply_markup=get_main_keyboard()
        )
        await state.set_state(MenuStates.main_menu)
        return

    elif action == "kb_equipment":
        await callback.message.delete()
        await callback.message.answer('Ожидайте... 😊')
        return

    elif action == "even_more_invested":
        await callback.message.edit_text(
            'Просто проверка, ничего важного',
            reply_markup=get_menu_button_keyboard()
        )
        return
