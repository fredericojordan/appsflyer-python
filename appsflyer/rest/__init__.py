import json
import logging

import requests

LOGGER = logging.getLogger(__name__)


class Client(object):
    """ A client for accessing the AppsFlyer S2S API. """

    def __init__(self, app_id=None, dev_key=None):
        """
        Initializes the AppsFlyer Client

        :param str app_id: Your AppsFlyer App ID
        :param str dev_key: Your AppsFlyer dev_key

        :returns: AppsFlyer Client
        :rtype: appsflyer.rest.Client
        """

        self.app_id = app_id
        """ :type : str """
        self.dev_key = dev_key
        """ :type : str """

        if not app_id or not dev_key:
            raise Exception(
                "app_id and dev_key are required to create an AppsFlyerClient"
            )

    def api_base_uri(self):
        return f"https://api2.appsflyer.com/inappevent/{self.app_id}"

    def request(self, data=None, headers=None):
        """
        Makes a POST request to the AppsFlyer API using provided payload data

        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers

        :returns: Response from AppsFlyer API
        :rtype: requests.models.Response
        """
        headers = headers or {}
        headers["Content-Type"] = "application/json"
        headers["authentication"] = f"{self.dev_key}"

        return requests.post(
            self.api_base_uri(), data=json.dumps(data), headers=headers
        )

    def generate_event(
        self,
        appsflyer_id=None,
        customer_user_id=None,
        att=None,
        ip=None,
        event_name=None,
        event_value=None,
        app_version_name=None,
        app_store=None,
        event_time=None,
        event_currency=None,
        bundle_identifier=None,
        sharing_filter=None,
        custom_dimension=None,
        app_type=None,
        custom_data=None,
        **kwargs,
    ):
        event_data = {
            "appsflyer_id": appsflyer_id,
            "customer_user_id": customer_user_id,
            "att": att,
            "ip": ip,
            "eventName": event_name,
            "eventValue": event_value,
            "app_version_name": app_version_name,
            "app_store": app_store,
            "eventTime": event_time,
            "eventCurrency": event_currency,
            "bundleIdentifier": bundle_identifier,
            "sharing_filter": sharing_filter,
            "custom_dimension": custom_dimension,
            "app_type": app_type,
            "custom_data": custom_data,
        }

        event_data = {
            key: value for key, value in event_data.items() if value is not None
        }
        event_data.update(kwargs)

        return self.request(data=event_data)
