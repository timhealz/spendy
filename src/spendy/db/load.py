#!/home/timhealz/code/spendy/env_spendy/bin python

import os
import re

from argparse import ArgumentParser

from sqlalchemy import delete
from sqlalchemy.sql.expression import extract
from sqlalchemy.orm import sessionmaker

from spendy.db.utils import get_db_engine
from spendy.db.models.transaction import Transaction
from spendy.db.models.bank_account import BankAccount
from spendy.csv.handlers import (
    AllyCSVHandler,
    ChaseCSVHandler,
    AmexCSVHandler,
    TargetCSVHandler
)
from spendy import SPENDY_HOME

SPENDY_DATA = os.path.join(SPENDY_HOME, "data")


def get_csv_handler(bank: str):
    bank = bank.lower()

    if bank == "ally":
        return AllyCSVHandler
    elif bank == "chase":
        return ChaseCSVHandler
    elif bank in ("amex", "american express"):
        return AmexCSVHandler
    elif bank == "target":
        return TargetCSVHandler
    else:
        raise RuntimeError(
            f"Bank csv handler not found for {bank}! Please create one.")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-y", "--year",
                        help="Year to process data for."
                        )
    parser.add_argument("-m", "--month",
                        help="Month to process data for."
                        )
    parser.add_argument("-a", "--account_id",
                        help="Account ID to process data for."
                        )
    args = parser.parse_args()

    Session = sessionmaker(bind=get_db_engine())
    session = Session()

    print(
        f"Clearing out data - account: {args.account_id}, year: {args.year}, month: {args.month}")
    session.query(Transaction).\
        filter(extract('year', Transaction.ds) == args.year).\
        filter(extract('month', Transaction.ds) == args.month).\
        filter(Transaction.account_id == args.account_id).\
        delete(synchronize_session=False)

    bank = re.search(r'(.*?)_(.*?)_(.*?)', args.account_id).group(1)

    print(f"Loading: {args.account_id}")
    csv_handler = get_csv_handler(bank=bank)(
        account_id=args.account_id,
        data_dir=os.path.join(SPENDY_DATA, args.year, args.month)
    )

    for transaction in csv_handler.process_csv():
        session.add(transaction)

    session.commit()
