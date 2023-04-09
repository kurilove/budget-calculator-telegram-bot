from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove
from config import Api_token
from keyboard import kb_main_menu, kb_expenses, ikb_category, ikb_category_income
from data import expenses_open, income_open, add_num, return_num, \
    dress, product, shoping, bisnes, flag_product, flag_shoping, flag_dress, flag_bisnes, \
    flag_temki, flag_salary, flag_present, temki, present, salary

bot = Bot(Api_token)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Запуск осуществлен")


@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await message.answer("Я запустился",
                         reply_markup=kb_main_menu())


@dp.message_handler(lambda message: message.text == "Затраты")
async def expenses_handler(message: types.Message):
    global expenses_open
    expenses_open = True
    await bot.send_photo(message.chat.id,
                         photo="https://static1.straitstimes.com.sg/s3fs-public/styles/large30x20/public/articles/2023/03/17/iStock-701189054_5.jpg?VersionId=QjzU166woU13n70k.g8lKpSWYr3fm1BA&itok=DMib-0-C",
                         reply_markup=ikb_category(),
                         caption="Фиксируем расходы")
    await message.delete()


@dp.message_handler(lambda message: message.text == "Прибыль")
async def income_handler(message: types.Message):
    global income_open
    income_open = True
    await bot.send_photo(message.chat.id,
                         photo="https://merriam-webster.com/assets/mw/images/article/art-wap-landing-mp-lg/meme-boy-gets-paid-4140-c9dfc888677499743410feaf017cfa46@1x.jpg",
                         caption="Выбери категорию доходов",
                         reply_markup=ikb_category_income())
    await message.delete()


@dp.message_handler(lambda message: message.text == "Отчет")
async def report(message: types.Message):
    global report_text
    expenses_sum = product + dress + shoping + bisnes
    income_sum = temki + present + salary

    total_balance = income_sum - expenses_sum
    await bot.send_photo(message.chat.id,
                         photo="https://blog.myneurogym.com/wp-content/uploads/2019/01/AdobeStock_111503704.jpeg",
                         caption=f"""
<em>Ваши расходы </em>                            
<b>Продукты</b> - {product}р                      
<b>Шопинг</b> - {shoping}р                        
<b>Бизнес</b> - {bisnes}р                           
<b>Одежда</b> - {dress}р

<em>Ваши доходы </em> 
<b>Зарплата</b> - {salary}р  
<b>Темки</b> - {temki}р  
<b>Подарки</b> - {present}р

<em>Ваш баланс</em> - <b>{total_balance}</b>р
<em>Ваш общий доход</em> - <b>{income_sum}</b>р
<em>Ваш общий расход</em> - <b>{expenses_sum}</b>р
""",
                         parse_mode="HTML")


@dp.message_handler(lambda message: message.text == "Обнулить данные")
async def report(message: types.Message):
    await message.answer("Если ты на самом деле хочешь <b>ОБНУЛИТЬ ДАННЫЕ</b>\nто напиши мне '<b>Хочу обнулиться</b>'",
                         parse_mode="HTML")


@dp.message_handler(lambda message: message.text == "Хочу обнулиться")
async def clean_data(message: types.Message):
    global product
    global bisnes
    global shoping
    global dress
    global temki
    global salary
    global present
    product = 0
    bisnes = 0
    shoping = 0
    dress = 0
    temki = 0
    salary = 0
    present = 0

    await message.answer("Все данные были удалены", reply_markup=kb_main_menu())
    await message.delete()


@dp.message_handler(lambda message: message.text == "Главное меню")
async def main_menu_handler(message: types.Message):
    global expenses_open
    global income_open
    global product
    global bisnes
    global shoping
    global dress
    expenses_open = False
    income_open = False
    global flag_product
    global flag_shoping
    global flag_bisnes
    global flag_dress
    flag_product = False
    flag_shoping = False
    flag_bisnes = False
    flag_dress = False
    global add_num
    global return_num
    add_num = False
    return_num = False
    global flag_temki
    global flag_salary
    global flag_present
    flag_temki = False
    flag_salary = False
    flag_present = False

    await message.answer("Возврат в главное меню",
                         reply_markup=kb_main_menu())

    await message.delete()


@dp.message_handler(lambda message: message.text == "добавить")
async def expenses_dobavit(message: types.Message):
    global add_num
    global return_num
    await message.answer('Окей, скажи сколько добавить ',
                         parse_mode="HTML")
    add_num = True
    return_num = False


@dp.message_handler(lambda message: message.text == "убавить")
async def expenses_dobavit(message: types.Message):
    global add_num
    global return_num
    await message.answer('Окей, вводи сколько надо убавить',
                         parse_mode="HTML")
    add_num = False
    return_num = True


