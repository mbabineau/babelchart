import boto

from ..models import TimeSeries, DataPoint


class CloudWatchSource(object):

    AVAILABLE_STATISTICS = ['Minimum', 'Maximum', 'Sum', 'Average', 'SampleCount']

    def __init__(self, aws_access_key_id, aws_secret_access_key, **kwargs):
        self.connection = boto.connect_cloudwatch(aws_access_key_id, aws_secret_access_key, **kwargs)

    @classmethod
    def to_series(self, cloudwatch_result, label_prefix='', label_map=None):
        """
        :type cloudwatch_result: list[dict]
        :param cloudwatch_result: Raw CloudWatch output from boto

        :type label_prefix: str
        :param label_prefix: Label prefix for each resulting time series. Concatenated with discovered statistics
        (e.g., 'myprefix ' becomes 'myprefix Sum'). Overridden by :label_map:

        :type label_map: dict[str, str]
        :param label_map: Map of statistics to labels. Example: {'Sum': 'mysum', 'Maximum': 'mymax'}. Overrides :label_prefix:
        """

        if not label_map: label_map = {stat: label_prefix+stat for stat in CloudWatchSource.AVAILABLE_STATISTICS}

        series = {}
        for r in cloudwatch_result:
            for stat in CloudWatchSource.AVAILABLE_STATISTICS:
                if stat in r:
                    if not stat in series: series[stat] = TimeSeries(label_map[stat])
                    series[stat].add_point(DataPoint(r['Timestamp'], r[stat]))

        return [series[k] for k in series]