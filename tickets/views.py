from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_fields = [
        'status',
        'priority',
        'category',
        'employee',
    ]

    search_fields = [
        'title',
        'description',
    ]