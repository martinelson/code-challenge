import pytest


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    result = client.get('/api/parse/', data={'address': address_string})
    if result.status_code == 200:
        exp_string = b'{"input_string":"123 main st chicago il",'
        exp_comp = b'"components":{"AddressNumber":"123","StreetName":"main",'
        exp_comp_2 = b'"StreetNamePostType":"st","PlaceName":"chicago","StateName":"il"},'
        exp_type = b'"type":"Street Address"}'
        assert result.content == exp_string + exp_comp + exp_comp_2 + exp_type
    else:
        pytest.fail()


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    result = client.get('/api/parse/', data={'address': address_string})
    if result.status_code == 400:
        assert result.content == b'{"detail":"There was an issue parsing the address."}'
    else:
        pytest.fail()
