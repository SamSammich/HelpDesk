from django.shortcuts import get_object_or_404, render
from tickets.models import Ticket


def home(request):
    total_tickets = Ticket.objects.count()

    new_tickets = Ticket.objects.filter(
        status=Ticket.Status.NEW
    ).count()

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


def ticket_list(request):
    tickets = Ticket.objects.select_related(
        'employee',
        'category',
    ).all()

    return render(
        request,
        'tickets/ticket_list.html',
        {'tickets': tickets},
    )


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(
        Ticket.objects.select_related(
            'employee',
            'category',
        ),
        id=ticket_id,
    )

    return render(
        request,
        'tickets/ticket_detail.html',
        {'ticket': ticket},
    )