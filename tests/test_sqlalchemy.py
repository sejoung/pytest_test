"""SQLAlchemy 테스트"""
import logging

import sqlalchemy
from testcontainers.postgres import PostgresContainer

logger = logging.getLogger(__name__)


def test_sqlalchemy():
    """SQLAlchemy 테스트"""
    assert sqlalchemy.__version__ == "2.0.23"


def test_postgres_container():
    """PostgreSQL 컨테이너 테스트"""
    postgres_container = PostgresContainer("postgres:9.5")
    with postgres_container as postgres:
        engine = sqlalchemy.create_engine(postgres.get_connection_url())
        with engine.begin() as connection:
            result = connection.execute(sqlalchemy.text("select version()"))
            for row in result:
                logger.info(row)
                assert row[0].lower().startswith("postgresql 9.5")
