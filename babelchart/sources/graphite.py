from datetime import datetime

from ..models import TimeSeries, DataPoint


class GraphiteSource(object):

    @classmethod
    def _parse_data_point(self, data_tuple):
        (value, ts) = data_tuple
        return DataPoint(datetime.fromtimestamp(ts), value)

    @classmethod
    def to_series(self, graphite_result):
        """
        :type graphite_result: list[dict]
        :param graphite_result: Parsed json output from Graphite
        """

        series = []
        for r in graphite_result:
            data = [self._parse_data_point(d) for d in r['datapoints']]
            series.append(TimeSeries(r['target'], data))

        return series