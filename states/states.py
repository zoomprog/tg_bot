from aiogram.fsm.state import State, StatesGroup

class MenuStates(StatesGroup):
    main_menu = State()
    one_c_submenu = State()
    reclamations_submenu = State()
    knowledge_base_submenu = State()
    equipment_servicing_submenu = State()
    about_company_submenu = State()
    tech_support_submenu = State()
    nesting_check_submenu = State()
