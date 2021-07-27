import re

import cryptocompare

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.utils.helpers import escape_markdown
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from django_telegrambot.apps import DjangoTelegramBot

from .models import MenuItem, TgProfile

import logging

logger = logging.getLogger(__name__)


def get_or_create(tg_effective_user):
    tg_profile, _ = TgProfile.objects.get_or_create(
        tg_id=tg_effective_user.id,
        username=f"@{tg_effective_user.username}",
        first_name=tg_effective_user.first_name,
        second_name=tg_effective_user.last_name,
    )
    return tg_profile


def start_handler(update: Update, context: CallbackContext):
    tg_profile = get_or_create(update.effective_user)

    message = (
        f"Здравствуйте, {escape_markdown(tg_profile.username)}\n"
        "Данный бот показывает текущий курс таких криптовалют, как\n"
        "BTC, ETH, DOGE\n\n"
        "Для того, чтобы узнать курс, интерисующей вас валюты,\n"
        "нажмите на соответствующую кнопку снизу"
    )
    main_keyboard = [[KeyboardButton(item.name) for item in MenuItem.objects.all()]]
    reply_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)

    update.message.reply_markdown_v2(message, reply_markup=reply_markup, )


def keyboard_button_handler(update: Update, context: CallbackContext):
    if match := re.match(r"^(BTC|ETH|DOGE)", update.message.text):
        currency = match.group(1)
        price = cryptocompare.get_price(currency, 'USD')
        update.message.reply_text(text=f"На данный момент {currency} стоит {price[currency]['USD']} USD")
    else:
        update.message.reply_text(
            text=(
                "Неизвестное сообщение.\n"
                "Для корректной работы используйте кнопки на раскладке"
            )
        )


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"' % (update, context.error))


def main():
    logger.info("Loading handlers for telegram bot")

    logging.basicConfig(format="%(asctime)s:%(name)s:%(levelname)s: %(message)s", level=logging.DEBUG)

    dp = DjangoTelegramBot.dispatcher

    dp.add_handler(CommandHandler('start', start_handler))
    dp.add_handler(MessageHandler(Filters.text, keyboard_button_handler))
    dp.add_error_handler(error)
