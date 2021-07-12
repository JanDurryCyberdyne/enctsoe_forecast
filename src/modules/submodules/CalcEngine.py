class CalcEngine():
    pd = 0
    def __init__(self,pd):
        self.pd = pd
        print("CalcEngine initiated")
    
    def calc_statistical(df_historical,days_to_average_over = 7):
        # historical data for last x week days:
        for i in range(days_to_average_over-1):
            df_historical = self.pd.concat([get_historical(date=datetime.datetime.now()-relativedelta(days=7*(i+2)),region=region),df_historical])
        df_historical = df_historical.groupby(df_historical.index.hour).mean()

        # get forecast for: wind, solar and (total) generation from EntsoE
        object = EntsoePandasClient(api_key = 'd3f5632f-b0be-4a39-a6e8-fe25ff95368c')
        if region=='DE':
            df_wind_and_solar       = object.query_wind_and_solar_forecast(region,start = start, end = end)
            df_generation_forecast  = object.query_generation_forecast(region,start = start, end = end)
        else:
            df_wind_and_solar       = object.query_wind_and_solar_forecast(region,start = start, end = end, lookup_bzones=True)
            df_generation_forecast  = object.query_generation_forecast(region,start = start, end = end)

        df_wind_and_solar = self.pd.DataFrame(df_wind_and_solar)
        df_wind_and_solar = df_wind_and_solar.groupby(df_wind_and_solar.index.hour).mean()
        df_wind_and_solar['Wind and Solar'] = df_wind_and_solar.sum(axis=1)

        df_generation_forecast  = self.pd.DataFrame(df_generation_forecast)
        df_generation_forecast  = df_generation_forecast.groupby(df_generation_forecast.index.hour).mean()
        df_generation_forecast.index = df_generation_forecast.index.map(lambda x: start + relativedelta(hours = x))

        # alle gemittelten daten der letzten wochen, bis auf die Vorhersage für wind und solar
        df_forecast = df_historical
        try:
            df_forecast["Wind Onshore"] = df_wind_and_solar["Wind Onshore"]
            df_forecast["Wind Offshore"] = df_wind_and_solar["Wind Offshore"]
        except KeyError:
            print("No Wind Offshore")

        df_forecast.index = df_forecast.index.map(lambda x: start + relativedelta(hours = x))
        df_forecast.to_csv(filename)
        return df_forecast

    
# def calc_entsoe(region='DE',date = datetime.datetime.now()):
# 	start,end = get_day_times(date)
# 	filename  = get_filename(date,region,data_type = "forecast",forecast_type = "entsoe")
# 	object    = EntsoePandasClient(api_key = 'd3f5632f-b0be-4a39-a6e8-fe25ff95368c')
# 	df_generation_forecast = object.query_generation_forecast(country_code=region,start=start,end=end)
# 	df_generation_forecast.to_csv(filename,header="0")
# 	return df_generation_forecast