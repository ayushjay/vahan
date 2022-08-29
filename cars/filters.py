import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(lookup_expr='icontains')
    year_gt = django_filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_lt = django_filters.NumberFilter(field_name='year', lookup_expr='lt')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Car
        fields = ['category', 'year', 'transmission']
