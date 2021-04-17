import csv

from datetime import datetime
from typing import Dict
from re import sub

from spendy.csv.base import BaseCSVHandler
from spendy.db.models.transaction import Transaction
import spendy.db.utils as utils


class AllyCSVHandler(BaseCSVHandler):

    def get_transaction(self, row: Dict) -> Transaction:
        return Transaction(
            id=utils.get_id("|".join(row.values())),
            ds=datetime.strptime(row["Date"], "%Y-%m-%d"),
            account_id=self.account_id,
            transaction_type=row[" Type"],
            description=row[" Description"],
            amount=float(row[" Amount"]),
            category=None,
        )


class ChaseCSVHandler(BaseCSVHandler):

    def get_transaction(self, row: Dict) -> Transaction:
        return Transaction(
            id=utils.get_id("|".join(row.values())),
            ds=datetime.strptime(row['Post Date'], '%m/%d/%Y'),
            account_id=self.account_id,
            transaction_type=row['Type'],
            description=row['Description'],
            amount=float(row['Amount']),
            category=row['Category']
        )


class AmexCSVHandler(BaseCSVHandler):

    def get_transaction(self, row: Dict) -> Transaction:
        return Transaction(
            id=utils.get_id("|".join(row.values())),
            ds=datetime.strptime(row['Date'], '%m/%d/%Y'),
            account_id=self.account_id,
            transaction_type=None,
            description=row['Description'],
            amount=-float(row['Amount']),
            category=row['Category']
        )


class TargetCSVHandler(BaseCSVHandler):

    @staticmethod
    def get_amount(amount: str) -> float:
        sign = 1 if amount[0] == "(" else -1
        return sign * float(sub(r'[^\d\-.]', '', amount))

    def get_transaction(self, row: Dict) -> Transaction:
        return Transaction(
            id=utils.get_id("|".join(row.values())),
            ds=datetime.strptime(row['Posting Date'], '%m/%d/%Y'),
            account_id=self.account_id,
            transaction_type=row['Transaction Type'],
            description=row['Description'],
            amount=self.get_amount(row['Amount']),
            category=row['Category']
        )
