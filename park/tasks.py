from celery import shared_task
import time

@shared_task
def send_test_email(email):
    """
    Простая задача, которая имитирует отправку email.
    """
    print(f"Starting to send a test email to {email}...")
    # Имитируем долгую операцию (например, подключение к почтовому серверу)
    time.sleep(5)
    print(f"Successfully sent a test email to {email}!")
    return f"Email sent to {email}"


@shared_task
def notify_admin_of_new_entertainment(entertainment_id):
    '''
    Иммитирует отправку уведомления администратору о новом развлечении.
    '''
    from .models import Entertainment # внутри иморт для избежания циклического импортирования

    try:
        entertainment = Entertainment.objects.get(id=entertainment_id)
        print("--- TASK START ---")
        print(f"Notifying admin about new entertainment: {entertainment.title} in park '{entertainment.park.title}")
        time.sleep(10) # иммитация долгой опреции
    except Entertainment.DoesNotExist:
        print(f"--- TASK FAILED: Entertainment with if={entertainment_id} not found! ---")
