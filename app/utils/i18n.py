user_langs = {
    int : str
}

async def set_lang(user_id, lang):
    user_langs[user_id] = lang

async def get_districts_str(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return 'Tumanlar'
    elif lang == 'ru':
        return 'Районы'

async def get_menu(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return ['🍞Non bormi', '⚙️Sozlamalar', '💬Izoh qoldirish']
    elif lang == 'ru':
        return ['🍞Есть ли хлеб', '⚙️Настройки', '💬Оставить отзыв']
    
async def get_back(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return '🔙Ortga'
    elif lang == 'ru':
        return '🔙Назад'
    
async def get_address(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return '📍Manzil'
    elif lang == 'ru':
        return '📍Адрес'
    
async def get_phone(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return '📞Telefon raqam'
    elif lang == 'ru':
        return '📞Номер телефона'
    
async def get_bread(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return '🍞Non'
    elif lang == 'ru':
        return '🍞Хлеб'
    
async def get_no_shops(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return f'Afsuski bu tumanidagi do\'konlardan hali hech qaysi biri bo\'timizdan ro\'yhatdan o\'tmagan.'
    elif lang == 'ru':
        return f'К сожалению магазини в этом районе пока ещё не зарегистрировани в нашем боте.'
    
async def get_shops(d_name, user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return f'{d_name} tumanidagi bo\'tda ro\'yhatdan o\'tgan do\'konlar'
    elif lang == 'ru':
        return f'Магазини в районе {d_name} зарегистрированные в нашем боте'
    
async def get_other_sh(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return f'Boshqa tuman do\'konlarini ko\'rish uchun ortga tugamasini bosing.'
    elif lang == 'ru':
        return f'Чтобы увидеть магазины в других районах нажмите на кнопку назад'
    
async def get_yes(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return '✅Bor'
    elif lang == 'ru':
        return '✅Есть'
    
async def get_no(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return '❌Yo\'q'
    elif lang == 'ru':
        return '❌Нет'

async def get_d_shops(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return f'Siz izlagan do\'kon joylashgan tumani tanlang'
    elif lang == 'ru':
        return f'Выберите район в котором расположен магаз которого вы ищете' 

async def get_set_info(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return 'Non bormi'
    elif lang == 'ru':
        return f'Есть ли хлеб'
    
async def get_admin_menu(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return ['✅Bor', '❌Yo\'q']
    elif lang == 'ru':
        return ['✅Есть', '❌Нет']
    
async def get_success(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return 'Ma\'lumotlar muvaffaqiyatli yangilandi.'
    elif lang == 'ru':
        return 'Информация успешно обновлёню'
    
async def get_settings(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return 'Sozlamalar'
    elif lang == 'ru':
        return 'Настройки'
    
async def settings_menu(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return ['Tilni o\'zgartirish']
    elif lang == 'ru':
        return ['Поменять язык']
    
async def get_comm(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return 'Taklif yoki shikoyatingizni yozing.'
    elif lang == 'ru':
        return 'Напишите свою жалобу или предложение.'
    
async def send_comm(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return 'Sizning izohingiz qabul qilindi. Biz uni tezda ko\'rib chiqishga harakat qilamiz.'
    elif lang == 'ru':
        return 'Ваш отзыв был принять. Мы как можно скорее проверим.'
    
async def answer_admin(user_id):
    lang = user_langs[user_id]

    if lang == 'uz':
        return 'Administratorlardan javob'
    elif lang == 'ru':
        return 'Ответ от администраторов'