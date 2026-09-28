from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'employee',
            'category',
            'title',
            'description',
            'priority',
        ]
        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 5}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = (
            self.fields['category']
            .queryset
            .filter(is_active=True)
        )