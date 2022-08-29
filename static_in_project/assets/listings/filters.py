import django_filters

from .models import *

class ListingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    year_gt = django_filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_lt = django_filters.NumberFilter(field_name='year', lookup_expr='lt')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Listing
        fields = ['category', 'year']
