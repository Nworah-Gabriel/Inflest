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
            input_data = form.cleaned_data

            # Convert input data to DataFrame
            input_d = pd.DataFrame([input_data])
            input_df = input_d.drop(columns=['year'])

            # Get historical data from the database
            queryset = MacroeconomicData.objects.all()
            historical_data = pd.DataFrame(list(queryset.values()))

            # Drop unnecessary columns
            historical_data = historical_data.drop(columns=['country', 'id', 'year'])

            # Combine historical data with input data for forecasting
            combined_data = pd.concat([historical_data, input_df], ignore_index=True)
            print("----------------+++++++++++11111111111111--------------")
            print(combined_data)

            # Train the model with combined data
            try:
                trained_model_path = train_varmax_model(combined_data)

                if trained_model_path:
                    # Forecast with the new input data
                    forecast = forecast_varmax_model(trained_model_path, input_df)
                    forecast_values = forecast.iloc[0].tolist()

                    print(forecast_values)

                    return render(request, 'result.html',
                                  {
                                   'inflation_rate': forecast_values[0],
                                   'interest_rate': forecast_values[1],
                                   'exchange_rate': forecast_values[2],
                                   'real_gdp': forecast_values[3],
                                   'fdi': forecast_values[4],
                                   'fiscal_expenditure': forecast_values[5],
                                   'growth_rate': forecast_values[6],
                                   }
                                  )
                else:
                    return render(request, 'input.html', {'form': form, 'error': 'Model training failed. Please check your data.'})
            except ValueError as e:
                return render(request, 'input.html', {'form': form, 'error': str(e)})
    else:
        form = DataForm()
    return render(request, 'input.html', {'form': form})
