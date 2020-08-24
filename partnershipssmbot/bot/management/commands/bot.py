from django.core.management.base import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request
from django.conf import settings
from bot.models import Profile
import random


def create_db(update: Update, context: CallbackContext):
    if update.message.from_user.first_name != None and update.message.from_user.last_name != None:
        user = update.message.from_user.first_name + ' ' + update.message.from_user.last_name
    else:
        user = update.message.from_user.username
    external_id = update.message.from_user.id
    text = update.message.text

    Profile.objects.get_or_create(
        external_id=external_id,
        defaults={
            'name': user,
            'external_id': external_id,
            'invite_from': text,
            'invited_users': 0,
        }
    )
    Profile.objects.get_or_create(
        name=text,
        defaults={
            'name': text,
            'external_id': random.randint(1,100000),
            'invite_from': '',
            'invited_users': 1,
        }
    )
    reply_text = "Вы успешно зарегистрировали партнера, ссылка на телеграм канал: t.me/joinchat/AAAAAE2wXNaz5xShifACyA"
    update.message.reply_text(
        text=reply_text
    )


def kostil(update: Update,context: CallbackContext):
    pass


class Command(BaseCommand):
    help = 'run bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=getattr(settings, 'PROXY_URL', None),
        )
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        print(bot.get_me())

        message_handler = MessageHandler(Filters.text, create_db)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()