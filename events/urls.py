# events/urls.py
from django.urls import path
from .views import create_event, event_list, update_event, delete_event

urlpatterns = [
    path('', event_list, name='event_list'),
    path('event/new/', create_event, name='create_event'),
    path('event/<int:pk>/edit/', update_event, name='update_event'),
    path('event/<int:pk>/delete/', delete_event, name='delete_event'),
]
