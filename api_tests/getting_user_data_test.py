import pytest
import requests


@pytest.mark.api
def test_getting_user_data(base_api_url, login_data, logger):
    params = {"email": login_data['valid_credentials']['username']}
    response = requests.get(f"{base_api_url}getUserDetailByEmail", params=params)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    assert data["user"]["id"] == 584904
    assert data["user"]["name"] == "testPlaywright"