import csv
import os
import unittest

from datetime import datetime

from spendy.csv.handlers import (
    AllyCSVHandler,
    ChaseCSVHandler,
    AmexCSVHandler,
    TargetCSVHandler
)


RESOURCES = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../resources'
)


class TestAllyCSVHandler(unittest.TestCase):

    ally = AllyCSVHandler(
        account_id="test_ally",
        data_dir=RESOURCES
    )

    def test_process_csv(self):
        test = next(self.ally.process_csv())
        self.assertEqual(
            test.ds,
            datetime(2021, 1, 25, 0, 0)
        )
        self.assertEqual(test.account_id, "test_ally")
        self.assertEqual(test.description, "test")
        self.assertEqual(test.amount, -50.00)
        self.assertEqual(test.category, None)


class TestChaseCSVHandler(unittest.TestCase):

    chase = ChaseCSVHandler(
        account_id="test_chase",
        data_dir=RESOURCES
    )

    def test_process_csv(self):
        test = next(self.chase.process_csv())
        self.assertEqual(
            test.ds,
            datetime(2021, 1, 26, 0, 0)
        )
        self.assertEqual(test.account_id, "test_chase")
        self.assertEqual(test.transaction_type, "Sale")
        self.assertEqual(test.description, "test chase")
        self.assertEqual(test.amount, -14.95)
        self.assertEqual(test.category, "Bills & Utilities")


class TestAmexCSVHandler(unittest.TestCase):

    amex = AmexCSVHandler(
        account_id="test_amex",
        data_dir=RESOURCES
    )

    def test_process_csv(self):
        test = next(self.amex.process_csv())
        self.assertEqual(
            test.ds,
            datetime(2021, 1, 31, 0, 0)
        )
        self.assertEqual(test.account_id, "test_amex")
        self.assertEqual(test.transaction_type, None)
        self.assertEqual(test.description,
                         "LUCKY #780.SUNNYVALESUNNYVALE           CA")
        self.assertEqual(test.amount, -60)
        self.assertEqual(test.category, "Merchandise & Supplies-Groceries")


class TestTargetCSVHandler(unittest.TestCase):

    target = TargetCSVHandler(
        account_id="test_target",
        data_dir=RESOURCES
    )

    def test_process_csv(self):
        test = next(self.target.process_csv())
        self.assertEqual(
            test.ds,
            datetime(2021, 1, 25, 0, 0)
        )
        self.assertEqual(test.account_id, "test_target")
        self.assertEqual(test.transaction_type, "Sales Draft")
        self.assertEqual(test.description, "Grocery Stores  Supermarkets")
        self.assertEqual(test.amount, -50)
        self.assertEqual(test.category, "Groceries")


if __name__ == '__main__':
    unittest.main()
