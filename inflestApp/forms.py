from django import forms

class DataForm(forms.Form):
    inflation_rate = forms.FloatField(label='Inflation Rate' )
    interest_rate = forms.FloatField(label='Interest Rate' )
    exchange_rate = forms.FloatField(label='Exchange Rate' )
    broad_money_growth_rate = forms.FloatField(label='Broad Money Growth Rate')
    real_gdp = forms.FloatField(label='Real GDP')
    fdi_growth_rate = forms.FloatField(label='FDI Growth Rate')
    fiscal_expenditure_growth_rate = forms.FloatField(label='Fiscal Expenditure Growth Rate')
    year = forms.IntegerField(label='Year')
    
    country_choices = [
        ('USA', 'United States'),
        ('CAN', 'Canada'),
        ('GBR', 'United Kingdom'),
        ('AUS', 'Australia'),
        ('IND', 'India'),
        ('CHN', 'China'),
        ('JPN', 'Japan'),
        ('GER', 'Germany'),
        ('FRA', 'France'),
        ('BRA', 'Brazil'),
        ('RUS', 'Russia'),
        ('ITA', 'Italy'),
        ('ESP', 'Spain'),
        ('MEX', 'Mexico'),
        ('KOR', 'South Korea'),
        ('IDN', 'Indonesia'),
        ('TUR', 'Turkey'),
        ('SAU', 'Saudi Arabia'),
        ('ZAF', 'South Africa'),
        ('NGA', 'Nigeria'),
        ('EGY', 'Egypt'),
        ('ARG', 'Argentina'),
        ('SWE', 'Sweden'),
        ('NOR', 'Norway'),
        ('CHE', 'Switzerland'),
        # Add more countries as needed
    ]
    country = forms.ChoiceField(choices=country_choices, label='Select Country', help_text='Choose the preferred country.')

    development_index_choices = [
        ('developed', 'Developed'),
        ('developing', 'Developing'),
        ('underdeveloped', 'Underdeveloped'),
    ]
    development_index = forms.ChoiceField(choices=development_index_choices, label='Development Index', help_text='Select the development index.')

    trilemma_choices = [
        ('option_a', 'Option A'),
        ('option_b', 'Option B'),
        ('option_c', 'Option C'),
    ]
    trilemma = forms.ChoiceField(choices=trilemma_choices, label='Trilemma', help_text='Select the trilemma option.')