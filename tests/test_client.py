import pytest
import requests
from appsflyer.rest import Client


def test_invalid_client():
    with pytest.raises(Exception) as exception:
        Client(app_id="", dev_key="")

    assert (
        str(exception.value)
        == "app_id and dev_key are required to create an AppsFlyerClient"
    )


def test_base_uri():
    client = Client(app_id="420", dev_key="some-key")
    assert client.api_base_uri() == "https://api2.appsflyer.com/inappevent/420"


def test_generate_simple_payload(mocker):
    mocker.patch("appsflyer.rest.Client.request")
    client = Client(app_id="420", dev_key="some-key")
    client.generate_event(event_name="ok")
    Client.request.assert_called_once_with(data={"eventName": "ok"})


def test_generate_complete_payload(mocker):
    mocker.patch("appsflyer.rest.Client.request")
    client = Client(app_id="420", dev_key="some-key")
    client.generate_event(
        appsflyer_id="9999999999999-9999999999999999999",
        customer_user_id="example_customer_id_123",
        att="example_att",
        ip="199.0.2.1",
        app_version_name="example_version_name",
        app_store="example_app_store",
        app_type="example_app_type",
        event_time="2020-04-20 16:20.000",
        event_name="af_purchase",
        event_currency="ZAR",
        event_value={
            "af_revenue": "1006",
            "af_content_type": "wallets",
            "af_content_id": "15854",
            "af_quantity": "1",
        },
        bundle_identifier="example_bundle_identifier",
        sharing_filter="example_sharing_filter",
        custom_dimension="example_custom_dimension",
        custom_data="example_custom_data",
        idfa="9876F1SS-2983-3855-27RR-2R626772VFNB",
    )
    Client.request.assert_called_once_with(
        data={
            "appsflyer_id": "9999999999999-9999999999999999999",
            "customer_user_id": "example_customer_id_123",
            "att": "example_att",
            "ip": "199.0.2.1",
            "eventName": "af_purchase",
            "eventValue": {
                "af_content_id": "15854",
                "af_content_type": "wallets",
                "af_quantity": "1",
                "af_revenue": "1006",
            },
            "app_version_name": "example_version_name",
            "app_store": "example_app_store",
            "eventTime": "2020-04-20 16:20.000",
            "eventCurrency": "ZAR",
            "bundleIdentifier": "example_bundle_identifier",
            "sharing_filter": "example_sharing_filter",
            "custom_dimension": "example_custom_dimension",
            "app_type": "example_app_type",
            "custom_data": "example_custom_data",
            "idfa": "9876F1SS-2983-3855-27RR-2R626772VFNB",
        }
    )


def test_generate_event_with_invalid_dev_key():
    client = Client(app_id="420", dev_key="some-key")
    response = client.generate_event(event_name="my-event")
    assert type(response) == requests.models.Response
    assert response.status_code == 403
