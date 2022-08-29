from django import forms 
from .models import SelectCar


class SelectCarForm(forms.ModelForm):
  
    class Meta:
        model = SelectCar
        fields = '__all__'
"""
    BRANDS = (
        ('BMW','BMW')
        ('Mercedes','MR')
    )
    brand = forms.ChoiceField(choices=BRANDS)
    CAR_MODELS = (
        ('X1','X1')
        ('X2','X2')
        ('X3','X3')

    )
    car_model = forms.ChoiceField(choices=CAR_MODELS) 
"""
    