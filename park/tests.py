import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

def test_parks_api_returns_200():
    '''
    Проверит, что эндпоинт парков возвразает статус 200 ОК.
    '''
    client = APIClient()
    response = client.get('/api/v1/parks/')

    assert response.status_code == 200