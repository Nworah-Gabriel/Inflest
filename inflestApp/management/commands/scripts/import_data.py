import pandas as pd
from inflestApp.models import MacroeconomicData

def import_data(file_path):
    data = pd.read_excel(file_path)
    data = data.dropna(subset=['YEAR'])

    for _, row in data.iterrows():
        year = row['YEAR']
        # if pd.isna(year) or not isinstance(year, int):
        #     continue

        print(f"Processing row: {row.to_dict()}")  # Add this line
        data = MacroeconomicData.objects.create(
            country=row['COUNTRY'],
            year=int(row['YEAR']),
            interest_rate=row['INTEREST RATE'],
            exchange_rate=row['EXR (US$)'],
            real_gdp=row['RGDP GROWTH RATE (%)'],
            growth_rate=row['BROADER MONEY (GROWTH RATE %)'],
            fdi=row['FDI Growth Rate (%)'],
            inflation_rate=row['INF (END-YEAR)'],
            fiscal_expenditure=row['Fiscal Expenditure Growth Rate (%)']
        )
        data.save()
        print("Saved:", data)  # Add this line
