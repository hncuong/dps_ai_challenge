# Artificial Intelligence Engineer challenge
The goals of this challenge are to create an AI model to predict number of accidents in a month and deploy it.
I used the following steps to achieve that.

- Data cleaning and EDA:
  - Clean missing values, format to right format data.
  - Exploratory Data Analysis.
  ![Accidents per category over time.](All_categories_accidents_over_time.png?raw=true "Accidents per category over time.")


- Modelling
  - I choose simple time series forcasting models such as Auto Regression (AR), Auto Regression Moving Average (ARMA), and also try Facebook Prophet.
  - After preparing data, training model and evaluation with Root Mean Square Error (RMSE), I decided to go for AR and ARMA for simplicity and efficiency. 
  - Grid search was done to find a good hyper parameters.

- Deploy the model
  - Modey is deploy with Flask web application framework in Google cloud virtual machine.