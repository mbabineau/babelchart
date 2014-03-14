import calendar
from datetime import datetime
import unittest

from babelchart.models import TimeSeries


class MockDataPoint(object):

    def __init__(self, dt, value, note=None):
        self.dt = dt
        self.value = value
        self.note = note

    def __cmp__(self, other):
        return cmp(calendar.timegm(self.dt.utctimetuple()), calendar.timegm(other.dt.utctimetuple()))


class TestTimeSeries(unittest.TestCase):

    def test_sorting(self):
        data = [
            MockDataPoint(datetime.utcfromtimestamp(1393450002), 0),
            MockDataPoint(datetime.utcfromtimestamp(1393450001), 0),
            MockDataPoint(datetime.utcfromtimestamp(1393450005), 0),
        ]
        sorted_data = sorted(data, key=lambda x: x.dt)

        ts = TimeSeries("Test", data)
        self.assertEquals([x.dt for x in sorted_data], [x.dt for x in ts.data])

        p1 = MockDataPoint(datetime.utcfromtimestamp(1393450004), 0)
        p2 = MockDataPoint(datetime.utcfromtimestamp(1393450003), 0)

        data.append(p1)
        data.append(p2)
        sorted_data = sorted(data, key=lambda x: x.dt)

        ts.add_point(p1)
        ts.add_point(p2)
        self.assertEquals([x.dt for x in sorted_data], [x.dt for x in ts.data])