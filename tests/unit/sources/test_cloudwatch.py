import datetime
import unittest

from babelchart.sources.cloudwatch import CloudWatchSource


CLOUDWATCH_RESULT = [
    {u'SampleCount': 5.0, u'Timestamp': datetime.datetime(2014, 2, 27, 19, 6), u'Average': 0.614, u'Unit': u'Percent'},
    {u'SampleCount': 5.0, u'Timestamp': datetime.datetime(2014, 2, 27, 19, 1), u'Average': 0.65, u'Unit': u'Percent'},
    {u'SampleCount': 5.0, u'Timestamp': datetime.datetime(2014, 2, 27, 18, 51), u'Average': 0.526, u'Unit': u'Percent'},
    {u'SampleCount': 5.0, u'Timestamp': datetime.datetime(2014, 2, 27, 18, 56), u'Average': 0.8939999999999999, u'Unit': u'Percent'}
]

class TestCloudWatchSource(unittest.TestCase):

    def test_to_series(self):
        tss = CloudWatchSource.to_series(CLOUDWATCH_RESULT)
        sorted_cw_result = sorted(CLOUDWATCH_RESULT, key=lambda x: x['Timestamp'])

        self.assertSetEqual(set([t.label for t in tss]), set(['Average', 'SampleCount']))

        for t in tss:
            for i in range(0, len(sorted_cw_result)):
                self.assertEqual(t.data[i].dt, sorted_cw_result[i]['Timestamp'])
                self.assertEqual(t.data[i].value, sorted_cw_result[i][t.label])
