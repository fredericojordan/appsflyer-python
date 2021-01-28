# appsflyer-python

[![PyPI](https://img.shields.io/pypi/v/appsflyer.svg)](https://pypi.python.org/pypi/appsflyer)

## Documentation

The documentation for AppsFlyer's Server-to-server events API for mobile can be found [here](https://support.appsflyer.com/hc/en-us/articles/207034486-Server-to-server-events-API-for-mobile-S2S-mobile-).

## Installation

Install using [`pip`](https://pypi.org/project/pip/):

```shell
pip install appsflyer
```

## Getting Started

To start generating events, we need only a `Client` instance.

The `Client` needs your AppsFlyer credentials. You can pass these directly to the constructor:

```python
from appsflyer.rest import Client

app_id = "XXXXXXXXXXXXXXXXX"
dev_key = "YYYYYYYYYYYYYYYY"

appsflyer_client = Client(app_id=app_id, dev_key=dev_key)
```

### Generating an Event

To generate an event, simply call `Client.generate_event()` with keyword arguments:

```python
from appsflyer.rest import Client

app_id = "XXXXXXXXXXXXXXXXX"
dev_key = "YYYYYYYYYYYYYYYY"

appsflyer_client = Client(app_id=app_id, dev_key=dev_key)

appsflyer_client.generate_event(
    appsflyer_id="9999999999999-9999999999999999999",
    customer_user_id="example_customer_id_123",
    ip="199.0.2.1",
    app_version_name="example_version_name",
    event_time="2020-02-25 12:00.000",
    event_name="af_purchase",
    event_currency="ZAR",
    event_value={
        "af_revenue": "1006",
        "af_content_type": "wallets",
        "af_content_id": "15854",
        "af_quantity": "1",
    },
)

```

The parameters `event_name`, `event_value` and `appsflyer_id` are mandatory.
