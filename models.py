import sqlalchemy as sa

from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

DSN = 'postgresql://postgres:Guj4_kow@localhost:5432/books_db'
engine = sa.create_engine(DSN)

class Publisher(Base):
    __tablename__ = "publisher"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)

    def __str__(self):
        return f'Publisher {self.id} : {self.name}'

class Book(Base):

    __tablename__ = "book"
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='Book')

    def __str__(self):
        return f'Book {self.id} : ({self.title}, {self.id_publisher})'

class Shop(Base):

    __tablename__ = "shop"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)

    def __str__(self):
        return f'Shop {self.id} : ({self.name})'

class Stock(Base):
    __tablename__ = "stock"

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    id_book = sa.Column(sa.Integer, sa.ForeignKey('book.id'), nullable=False)
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False)
    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')


    def __str__(self):
        return f'Stock {self.id} : ({self.id_book}, {self.id_shop}, {self.id_publisher}, {self.count})'

class Sale(Base):

    __tablename__ = "sale"
    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Integer, nullable=False)
    date_sale = sa.Column(sa. DateTime, nullable=False)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey('stock.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False)
    stock = relationship(Stock, backref='sale')

    def __str__(self):
        return f'Sale {self.id} : ({self.price}, {self.date_sale}, {self.id_stock}, {self.count})'

def create_tables(engine):
    Base.metadata.create_all(engine)