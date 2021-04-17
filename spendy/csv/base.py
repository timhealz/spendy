import csv
import os
from typing import Dict
from abc import ABC, abstractmethod

from spendy.db.models.transaction import Transaction


class BaseCSVHandler(ABC):
    def __init__(self, account_id: str, data_dir: str):
        super().__init__()
        self.account_id = account_id
        self.csv_filepath = os.path.join(data_dir, f"{account_id}.csv")

    @abstractmethod
    def get_transaction(self, row: Dict) -> Transaction:
        pass

    def process_csv(self):
        with open(self.csv_filepath) as csvfile:
            csv_reader = csv.DictReader(csvfile, quotechar='"')
            for row in csv_reader:
                yield self.get_transaction(row)
