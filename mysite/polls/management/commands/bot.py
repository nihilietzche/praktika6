from django.core.management.base import BaseCommand
from telegram import Bot
from django.conf import settings
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler
from telegram.ext import Filters, CommandHandler
from telegram.ext import Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.utils.request import Request
import os

from polls.models import *

PORT = int(os.environ.get('PORT', 8000))

def start(update, context):
    chat_id = update.message.chat_id
    username = update.message.chat.username

    Profile.objects.update_or_create(
        external_id = chat_id,
        defaults ={
            'name': username,
        }
    )
    
    cat_objs = Category.objects.order_by('id')[:4]
    message = f''' '''


    for cat_obj in cat_objs:
        message += f'''{cat_obj.category} \n'''


    update.message.reply_text('Привет {}! Добро пожаловать в нашего бота с тестами '.format(username))
    update.message.reply_text('Ваш ID {}!'.format(chat_id))
    update.message.reply_text(f'''{message}''')
    update.message.reply_text(quest(), reply_markup=menu_keyboard())

########################################################################################

CALLBACK_BUTTON1_CATEGORY = "callback_button1_category"
CALLBACK_BUTTON2_RESULTS = "callback_button2_results"
CALLBACK_BUTTON_HIDE_KEYBOARD = "callback_button_hide"

CALLBACK_BUTTON3_CATEGORY1 = "callback_button3_category1"
CALLBACK_BUTTON4_CATEGORY2 = "callback_button4_category2"
CALLBACK_BUTTON5_CATEGORY3 = "callback_button5_category3"
CALLBACK_BUTTON6_CATEGORY4 = "callback_button6_category4"
CALLBACK_BUTTON7_CATEGORY_MORE = "callback_button7_category_more"

# CALLBACK_BUTTON8_TEST1 = "callback_button8_test1"
# CALLBACK_BUTTON9_TEST2 = "callback_button9_test2"
# CALLBACK_BUTTON10_TEST3 = "callback_button10_test3"
# CALLBACK_BUTTON11_TEST4 = "callback_button11_test4"
# CALLBACK_BUTTON12_TEST_MORE = "callback_button12_test_more"


TITLES = {
    CALLBACK_BUTTON1_CATEGORY: "Категории",
    CALLBACK_BUTTON2_RESULTS: "Результаты",
    CALLBACK_BUTTON_HIDE_KEYBOARD: "Спрять клавиатуру",
}

########################################################################################

def menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_CATEGORY], callback_data=CALLBACK_BUTTON1_CATEGORY),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_RESULTS], callback_data=CALLBACK_BUTTON2_RESULTS),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HIDE_KEYBOARD], callback_data=CALLBACK_BUTTON_HIDE_KEYBOARD),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def category_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_CATEGORY1], callback_data=CALLBACK_BUTTON3_CATEGORY1),
        ]
    ]


def quest():
    return 'Выберите дальнейшие действия, вы можете или найти тесты по категориям или посмотреть результаты своих пройденных тестов'

########################################################################################

class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True,
        )
        
        start_command = CommandHandler('start', start)
        updater.dispatcher.add_handler(start_command)

        updater.start_polling()



        # updater.start_webhook(
        #             listen='0.0.0.0',
        #             port=int(PORT),
        #             url_path=settings.TOKEN,
        #             webhook_url='https://1ca2-85-174-193-158.ngrok.io/' + settings.TOKEN,
        # )

        updater.idle()