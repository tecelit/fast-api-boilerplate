import os
import logging
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

load_dotenv()

log = logging.getLogger(__name__)

def initializeDbEngine():
    try:
        dbUser = os.getenv('DB_USER')
        dbPass = os.getenv('DB_PASS')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT', default='5432')
        db_server = db_host + ':' + db_port
        
        dbName = os.getenv('DB_NAME')
        db_string = "postgresql://{0}:{1}@{2}/{3}".format(dbUser, dbPass, db_server, dbName)
        
        db = create_engine(db_string)
        if not database_exists(db.url):
            log.warning("Database {} does not exist, attempting to create".format(dbName))
            create_database(db.url)
    
    except Exception as e:
        log.error("Connection to Database Instance failed : {}".format(e))