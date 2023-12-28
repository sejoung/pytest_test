"""pymongo 테스트"""
import logging

import pymongo
from testcontainers.mongodb import MongoDbContainer

logger = logging.getLogger(__name__)


def test_mongodb_container():
    """mongodb 컨테이너 테스트"""
    mongodb_container = MongoDbContainer("mongo:4.0.10")
    with mongodb_container as mongodb:
        client = pymongo.MongoClient(mongodb.get_connection_url())
        result = client.admin.command("ping")
        logger.info(result)

        assert result["ok"] == 1.0


def test_insert():
    """mongodb 컨테이너 테스트"""
    mongodb_container = MongoDbContainer("mongo:4.0.10")
    with mongodb_container as mongodb:
        client = pymongo.MongoClient(mongodb.get_connection_url())
        result = client["test_db"]["test_collection"].insert_one({"test": "test"})
        inserted_id = result.inserted_id
        logger.info(inserted_id)
        assert inserted_id is not None


def test_select():
    """mongodb 컨테이너 테스트"""
    mongodb_container = MongoDbContainer("mongo:4.0.10")
    with mongodb_container as mongodb:
        client = pymongo.MongoClient(mongodb.get_connection_url())
        result = client["test_db"]["test_collection"].insert_one({"test": "test"})
        inserted_id = result.inserted_id
        actual = client["test_db"]["test_collection"].find_one({"_id": inserted_id})
        logger.info(actual)
        assert actual["test"] == "test"
