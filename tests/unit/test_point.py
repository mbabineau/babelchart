from datetime import datetime
import unittest

from babelchart.models import DataPoint


class TestDataPoint(unittest.TestCase):

    def test_comparison(self):
        sooner = DataPoint(datetime.utcfromtimestamp(1393450001), 0)
        later =  DataPoint(datetime.utcfromtimestamp(1393450005), 0)
        self.assertGreater(later, sooner)