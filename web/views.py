from django.shortcuts import render

from tickets.models import Ticket


def home(request):
    total_tickets = Ticket.objects.count()
    new_tickets = Ticket.objects.filter(status=Ticket.Status.NEW).count()
    resolved_tickets = Ticket.objects.filter(
        status=Ticket.Status.RESOLVED
    ).count()

    latest_tickets = Ticket.objects.select_related(
        'employee',
        'category',
    ).order_by('-created_at')[:5]

    context = {
        'total_tickets': total_tickets,
        'new_tickets': new_tickets,
        'resolved_tickets': resolved_tickets,
        'latest_tickets': latest_tickets,
    }

    return render(request, 'home.html', context)