from django import forms

class DataForm(forms.Form):
    inflation_rate = forms.FloatField()
    interest_rate = forms.FloatField()
    exchange_rate = forms.FloatField()
    growth_rate = forms.FloatField()
    real_gdp = forms.FloatField()
    fdi = forms.FloatField()
    fiscal_expenditure = forms.FloatField()
    year = forms.IntegerField()
