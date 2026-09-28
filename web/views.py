from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from tickets.forms import TicketForm
from tickets.models import Ticket


@login_required
def home(request):
    if request.user.is_staff:
        tickets = Ticket.objects.all()
    else:
        employee = getattr(request.user, 'employee_profile', None)

        if employee is None:
            raise PermissionDenied

        tickets = Ticket.objects.filter(employee=employee)

    total_tickets = tickets.count()
    new_tickets = tickets.filter(status=Ticket.Status.NEW).count()
    resolved_tickets = tickets.filter(status=Ticket.Status.RESOLVED).count()

    latest_tickets = (
        tickets
        .select_related('employee', 'category')
        .order_by('-created_at')[:5]
    )

    context = {
        'total_tickets': total_tickets,
        'new_tickets': new_tickets,
        'resolved_tickets': resolved_tickets,
        'latest_tickets': latest_tickets,
    }

    return render(request, 'home.html', context)


@login_required
def ticket_list(request):
    if request.user.is_staff:
        tickets = Ticket.objects.select_related(
            'employee',
            'category',
        ).all()
    else:
        employee = getattr(request.user, 'employee_profile', None)

        if employee is None:
            raise PermissionDenied

        tickets = Ticket.objects.select_related(
            'employee',
            'category',
        ).filter(employee=employee)

    return render(
        request,
        'tickets/ticket_list.html',
        {'tickets': tickets},
    )


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(
        Ticket.objects.select_related('employee', 'category'),
        id=ticket_id,
    )

    if not request.user.is_staff:
        employee = getattr(request.user, 'employee_profile', None)

        if employee is None or ticket.employee != employee:
            raise PermissionDenied

    return render(
        request,
        'tickets/ticket_detail.html',
        {'ticket': ticket},
    )


@login_required
def ticket_create(request):
    employee = getattr(request.user, 'employee_profile', None)

    if employee is None:
        raise PermissionDenied

    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.employee = employee
            ticket.save()

            return redirect(
                'ticket_detail',
                ticket_id=ticket.id,
            )
    else:
        form = TicketForm()

    return render(
        request,
        'tickets/ticket_create.html',
        {'form': form},
    )