import unittest

from spendy.db.utils import get_id


class TestGetID(unittest.TestCase):

    def test_get_id(self):
        self.assertEqual(
            get_id('some random string'),
            7189773441855079
        )
