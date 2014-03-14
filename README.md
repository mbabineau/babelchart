# babelchart

## Introduction

babelchart simplifies the transformation of annotated time series data.

It is a Python library that acts as glue between data `sources` (such as Amazon CloudWatch or Graphite) and `sinks`
(such as Google Charts or Highcharts). It solves the problem of converting time series data from the source's format
into something usable by, say, a charting tool.

By providing a common interface for these transformations, babelchart makes it easy to add your own converters. Out of
the box, the following converters are included:

* sources
    * Amazon CloudWatch
    * Graphite
* sinks
    * Google Charts

babelchart is open source under the Apache 2.0 license.

## Installation

babelchart was developed using Python 2.7. That said, it should work on Python 2.6+.

You can install it via pip:

```bash
pip install babelchart
```

## Examples

##### Graphite -> Google Charts
```python
>>> # Fetch and parse the json response from Graphite
>>> import requests
>>> graphite_url = 'http://mygraphiteserver/render/?target=mymetrics.m1&target=&mymetrics.m2&format=json'
>>> graphite_result = requests.get(graphite_url).json()
>>>
>>> # Transform it into a list of TimeSeries objects
>>> from babelchart.sources.graphite import GraphiteSource
>>> tss = GraphiteSource.to_series(graphite_result)
>>>
>>> # Generate the Google Charts data response
>>> from babelchart.sinks.googlecharts import GoogleChartsSink
>>> GoogleChartsSink.from_series(tss)
'google.visualization.Query.setResponse({"status":"ok","table":{"rows":[{"c":[{"v":"Date(2014,2,4,16,0,0)"},{"v":1.62},null,{"v":0.54},null]},{"c":[{"v":"Date(2014,2,4,17,30,0)"},null,null,null,null]},{"c":[{"v":"Date(2014,2,4,17,0,0)"},{"v":1.51},null,{"v":0.54},null]},{"c":[{"v":"Date(2014,2,4,16,30,0)"},{"v":2.38},null,{"v":0.91},null]},{"c":[{"v":"Date(2014,2,4,15,30,0)"},{"v":1.42},null,{"v":0.63},null]}],"cols":[{"type":"datetime","id":"Date","label":"Date"},{"type":"number","id":"mymetrics.m1","label":"mymetrics.m1"},{"type":"string","id":"mymetrics.m1 note","label":"mymetrics.m1 note"},{"type":"number","id":"mymetrics.m2","label":"mymetrics.m2"},{"type":"string","id":"mymetrics.m2 note","label":"mymetrics.m2 note"}]},"reqId":"0","version":"0.6"});'
```

##### CloudWatch -> Google Charts
```python
>>> # Fetch the boto-parsed data from CloudWatch
>>> import boto, datetime
>>> c = boto.connect_cloudwatch()
>>> cloudwatch_result = c.get_metric_statistics(
...     900,
...     datetime.datetime.utcnow() - datetime.timedelta(hours=1),
...     datetime.datetime.utcnow(),
...     'CPUUtilization',
...     'AWS/EC2',
...     ['Average', 'Maximum'],
...     dimensions={'InstanceId':['i-78daf759']}
... )
>>>
>>> # Transform it into a list of TimeSeries objects
>>> from babelchart.sources.cloudwatch import CloudWatchSource
>>> tss = CloudWatchSource.to_series(cloudwatch_result)
>>>
>>> # Generate the Google Charts data response
>>> from babelchart.sinks.googlecharts import GoogleChartsSink
>>> GoogleChartsSink.from_series(tss)
'google.visualization.Query.setResponse({"status":"ok","table":{"rows":[{"c":[{"v":"Date(2014,2,5,17,38,0)"},{"v":2.543},null,{"v":3.16},null]},{"c":[{"v":"Date(2014,2,5,17,8,0)"},{"v":2.513},null,{"v":3.16},null]},{"c":[{"v":"Date(2014,2,5,16,53,0)"},{"v":2.567},null,{"v":3.03},null]},{"c":[{"v":"Date(2014,2,5,17,23,0)"},{"v":2.527},null,{"v":3.19},null]}],"cols":[{"type":"datetime","id":"Date","label":"Date"},{"type":"number","id":"Average","label":"Average"},{"type":"string","id":"Average note","label":"Average note"},{"type":"number","id":"Maximum","label":"Maximum"},{"type":"string","id":"Maximum note","label":"Maximum note"}]},"reqId":"0","version":"0.6"});'
```

