from django.contrib import admin

from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'employee',
        'category',
        'priority',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'priority',
        'category',
    )

    search_fields = (
        'title',
        'employee__full_name',
    )

    list_editable = (
        'priority',
        'status',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )