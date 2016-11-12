import logging
import telegram
from telegram.updater import Updater
from urllib.parse import quote
from get_weather import GetWeather
import signal
import multiprocessing

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='system.log')

# please, use you own api token
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
                                                         "я бот и я знаю информацию о погоде"
                                                         " в различных уголках мира"
                                                         " " + telegram.Emoji.BLACK_SUN_WITH_RAYS)


dispatcher.addTelegramCommandHandler('start', start)


def god(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="2016 Андрей Дорохин, Норильск" + telegram.Emoji.FACE_WITH_STUCK_OUT_TONGUE_AND_WINKING_EYE)


dispatcher.addTelegramCommandHandler('god', god)


def weather_message(bot, update, args):
    print('weather message')
    if not args:
        town = 'Norilsk'
    else:
        town = quote(args[0])

    weather = GetWeather(town)

    bot.sendMessage(chat_id=update.message.chat_id, text='Погода ' +
                                                         telegram.Emoji.SUNRISE + '\n' +
                                                         'Температура: ' +
                                                         weather.temperature() + ' градусов \n' +
                                                         'Влажность: ' +
                                                         weather.humidity() + ' % \n' +
                                                         'Ветер: ' +
                                                         ' ' + weather.wind_direction() + ' ' +
                                                         weather.wind_speed() + ' м/с \n'
                    )


dispatcher.addTelegramCommandHandler('w', weather_message)


def echo(bot, update):
    if update.message.text == 'Привет':
        bot.sendMessage(chat_id=update.message.chat_id, text='Ара')

        # bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


dispatcher.addTelegramMessageHandler(echo)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="А вот нет такой команды " + telegram.Emoji.FACE_WITH_STUCK_OUT_TONGUE_AND_WINKING_EYE)
dispatcher.addUnknownTelegramCommandHandler(unknown)


stop_event = multiprocessing.Event()


def stop(signum, frame):
    stop_event.set()

signal.signal(signal.SIGTERM, stop)

if __name__ == '__main__':
    while not stop_event.is_set():
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

