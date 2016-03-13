import sqlite3
import os.path
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='system.log')

db_file_name = 'settings.db'
# for first run fill, then run create_db() / open_and_write_db()
name = ''
api_key = ''
flags = ''
description = ''


def create_db(db_file_name_local):
    db_connection = sqlite3.connect(db_file_name_local)
    db_conn_cursor = db_connection.cursor()
    db_conn_cursor.execute('''CREATE TABLE bot
        (id INTEGER PRIMARY KEY, name TEXT, api_key TEXT, flags INTEGER, description TEXT)''')
    db_connection.commit()
    db_connection.close()
    logging.debug('file created')


def open_and_write_db(db_file_name_local):
    db_connection = sqlite3.connect(db_file_name_local)
    db_conn_cursor = db_connection.cursor()
    db_conn_cursor.execute('''INSERT INTO bot(name, api_key, flags, description)
                  VALUES(?,?,?,?)''', (name, api_key, flags, description))
    db_connection.commit()
    logging.debug('data writed')
    db_connection.close()


def open_and_read_db(db_file_name_local):
    db_connection = sqlite3.connect(db_file_name_local)
    db_conn_cursor = db_connection.cursor()
    logging.debug('read data')
    for row in db_conn_cursor.execute('SELECT * FROM bot ORDER BY id LIMIT 1'):
        print(row)
        logging.debug(row)
    logging.debug('end data')
    db_connection.close()


def get_data_from_db(file, table, data):
    # Get the latest record from table
    global result_gd
    result_gd = ''
    if not data:
        data = '*'

    db_connection = sqlite3.connect(file)
    db_conn_cursor = db_connection.cursor()

    logging.debug('read data')

    for row in db_conn_cursor.execute('SELECT {1} FROM {0} ORDER BY id DESC LIMIT 1'.format(table, data)):
        # id INTEGER PRIMARY KEY, town TEXT, dtime TEXT, t_value TEXT, h_value INTEGER, w_value TEXT, w_dir TEXT
        # SELECT * FROM    TABLE WHERE   ID = (SELECT MAX(ID)  FROM TABLE);
        # SELECT * FROM table ORDER BY column DESC LIMIT 1;
        result_gd = row

    logging.debug('end data')
    db_connection.close()
    return result_gd

if not (os.path.isfile(db_file_name)):
    logging.debug('settings file not found')
    create_db(db_file_name)
    open_and_write_db(db_file_name)

# open_and_read_db(db_file_name)



