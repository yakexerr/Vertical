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

def test_api_create_with_all_args():
    client = APIClient()
    park_data = {
        'title': "Bla",
        'city': "Tmz",
        'address': "Pushkina",
        "description": "Описание",
        "is_work": "true",
        "schedule": "11:00 - 21:00"
    }
    response = client.post('/api/v1/parks/', data=park_data)
    assert response.status_code == 201
    assert Park.objects.count() == 1
    assert response.data['title'] == 'Bla'


def test_retrieve_existing_park_returns_200():
    client = APIClient()
    park_data = {
        'title': "Bla",
        'city': "Tmz",
        'address': "Pushkina",
        "description": "Описание",
        "is_work": True,
        "schedule": "11:00 - 21:00"
    }

    test_park = Park.objects.create(**park_data)
    url = f'/api/v1/parks/{test_park.id}/'
    response = client.get(url)

    assert response.status_code == 200


def test_retrieve_non_existing_park_returns_404():
    client = APIClient()

    url = f'/api/v1/parks/999/'
    response = client.get(url)

    assert response.status_code == 404


def test_update_park_succeeds_new_title():
    client = APIClient()
    updated_data = {
        'title': "Ble",
    }

    park_data = {
        'title': "Bla",
        'city': "Tmz",
        'address': "Pushkina",
        "description": "Описание",
        "is_work": True,
        "schedule": "11:00 - 21:00"
    }
    park = Park.objects.create(**park_data)

    url = f'/api/v1/parks/{park.id}/'
    response = client.patch(url, data=updated_data)

    assert response.status_code == 200
    assert response.data['title'] == "Ble"
    park.refresh_from_db() # обновил
    assert park.title == "Ble"


def test_update_park_succeeds_new_all():
    client = APIClient()
    park_data = {
    'title': "Bla",
    'city': "Tmz",
    'address': "Pushkina",
    "description": "Описание",
    "is_work": True,
    "schedule": "11:00 - 21:00"
    }
    updated_data = {
        'title': "Ble",
        'city': "Tmzz",
        'address': "Pushkinaa",
        "description": "Описаниее",
        "is_work": False,
        "schedule": "12:00 - 21:00"
    }
        
    park = Park.objects.create(**park_data)

    url = f'/api/v1/parks/{park.id}/'
    response = client.patch(url, data=updated_data)

    assert response.status_code == 200
    assert response.data['title'] == "Ble"
    park.refresh_from_db() # обновил
    assert park.title == "Ble"
    assert park.city == "Tmzz"
    assert park.description == "Описаниее"


def test_delete_park_succeeds():
    park_data = {
    'title': "Bla",
    'city': "Tmz",
    'address': "Pushkina",
    "description": "Описание",
    "is_work": True,
    "schedule": "11:00 - 21:00"
    }
    client = APIClient()
    park = Park.objects.create(**park_data)
    url = f"/api/v1/parks/{park.id}/"

    response = client.delete(url)

    assert response.status_code == 204
    assert Park.objects.count() == 0