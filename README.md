# ARIMA

A popular and widely used statistical method for time series forecasting is the ARIMA model. ARIMA is an acronym that stands for AutoRegressive Integrated Moving Average. It is a class of model that captures a suite of different standard temporal structures in time series data.

The log transformation is often used to convert time series that are nonstationary with respect to the innovation variance into stationary time series.
As one alternative, you can simply exponentiate the forecast series. This procedure gives a forecast for the median of the series, but the antilog of the forecast log series underpredicts the mean of the original series. 

Augmented Dickey Fuller test (ADF Test) is a common statistical test used to test whether a given Time series is stationary or not. It is one of the most commonly used statistical test when it comes to analyzing the stationary of a series. 
Dickey-Fuller test is a unit root test that tests the mull hypothesis that α=1 in the following model equation. alpha is the coefficient of the first lag on Y.

Null Hypothesis (H0): alpha=1
The Augmented Dickey-Fuller test evolved based on the above equation and is one of the most common form of Unit Root test.

ARIMA is a very popular statistical method for time series forecasting.
ARIMA stands for Auto_regressive Integrated Moving Average
AR term refers to the past values used for forecasting the next value. 
The AR term is defined by the parameter ‘p’ in arima.
The value of ‘p’ is determined using the PACF plot.
MA term is used to defines number of past forecast errors used to predict the future values. The parameter ‘q’ in arima represents the MA term. 
ACF plot is used to identify the correct ‘q’ value.
Order of differencing  specifies the number of times the differencing operation is performed on series to make it stationary. 
Test like ADF and KPSS can be used to determine whether the series is stationary and help in identifying the d value. 


