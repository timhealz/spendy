from datetime import datetime

from sqlalchemy import(
    MetaData,
    Table,
    Column,
    ForeignKey,
    Numeric,
    BigInteger,
    String,
    Date,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from spendy.db.models.bank_account import BankAccount
from spendy.db.utils import get_db_engine, get_process_ts


Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transactions_log'

    id = Column(BigInteger, primary_key=True)
    ds = Column(Date)
    account_id = Column(String(50), ForeignKey(BankAccount.id))
    transaction_type = Column(String(50))
    description = Column(String(100))
    amount = Column(Numeric(10, 2))
    category = Column(String(100))
    process_ts = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return f"<Transaction(ds='{self.ds}', description='{self.description}', amount={self.amount})>"

    def get_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


if __name__ == "__main__":
    db_engine = get_db_engine()
    Base.metadata.create_all(db_engine)
