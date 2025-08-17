from django.shortcuts import render
import requests

def park_list(request):
    """
    Представление для отображения списка парков.
    """
    # Делаем GET-запрос к нашему собственному API
    api_url = "http://localhost:8000/api/v1/parks/"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Вызовет ошибку, если статус не 2xx
        parks = response.json()
    except requests.exceptions.RequestException as e:
        # Если API недоступен или вернул ошибку, показываем пустую страницу
        print(f"Could not connect to API: {e}")
        parks = []

    context = {
        'parks': parks
    }
    return render(request, 'frontend/park_list.html', context)


def park_detail(request, park_id):
    api_url_park_id = f"http://localhost:8000/api/v1/parks/{park_id}/"
    api_url_entertainments_id = f"http://localhost:8000/api/v1/entertainments/?park_id={park_id}"
    park = None
    entertainments = []
    try:
        response_park = requests.get(api_url_park_id)
        response_park.raise_for_status()
        park = response_park.json()        
    except requests.exceptions.RequestException as e:
        print(f"Couldnt get park details: {e}")

    if park:
        try:
            response_ent = requests.get(api_url_entertainments_id)
            response_ent.raise_for_status()
            entertainments = response_ent.json()
        except requests.exceptions.RequestException as e:
            print(f"Couldnt get entertainments: {e}")

    context = {
        'park': park,
        'entertainments': entertainments,
    }

    return render(request, 'frontend/park_detail.html', context)
    