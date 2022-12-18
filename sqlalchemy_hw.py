import sqlalchemy
import json
from pprint import pprint
import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import Publisher, Book, Shop, Stock, Sale, create_tables

Base = declarative_base()

DSN = 'postgresql://postgres:Guj4_kow@localhost:5432/books_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open ('fixtures.json', 'r', encoding='utf-8') as f:
  text = json.load(f)
  pprint(text)

# pub1 = Publisher(name="Иванов")
# pub2 = Publisher(name="Петров")
# pub3 = Publisher(name="Васильев")
# session.add_all([pub1, pub2, pub3])
# session.commit()
#
# book1 = Book(title='Обо всем', id_publisher='1')
# book2 = Book(title='123', id_publisher='1')
# book3 = Book(title='678', id_publisher='2')
# book4 = Book(title='79', id_publisher='3')
# session.add_all([book1, book2, book3, book4])
# session.commit()
#
# shop1 = Shop(name='универмаг')
# shop2 = Shop(name='Книжный магазин')
# session.add_all([shop1, shop2])
# session.commit()
#
# stock1 = Stock(id_book=1, id_shop=2, count=30)
# stock2 = Stock(id_book=2, id_shop=2, count='26')
# stock3 = Stock(id_book='3', id_shop='1', count='267')
# stock4 = Stock(id_book='4', id_shop='1', count='76')
# session.add_all([stock1, stock2, stock3, stock4])
# session.commit()
#
# sale1 = Sale(price='10', date_sale='10.12.2013', id_stock='1', count='4')
# sale2 = Sale(price='15', date_sale='10.04.2013', id_stock='2', count='7')
# sale3 = Sale(price='18', date_sale='16.12.2013', id_stock='3', count='43')
# sale4 = Sale(price='7', date_sale='16.12.2010', id_stock='4', count='8')
# session.add_all([sale1, sale2, sale3, sale4])
# session.commit()
#
# session.close()
#
# def get_sales():
#     input_publisher_name = input('Введите имя издателя, факты покупки книг которого вы хотиите получь: ')
#     query = session.query(Book.title, Shop.name, Stock, Sale.price, Sale.date_sale)
#     query = query.join(Sale)
#     query = query.join(Shop)
#     query = query.join(Book)
#     query = query.join(Publisher).filter(Publisher.name == input_publisher_name)
#     record = query.all()
#
#     for r in record:
#         print(f'Книга "{r[0]}" куплена в магазине  "{r[1]}" стоимостью "{r[3]}", дата покупки "{r[4]}"')
#
# get_sales()

# new_record = Publisher(name='Пушкин')
# session.add(new_record)
# session.commit()

# def main():
#     DSN = 'postgresql://postgres:Guj4_kow@localhost:5432/books_db'
#     engine = create_engine(DSN)
#     Base.metadata.create_all(engine)
#
#     Session = sessionmaker(bind=engine)
#     session = Session()
#
#     new_record = Publisher(name='Пушкин')
#     session.add(new_record)
#     session.commit()
#
#
# if __name__ == "__main__":
#      main()
