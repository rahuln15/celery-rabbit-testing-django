from celery import shared_task

@shared_task
def send_push_notification(user_id, message):
    # Logic to send push notification
    print(f"Sending push notification to user {user_id}: {message}")
    return f"Notification sent to user {user_id} with message: {message}"
