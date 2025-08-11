import pytest
from rest_framework.test import APIClient
from .models import Park, Entertainment
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db

class TestParkAPI:
    def test_parks_api_returns_200(self):
        '''
        Проверит, что эндпоинт парков возвразает статус 200 ОК.
        '''
        client = APIClient()
        response = client.get('/api/v1/parks/')

        assert response.status_code == 200

    def test_api_create_park_without_title_fails(self):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
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

    def test_api_create_with_all_args(self):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
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


    def test_retrieve_existing_park_returns_200(self):
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


    def test_retrieve_non_existing_park_returns_404(self):
        client = APIClient()

        url = f'/api/v1/parks/999/'
        response = client.get(url)

        assert response.status_code == 404


    def test_update_park_succeeds_new_title(self):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
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


    def test_update_park_succeeds_new_all(self):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
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


    def test_delete_park_succeeds(self):
        park_data = {
        'title': "Bla",
        'city': "Tmz",
        'address': "Pushkina",
        "description": "Описание",
        "is_work": True,
        "schedule": "11:00 - 21:00"
        }
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
        park = Park.objects.create(**park_data)
        url = f"/api/v1/parks/{park.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Park.objects.count() == 0


class TestEntertainmentAPI:
    def test_api_entertainments_list_return_200(self):
        client = APIClient()
        response = client.get('/api/v1/entertainments/')
        assert response.status_code == 200


    def test_api_create_entertainment_succesed(self):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
        test_park = Park.objects.create(title='Тестовый парк', city='Тестоград')
        entertainment_data = {
            'park': test_park.id,
            'title': 'Тестовое развлечение',
            'description': 'bleblablu',
            'min_height': '123',
            'price': 150.00
        } 
        responce = client.post('/api/v1/entertainments/', data=entertainment_data)
        assert responce.status_code == 201
        assert Entertainment.objects.count() == 1
        assert responce.data['title'] == 'Тестовое развлечение'

    def test_api_create_entertainments_without_title(self):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
        entertainment_data = {
            
            'title': 'ble',
            'description': 'blu',
            'min_height': 1,
            'price': 2
        }
        responce = client.post('/api/v1/entertainments/', data=entertainment_data)
        assert responce.status_code == 400
        assert Park.objects.count() == 0


    def test_api_retrieve_entertainment_successed(self):
        client = APIClient()
        test_park_data = Park.objects.create(title='Тестовый парк', city='Тестоград')
        test_entertainment = Entertainment.objects.create(
            park=test_park_data,
            title='Тестовое развлечение',
            price=150.00
            )
        
        url = f'/api/v1/entertainments/{test_entertainment.id}/'
        responce = client.get(url)

        assert responce.status_code == 200
        assert responce.data['title'] == 'Тестовое развлечение'


    def test_api_retrieve_not_exiting_entertainment_fails(self):
        client = APIClient()

        url = f'/api/v1/entertainments/999/'
        responce = client.get(url)

        assert responce.status_code == 404


    def test_api_update_entertainment_succeed(self):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
        test_park = Park.objects.create(title='Тестовый парк', city='Тестоград')

        entertainment_to_update = Entertainment.objects.create(
            park = test_park,
            title='Тестовый парк 1',
            price=150.0
        ) 
        update_edata = {
            'title': "Тестовый парк 2",
            'price': 152.00
        }

        url = f'/api/v1/entertainments/{entertainment_to_update.id}/'

        response = client.patch(url, data=update_edata)

        assert response.status_code == 200
        assert response.data['title'] == "Тестовый парк 2"
        assert response.data['price'] == '152.00'

        entertainment_to_update.refresh_from_db()
        assert entertainment_to_update.title == "Тестовый парк 2"


    def test_api_delete_entertainment_succeds(seld):
        test_user = User.objects.create_user(username="testuser", password='123')
        client = APIClient()
        client.force_authenticate(user=test_user)
        test_park = Park.objects.create(title='Тестовый парк', city='Тестоград')

        test_entertainment = Entertainment.objects.create(
            park = test_park,
            title='Тестовый парк 1',
            price=150.0
        )

        url = f'/api/v1/entertainments/{test_entertainment.id}/'
        response = client.delete(url)
        
        assert response.status_code == 204
        assert Entertainment.objects.count() == 0