from statsmodels.tsa.arima.model import ARIMAResultsWrapper
MONTH_PER_YEAR = 12

class AccidentsInferer(object):
    def __init__(self, model_file="arma_model_2020_12_p6_q24.pickle") -> None:
        """ AR Model to predict number of accidents 
        """
        self.model_predictor = ARIMAResultsWrapper.load(model_file)
        self.last_data_year = 2020
        self.last_data_month = 12
        self.last_data_idx = self.last_data_year * MONTH_PER_YEAR + self.last_data_month
        self.last_data_idx_in_model = 251
        
    
    def predict(self, year, month):
        # Convert to year and month to offset to last month in data
        offset = year * MONTH_PER_YEAR + month - self.last_data_idx
        index = self.last_data_idx_in_model + offset 
        print(f"Making prediction for year {year}, {month} with {index}.")

        # Make prediction
        preds = self.model_predictor.predict(start=self.last_data_idx_in_model + 1, end=index, dynamic=False)

        # Round the result
        result = round(preds.loc[index])
        print(f"Result: {result}")
        return result

