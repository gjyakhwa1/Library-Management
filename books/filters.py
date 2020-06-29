import django_filters
from .models import IssueBooks


class IssueFilter(django_filters.FilterSet):
    class Meta:
        model = IssueBooks
        fields = '__all__'
        exclude = ['entry_date', 'expiry_date']
