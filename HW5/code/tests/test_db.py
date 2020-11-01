import pytest
import logging
from conftest import logger

from models.models import *
from manager.postgres_manager import PostgresConnection


class TestPostgres(object):
    @pytest.fixture(scope='function')
    def setup(self):
        self.postgres = PostgresConnection()

    def test_create_sql(self, setup):
        sql_query = "INSERT INTO pets (nickname, kind, is_male) VALUES ('Шарик', 'Собака', TRUE);"
        self.postgres.session.execute(sql_query)
        self.postgres.session.commit()

        sql_query = "SELECT * FROM pets WHERE nickname = 'Шарик';"
        res = self.postgres.session.execute(sql_query)
        assert res.rowcount == 1  

        self.postgres.close_connection()   

    def test_create_orm(self, setup):
        item = Pets(
                nickname = 'Шарик',
                kind = 'Собака',
                is_male = True
            )
        self.postgres.session.add(item)
        self.postgres.session.commit()

        res = self.postgres.session.query(Pets).filter_by(nickname='Шарик').all()
        assert len(res) == 1

        self.postgres.close_connection()