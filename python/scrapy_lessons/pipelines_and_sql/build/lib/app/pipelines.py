# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import scrapy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from .config import db
from . import models as M


class AppPipeline:
    def process_item(self, item, spider):
        return item


class PriceToTHBPipeline:
    rub_to_thb = 2.75

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("price"):
            float_price = float(adapter["price"])
            adapter["price"] = float_price / self.rub_to_thb
            return item
        else:
            raise DropItem(f"Missing price to this item")


class DuplicatesPipeline:
    def __init__(self):
        self.unique_titles = set()

    def process_item(self, item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)

        if (name := adapter["title"]) in self.unique_titles:
            raise DropItem(f"Duplicate item found: {name}")
        else:
            self.unique_titles.add(name)
            spider.logger.info(f"add new item: {name}")
            return item


class SavingToMysqlPipeline:
    def __init__(self):
        engine = create_engine(db.url)
        self.create_db()
        self.session_maker = sessionmaker(bind=engine)

    def create_db(self):
        alembic_cfg = Config("alembic.ini")
        command.downgrade(alembic_cfg, "base")
        command.upgrade(alembic_cfg, "head")
        alembic_cfg.set_section_option("logger_alembic", "level", "DEBUG")

    def process_item(self, item, spider: scrapy.Spider):
        with self.session_maker() as session:
            with session.begin():
                product = M.Product(**item)
                session.add(product)
                session.commit()
        spider.logger.info("INSERTED")

        return item
