from datetime import datetime
from sqlalchemy import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from config import engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker


Base = declarative_base()


class Status(Base):
    __tablename__ = 'status'

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str]
    coin: Mapped[str]
    amount: Mapped[float]
    proxy: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)


class CRUD:
    def __init__(self, session = None) -> None:
        if not session:
            self.session = sessionmaker(engine)
        else:
            self.session = session
    
    def drop_table(self):
        x = input('Вы уверены, что хотите удалить все таблицы бд? (y/n): ')

        if x == 'y':
            Base.metadata.drop_all(engine)
    
    def create_base(self):
        Base.metadata.create_all(engine)

    
    async def create_status(self, key: str, coin: str, amount: float, status: str, proxy: str = None):
        status = Status(key=key, coin=coin, amount=amount, proxy=proxy, status=status)
        
        with self.session() as session:
            session.add(status)
            session.commit()

