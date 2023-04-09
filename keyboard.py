from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Клавитура главного меню
def kb_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Затраты")
    btn2 = KeyboardButton("Прибыль")
    btn3 = KeyboardButton("Отчет")
    btn4 = KeyboardButton("Обнулить данные")
    kb.add(btn1, btn2, btn3).add(btn4)
    return kb  # #r# ####


# клавиатура манипуляций с категориями
def kb_expenses():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = KeyboardButton("добавить")
    btn2 = KeyboardButton("убавить")
    btn3 = KeyboardButton("Главное меню")
    kb.add(btn1, btn2).add(btn3)
    return kb


#  инлайн клавиатура категорий расходов
def ikb_category():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Продукты", callback_data="продукты")],
        [InlineKeyboardButton(text="Шопинг", callback_data="шопинг")],
        [InlineKeyboardButton(text="Бизнес", callback_data="бизнес")],
        [InlineKeyboardButton(text="Одежда", callback_data="одежда")]
    ])
    return ikb

# инлайн клавиатура категорий доходов
def ikb_category_income():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Зарплата", callback_data="зарплата")],
        [InlineKeyboardButton(text="Темки", callback_data="темки")],
        [InlineKeyboardButton(text="Подарки", callback_data="подарки")]
    ])
    return ikb
