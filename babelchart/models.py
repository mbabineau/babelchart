import bisect
import calendar
from datetime import datetime


class DataPoint(object):

    def __init__(self, dt, value, note=None):
        """
        :type dt: datetime
        :param dt: Datetime associated with this data point

        :type value: float
        :param dt value: Scalar value of this data point

        :type note: string or None
        :param string note: Optional annotation associated with this point
        """
        self.dt = dt
        self.value = value
        self.note = note

    def __cmp__(self, other):
        return cmp(calendar.timegm(self.dt.utctimetuple()), calendar.timegm(other.dt.utctimetuple()))


class TimeSeries(object):

    def __init__(self, label=None, data=None):
        """
        :type label: string
        :param label: Label for this series. Should be unique per chart.

        :type data: list[DataPoint]
        :param data: Collection of data points comprising the time series
        """
        self.label = label
        self.data = [] if data is None else data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = sorted(value, key=lambda x: x.dt)

    def add_point(self, dp):
        """
        :type dp: DataPoint
        :param dp: New data point to be added to the series
        """
        bisect.insort(self.data, dp)