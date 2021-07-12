from src.modules.submodules.CalcEngine import CalcEngine


class DataHandler:
    os = 0
    pd = 0

    def __init__(self, os, pd):
        self.os = os
        self.pd = pd
        self.CalcEngine = CalcEngine(pd)
        #print("DataHandler initiated")

    def get_data(self, fileexists, filename,data_type,forecast_type):
        if (fileexists):
            df_data = self.pd.read_csv(filename, index_col=0)
            df_data.index = self.df_data.index.map(
                lambda x: self.pd.Timestamp(x, tz='Europe/Berlin', freq='H'))
            return df_data
        else:
            if data_type == "forecast":
                if forecast_type == "statistical":
                    df_data = self.CalcEngine.calc_statistical()
                    df_data.to_csv(filename)
                    return df_data
                if forecast_type == "deep_learning":
                    df_data=self.CalcEngine.calc_deep_learning()
                    df_data.to_csv(filename)
                    return df_data
                if forecast_type == 'entsoe':
                    df_data=self.CalcEngine.calc_entsoe()
                    df_data['0']=df_data
                    return df_data
            if data_type == "historical":
                    # Declaration: this function returns the total energy generation of a PAST! day.
                    # The function checks the storage, if there is an existing file it loads it. If there is no existing it
                    # makes the entso-E call and safes the data.
                    '''
                    Input: region [str] (see possibilities below); date [datetime.object]
                    Return : pd.Dataframe
                    '''
                    # 'DE-TENNET' #'DE-AMPRION'  'DE-50HZ' 'DE-TRANSNET' 
                    start,end     = get_day_times(date)
                    api_key = 'd3f5632f-b0be-4a39-a6e8-fe25ff95368c'
                    object = EntsoePandasClient(api_key=api_key)
                    if region =='DE':
                        df_generation = object.query_generation(start=start,end=end+relativedelta(hours=1),country_code=region)
                        df_generation = df_generation.resample('1H').mean()
                        df_generation.to_csv(filename)
                    else:
                        df_generation = object.query_generation(start=start,end=end+relativedelta(hours=1),country_code=region,lookup_bzones=True)
                        df_generation = df_generation.resample('1H').mean()
                        df_generation.to_csv(filename)        
                    return df_generation