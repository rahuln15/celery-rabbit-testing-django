from django.http import HttpResponse
from .tasks import send_push_notification

def notify_user(request, user_id, message):
    # Trigger the Celery task
    result = send_push_notification.delay(user_id, message)
    return HttpResponse(f"Task ID: {result.id} - Notification task triggered!")
