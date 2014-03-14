from datetime import datetime
import unittest

from babelchart.models import TimeSeries, DataPoint
from babelchart.sinks.googlecharts import GoogleChartsSink


INPUT_SERIES = [
    TimeSeries('foo', [
        DataPoint(datetime.utcfromtimestamp(1390100000), 1),
        DataPoint(datetime.utcfromtimestamp(1390200000), 2, "crazy foo event"),
        DataPoint(datetime.utcfromtimestamp(1390500000), 5)
    ]),
    TimeSeries('bar', [
        DataPoint(datetime.utcfromtimestamp(1390100000), 10),
        DataPoint(datetime.utcfromtimestamp(1390300000), 30),
        DataPoint(datetime.utcfromtimestamp(1390400000), 40),
        DataPoint(datetime.utcfromtimestamp(1390500000), 50, "normal bar event")
    ])
]

EXPECTED_OUTPUT = 'google.visualization.Query.setResponse({"status":"ok","table":{"rows":[{"c":[{"v":"Date(2014,0,22,14,13,20)"},null,null,{"v":40},null]},{"c":[{"v":"Date(2014,0,19,2,53,20)"},{"v":1},null,{"v":10},null]},{"c":[{"v":"Date(2014,0,21,10,26,40)"},null,null,{"v":30},null]},{"c":[{"v":"Date(2014,0,20,6,40,0)"},{"v":2},{"v":"crazy foo event"},null,null]},{"c":[{"v":"Date(2014,0,23,18,0,0)"},{"v":5},null,{"v":50},{"v":"normal bar event"}]}],"cols":[{"type":"datetime","id":"Date","label":"Date"},{"type":"number","id":"foo","label":"foo"},{"type":"string","id":"foo note","label":"foo note"},{"type":"number","id":"bar","label":"bar"},{"type":"string","id":"bar note","label":"bar note"}]},"reqId":"0","version":"0.6"});'

class TestGoogleChartsSink(unittest.TestCase):

    def test_from_series(self):
        result = GoogleChartsSink.from_series(INPUT_SERIES)
        self.assertEqual(result, EXPECTED_OUTPUT)
