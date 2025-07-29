import pytest
from rest_framework.test import APIClient
from .models import Park, Entertainment

pytestmark = pytest.mark.django_db

def test_parks_api_returns_200():
    '''
    Проверит, что эндпоинт парков возвразает статус 200 ОК.
    '''
    client = APIClient()
    response = client.get('/api/v1/parks/')

    assert response.status_code == 200

def test_api_create_park_without_title_fails():
    client = APIClient()
    park_data = {
        'city': "Tmz",
        'address': "Pushkina",
        "description": "Описание",
        "is_work": "true",
        "schedule": "11:00 - 21:00"
    }

    response = client.post('/api/v1/parks/', data=park_data)
    assert response.status_code == 400
    assert Park.objects.count() == 0

