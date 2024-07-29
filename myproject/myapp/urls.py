from django.urls import path
from .views import notify_user

urlpatterns = [
    path('notify/<int:user_id>/<str:message>/', notify_user, name='notify_user'),
]
