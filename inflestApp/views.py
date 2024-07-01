from django.shortcuts import render
from .forms import DataForm
from .models import MacroeconomicData
from .analysis.analysis import  train_varmax_model, forecast_varmax_model
from .management.commands.import_data import import_data
import pandas as pd

def analysis_view(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # import_data("./file2.xlsx")
            new_data = MacroeconomicData.objects.create(
                inflation_rate=form.cleaned_data["inflation_rate"],
                interest_rate=form.cleaned_data["interest_rate"],
                exchange_rate=form.cleaned_data["exchange_rate"],
                real_gdp=form.cleaned_data["real_gdp"],
                fdi=form.cleaned_data["fdi"],
                fiscal_expenditure=form.cleaned_data["fiscal_expenditure"],
                year=form.cleaned_data["year"],
                growth_rate=form.cleaned_data["growth_rate"]

            )
            new_data.save()
            print("sAVED")

            queryset = MacroeconomicData.objects.all()
            df = pd.DataFrame(list(queryset.values()))
            df2 = []
            values = list(queryset.values())
            for data in values:
                del data["country"]
                del data["id"]
                df2.append(data)
            df3 = pd.DataFrame(df2)
            print(df3)
            # trained_model_path =  train_varmax_model(df3)
            trained_model_path = 'varmax_model.pkl'
            print("----------------------------------")
            dta = pd.DataFrame([data])
            print(dta)
            forecast = forecast_varmax_model(trained_model_path, dta)
            print(forecast)
            return render(request, 'result.html',
                          {'forecast': forecast,}
                        #    'inflation_rate': forecast[0][0],
                        #    'interest_rate': forecast[0][1],
                        #    'exchange_rate':forecast[0][2],
                        #    'real_gdp':forecast[0][3],
                        #    'fdi': forecast[0][4],
                        #    'fiscal_expenditure': forecast[0][5]}
                           )
    else:
        form = DataForm()
    return render(request, 'input.html', {'form': form})
