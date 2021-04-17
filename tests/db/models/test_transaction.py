import unittest
from datetime import datetime

from spendy.db.models.transaction import Transaction

TEST_TRXN = {
    'id': None,
    'ds': datetime(2021, 1, 1),
    'account_id': 'gucci_th_ducats',
    'transaction_type': 'zed',
    'description': 'this is a test',
    'amount': 123.456,
    'category': 'Groceries',
    'process_ts': None
}


class TestTransaction(unittest.TestCase):

    transaction = Transaction(**TEST_TRXN)

    def test_init(self):
        self.assertEqual(
            self.transaction.ds,
            datetime(2021, 1, 1, 0, 0)
        )
        self.assertEqual(self.transaction.account_id, 'gucci_th_ducats')
        self.assertEqual(
            self.transaction.transaction_type,
            'zed'
        )
        self.assertEqual(
            self.transaction.description,
            'this is a test'
        )
        self.assertEqual(self.transaction.amount, 123.456)
        self.assertEqual(
            self.transaction.category,
            'Groceries'
        )

    def test_dict(self):
        print(self.transaction.get_dict())
        self.assertEqual(
            self.transaction.get_dict(),
            TEST_TRXN
        )


if __name__ == '__main__':
    unittest.main()
