from collections import defaultdict

try:
    import gviz_api
except ImportError:
    from ..dependencies import gviz_api


class GoogleChartsSink(object):

    @classmethod
    def from_series(self, series):
        """
        :type series: list[TimeSeries]
        :param series: Collection of TimeSeries objections from which to generate the Google Charts Data Table
        """

        labels = []
        zipped_data = defaultdict(dict)
        for s in series:
            labels.append(s.label)

            for point in s.data:
                zipped_data[point.dt][s.label] = point

        table_description = [('Date', 'datetime')]
        for label in labels:
            table_description.append((label, 'number'))
            table_description.append((label+' note', 'string'))

        table_data = []
        for dt,d in zipped_data.items():
            row = [dt]
            for label in labels:
                row += (d[label].value, d[label].note) if label in d else (None, None)

            table_data.append(row)

        data_table = gviz_api.DataTable(table_description, table_data)
        return data_table.ToJSonResponse()