@dp.callback_query_handler(lambda callback: callback.data == "продукты")
async def ikb_prouct_cb(callback: types.CallbackQuery):
    global flag_product
    global flag_shoping
    global flag_bisnes
    global flag_dress

    flag_product = True
    flag_shoping = False
    flag_bisnes = False
    flag_dress = False

    await callback.message.answer(text="Начался учет продуктов", reply_markup=kb_expenses())
    await callback.answer("Категория продукты", cache_time=2)


@dp.callback_query_handler(lambda callback: callback.data == "шопинг")
async def ikb_prouct_cb(callback: types.CallbackQuery):
    global flag_product
    global flag_shoping
    global flag_bisnes
    global flag_dress
    flag_product = False
    flag_shoping = True
    flag_bisnes = False
    flag_dress = False
    await callback.message.answer(text="Начался учет шопинга", reply_markup=kb_expenses())
    await callback.answer("Категория шопинг", cache_time=2)


@dp.callback_query_handler(lambda callback: callback.data == "бизнес")
async def ikb_prouct_cb(callback: types.CallbackQuery):
    global flag_product
    global flag_shoping
    global flag_bisnes
    global flag_dress
    flag_product = False
    flag_shoping = False
    flag_bisnes = True
    flag_dress = False
    await callback.message.answer(text="Начался учет бизнес расходов", reply_markup=kb_expenses())
    await callback.answer("Категория бизнес", cache_time=2)


@dp.callback_query_handler(lambda callback: callback.data == "одежда")
async def ikb_prouct_cb(callback: types.CallbackQuery):
    global flag_product
    global flag_shoping
    global flag_bisnes
    global flag_dress
    flag_product = False
    flag_shoping = False
    flag_bisnes = False
    flag_dress = True
    await callback.message.answer(text="Начался учет расходов на одежду", reply_markup=kb_expenses())
    await callback.answer("Категория одежда", cache_time=2)


@dp.callback_query_handler(lambda callback: callback.data == "зарплата")
async def ikb_prouct_cb(callback: types.CallbackQuery):
    global flag_salary
    global flag_temki
    global flag_present
    flag_salary = True
    flag_temki = False
    flag_present = False
    await callback.message.answer(text="Учет дохода от зарплаты", reply_markup=kb_expenses())
    await callback.answer("Категория зарплата", cache_time=2)


@dp.callback_query_handler(lambda callback: callback.data == "темки")
async def ikb_prouct_cb(callback: types.CallbackQuery):
    global flag_salary
    global flag_temki
    global flag_present
    flag_salary = False
    flag_temki = True
    flag_present = False
    await callback.message.answer(text="Учет дохода с темок", reply_markup=kb_expenses())
    await callback.answer("Категория темочки", cache_time=2)


@dp.callback_query_handler(lambda callback: callback.data == "подарки")
async def ikb_prouct_cb(callback: types.CallbackQuery):
    global flag_salary
    global flag_temki
    global flag_present
    flag_salary = False
    flag_temki = False
    flag_present = True
    await callback.message.answer(text="Сколько подарили?", reply_markup=kb_expenses())
    await callback.answer("Категория подарочки", cache_time=2)


def plus_expenses(message):
    global flag_product
    global flag_shoping
    global flag_bisnes
    global flag_dress
    global product
    global bisnes
    global shoping
    global dress

    global flag_salary
    global flag_temki
    global flag_present
    global salary
    global temki
    global present

    if flag_product:
        product += int(message.text)
    if flag_shoping:
        shoping += int(message.text)
    if flag_bisnes:
        bisnes += int(message.text)
    if flag_dress:
        dress += int(message.text)
    if flag_salary:
        salary += int(message.text)
    if flag_temki:
        temki += int(message.text)
    if flag_present:
        present += int(message.text)
    print(f"product {product}\nshoping {shoping}\nbisnes {bisnes}\ndress {dress}\n "
          f"income : salary: {salary}, temki {temki}, present {present}")


def minus_expenses(message):
    global flag_product
    global flag_shoping
    global flag_bisnes
    global flag_dress
    global product
    global bisnes
    global shoping
    global dress

    global flag_salary
    global flag_temki
    global flag_present
    global salary
    global temki
    global present

    if flag_product:
        product -= int(message.text)
    if flag_shoping:
        shoping -= int(message.text)
    if flag_bisnes:
        bisnes -= int(message.text)
    if flag_dress:
        dress -= int(message.text)
    if flag_salary:
        salary -= int(message.text)
    if flag_temki:
        temki -= int(message.text)
    if flag_present:
        present -= int(message.text)
    print(f"product {product}\nshoping {shoping}\nbisnes {bisnes}\ndress {dress}\n "
          f"income : salary: {salary}, temki {temki}, present {present}")


@dp.message_handler()
async def add_num_expenses(message: types.Message):
    global plus_expenses
    global add_num
    global return_num

    try:
        if add_num:
            plus_expenses(message)

        if return_num:
            minus_expenses(message)
        await message.answer("Принял 🫡")

    except ValueError:
        await message.answer('МНЕ НУЖНЫ ЦЫФРЫ БРАТ')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
