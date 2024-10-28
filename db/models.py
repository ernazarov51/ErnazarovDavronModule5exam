from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr, Session

from db.config import engine

from sqlalchemy import create_engine
engine=engine
engine=create_engine(engine)
engine.connect()

class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()+'s'
class HomeBase(Base):
    __abstract__=True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

class User(HomeBase):
    first_name:Mapped[str]=mapped_column(nullable=True)
    phone_number:Mapped[str]=mapped_column(nullable=True)
    user_name:Mapped[str]=mapped_column(nullable=True)
    adress:Mapped[str]=mapped_column(nullable=True)
    jinsi:Mapped[str]=mapped_column(nullable=True)


Base.metadata.create_all(engine)
engine.dispose()
session = Session(engine)

class Models:
    User=User


