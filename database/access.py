from config import Config
from database.database import Database

db = Database(Config.DATABASE_URL, Config.SESSION_NAME)
