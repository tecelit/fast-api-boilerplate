from dotenv import load_dotenv
import os

load_dotenv()


dbUser = os.getenv('DB_USER')
dbPass = os.getenv('DB_PASS')

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT', default='5432')
db_server = db_host + ':' + db_port
dbName = os.getenv('DB_NAME')
db_string = "postgresql://{0}:{1}@{2}/{3}".format(dbUser, dbPass, db_server, dbName)

config_vars = {
    "DB_STRING" : db_string
}