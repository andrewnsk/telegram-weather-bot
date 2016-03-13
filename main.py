import logging
import telegram
from telegram import Updater, emoji
from db import get_data_from_db

# please, use you own ipi token
bot_token = '186600990:AAHJU4yx2UwFtMf41buQacWsttj6u6Q7rMo'
bot = telegram.Bot(token=bot_token)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Привет! "
                                                         "я бот и я знаю информацию о погоде в Норильске"
                                                         ", Краснодаре "
                                                         "и Сочи" + telegram.Emoji.BLACK_SUN_WITH_RAYS)


dispatcher.addTelegramCommandHandler('start', start)


def info(bot, update, args):
    town = str(args[0])

    if town == 'Норильск' or 'норильск':
        table = 'weather'
    else:
        table = 'error'

    file = 'weather.db'

    data = ''
    weather = get_data_from_db(file, table, data)
    '''
    weather_krasnodar = get_data_from_db(file, table_krasnodar, data)
    weather_sochi = get_data_from_db(file, table_sochi, data)
    '''

    bot.sendMessage(chat_id=update.message.chat_id, text='Погода в Норильске ' +
                                                         telegram.Emoji.WHITE_UP_POINTING_INDEX + '\n' +
                                                         str(args) + ' ' + town + '\n'
                                                         'Температура:          ' +
                                                         str(weather[3]) + '\n' +
                                                         'Влажность:           ' +
                                                         str(weather[4]) + ' % \n' +
                                                         'Ветер:               ' + str(weather[5]) +
                                                         ' ' + str(weather[6]) + '\n')


dispatcher.addTelegramCommandHandler('info', info)


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


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
