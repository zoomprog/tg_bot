import logging
import os
from aiogram.types import FSInputFile

async def send_document_with_caption(message, file_path: str, caption: str, menu_keyboard=None):
    logging.info(f"send_document_with_caption called with file_path={file_path}, caption={caption}")
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        await message.answer(f"Файл не найден: {os.path.basename(file_path)}")
        return

    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    display_name = ' '.join(name.split('_')).strip() + ext

    # Ограничиваем длину имени файла до 60 символов
    max_len = 60
    if len(display_name) > max_len:
        display_name = display_name[:max_len-len(ext)].rstrip() + ext

    logging.info(f"Sending file with display_name={display_name}")
    input_file = FSInputFile(file_path, filename=display_name)

    await message.answer_document(
        document=input_file,
        caption=caption,
        reply_markup=menu_keyboard
    )
    logging.info(f"Document sent: {display_name}")
