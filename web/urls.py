from django.urls import path
from .views import home, ticket_list, ticket_detail

urlpatterns = [
    path('', home, name='home'),
    path('tickets/', ticket_list, name='ticket_list'),
    path(
        'tickets/<int:ticket_id>/',
        ticket_detail,
        name='ticket_detail',
    ),
]