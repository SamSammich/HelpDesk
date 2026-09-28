from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import home, ticket_list, ticket_detail, ticket_create


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('tickets/create/', ticket_create, name='ticket_create'),
]