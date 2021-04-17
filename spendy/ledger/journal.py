import os

from argparse import ArgumentParser

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import extract

from spendy.db.utils import get_db_engine
from spendy.db.models.transaction import Transaction
from spendy.db.models.bank_account import BankAccount
from spendy import SPENDY_HOME


DATA_DIR = os.path.join(SPENDY_HOME, "data")
JOURNAL_DIR = os.path.join(SPENDY_HOME, "journals")

JOURNAL_ENTRY = """
{date}  {description}
    {to_account}  {amount}
    {from_account}

"""


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-y", "--year",
                        help="Year to process data for."
                        )
    parser.add_argument("-m", "--month",
                        help="Month to process data for."
                        )
    args = parser.parse_args()

    Session = sessionmaker(bind=get_db_engine(database='spendy'))
    session = Session()

    transactions = session.query(Transaction, BankAccount).\
        filter(Transaction.account_id == BankAccount.id).\
        filter(extract('year', Transaction.ds) == args.year).\
        filter(extract('month', Transaction.ds) == args.month).\
        order_by(Transaction.ds).\
        all()

    with open(os.path.join(JOURNAL_DIR, args.year, f"{args.month}.ldg"), "w") as f:
        f.write(
            f"# GENERATED FILE - EDITS WILL BE OVERWRITTEN!\n")
        for transaction, bank_account in transactions:
            f.write(JOURNAL_ENTRY.format(
                date=transaction.ds,
                description=transaction.description,
                to_account='PLACEHOLDER',
                from_account=bank_account.ledger_account,
                amount=-transaction.amount
            ))
