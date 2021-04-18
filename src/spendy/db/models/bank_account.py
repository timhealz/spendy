from sqlalchemy import (
    Column,
    String,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from spendy.db.utils import get_db_engine


Base = declarative_base()


class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(String(50), primary_key=True)
    bank = Column(String(50))
    owner = Column(String(50))
    type = Column(String(50))
    description = Column(String(100))
    ledger_account = Column(String(100))
    process_ts = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return f"<BankAccount(bank='{self.bank}', owner='{self.owner}', type={self.type})>"


if __name__ == "__main__":
    db_engine = get_db_engine()
    Base.metadata.create_all(db_engine)
