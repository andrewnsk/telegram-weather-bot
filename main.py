import logging
import telegram
from telegram.updater import Updater
from telegram import emoji
from db import get_data_from_db
from bottle_logic import Bottle
from get_weather import GetWeather

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='system.log')

# please, use you own api token
"""
db_file_name = 'settings.db'
bot_settings = get_data_from_db(db_file_name, 'bot', '')
bot_token = bot_settings[2]
"""

bot_token = '186600990:AAHJU4yx2UwFtMf41buQacWsttj6u6Q7rMo'
bot = telegram.Bot(token=bot_token)

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


def wemoji(code):
    # partially get from github.com/mustafababil/Telegram-Weather-Bot/
    if code:
        if str(code)[0] == '2' or code == 900 or code == 901 or code == 902 or code == 905:
            return telegram.Emoji.UMBRELLA_WITH_RAIN_DROPS
        elif str(code)[0] == '3':
            return telegram.Emoji.UMBRELLA_WITH_RAIN_DROPS
        elif str(code)[0] == '5':
            return telegram.Emoji.UMBRELLA_WITH_RAIN_DROPS
        elif str(code)[0] == '6' or code == 903 or code == 906:
            return telegram.Emoji.SNOWFLAKE
        elif str(code)[0] == '7':
            return telegram.Emoji.BLACK_SUN_WITH_RAYS
        elif code == 800:
            return telegram.Emoji.BLACK_SUN_WITH_RAYS
        elif code == 801:
            return telegram.Emoji.CLOUD
        elif code == 802 or code == 803 or code == 803:
            return telegram.Emoji.CLOUD
        elif code == 904:
            return telegram.Emoji.BLACK_SUN_WITH_RAYS
        else:
            return telegram.Emoji.SMILING_FACE_WITH_SUNGLASSES    # Default emoji

    else:
        return telegram.Emoji.SMILING_FACE_WITH_SUNGLASSES   # Default emoji


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Привет! "
                                                         "я бот и я знаю информацию о погоде в Норильске"
                                                         ", Краснодаре "
                                                         "и Сочи" + telegram.Emoji.BLACK_SUN_WITH_RAYS)


dispatcher.addTelegramCommandHandler('start', start)


def weather_message(bot, update, args):
    weather = GetWeather(args[0])

    bot.sendMessage(chat_id=update.message.chat_id, text='Погода ' +
                                                         telegram.Emoji.SUNRISE + '\n' +
                                                         'Температура:          ' +
                                                         str(weather.temperature()) + ' градусов \n' +
                                                         'Влажность:           ' +
                                                         str(weather.humidity()) + ' % \n' +
                                                         'Ветер:               ' +
                                                         ' ' + str(weather.wind_direction()) + ' ' +
                                                         str(weather.wind_speed()) + ' м/с \n' +
                                                         weather.status()
                    )


dispatcher.addTelegramCommandHandler('w', weather_message)


# Поиграем в бытылочку ;)
def bottle_game(bot, update, args):
    newgame = Bottle()
    kissed = newgame.kiss(args[0])
    bot.sendMessage(chat_id=update.message.chat_id, text=kissed + telegram.Emoji.WHITE_UP_POINTING_INDEX + '\n')


dispatcher.addTelegramCommandHandler('bottle', bottle_game)


def echo(bot, update):
    if update.message.text == 'Привет':
        bot.sendMessage(chat_id=update.message.chat_id, text='Ара')

        # bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


dispatcher.addTelegramMessageHandler(echo)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="А вот нет такой команды " + telegram.Emoji.FACE_WITH_STUCK_OUT_TONGUE_AND_WINKING_EYE)


dispatcher.addUnknownTelegramCommandHandler(unknown)

updater.start_polling()
'''
def empty_message(bot, update):
    """
    Empty messages could be status messages, so we check them if there is a new
    group member, someone left the chat or if the bot has been added somewhere.
    """

    # Keep chatlist
    chats = db.get('chats')

    if update.message.chat.id not in chats:
        chats.append(update.message.chat.id)
        db.set('chats', chats)
        logger.info("I have been added to %d chats" % len(chats))

    if update.message.new_chat_participant is not None:
        # Bot was added to a group chat
        if update.message.new_chat_participant.username == BOTNAME:
            return introduce(bot, update)
        # Another user joined the chat
        else:
            return welcome(bot, update)

    # Someone left the chat
    elif update.message.left_chat_participant is not None:
        if update.message.left_chat_participant.username != BOTNAME:
            return goodbye(bot, update)
'''
