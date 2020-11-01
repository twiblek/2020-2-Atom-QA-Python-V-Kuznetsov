import sqlalchemy
import json

from models.models import Base
from sqlalchemy.orm import sessionmaker

class PostgresConnection(object):
    def __init__(self):

        self.db_cred = self.get_credentials()

        self.connection = self.connect()

        Base.metadata.drop_all(self.engine, checkfirst=True)
        Base.metadata.create_all(self.engine)

        session = sessionmaker(bind=self.connection)
        self.session = session()

    def get_credentials(self):
        with open('cred.json', 'r', encoding='utf-8') as f:
            db_cred = json.loads(f.read())

        return db_cred

    def get_connection(self, db_created=False):
        
        self.engine = sqlalchemy.create_engine('postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
            user=self.db_cred['user'],
            password=self.db_cred['password'],
            host=self.db_cred['host'],
            port=self.db_cred['port'],
            db=self.db_cred['db_name'] if db_created else 'postgres'
        ))
        return self.engine.connect()

    def connect(self):
        connection = self.get_connection(db_created=False)

        connection.execute('commit')
        connection.execute('DROP DATABASE IF EXISTS %s' % self.db_cred['db_name'])
        connection.execute('commit')
        connection.execute('CREATE DATABASE %s' % self.db_cred['db_name'])

        connection.close()
        self.engine.dispose()

        return self.get_connection(db_created=True)

    def close_connection(self):
        self.connection.close()
        self.engine.dispose()
