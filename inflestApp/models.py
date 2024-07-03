from django.db import models

class MacroeconomicData(models.Model):
    inflation_rate = models.FloatField(null=True)
    interest_rate = models.FloatField(null=True)
    exchange_rate = models.FloatField(null=True)
    real_gdp = models.FloatField(null=True)
    fdi_growth_rate = models.FloatField(null=True)
    fiscal_expenditure_growth_rate = models.FloatField(null=True)
    year = models.IntegerField(null=True)
    country = models.CharField(max_length=100)
    broad_money_growth_rate = models.FloatField(null=True)
    