import os

from helper_func.dbhelper import Database as Db
db = Db().setup()

import pyrogram

class Config:

    ENCODE_DIR = os.environ.get("ENCODE_DIR", "encodes") 
    APP_ID = os.environ.get("APP_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 

    #comma seperated user id of users who are allowed to use
    #ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
    OWNER_ID = os.environ.get("OWNER_ID", '1276627253') 
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", '-1001157048481')
