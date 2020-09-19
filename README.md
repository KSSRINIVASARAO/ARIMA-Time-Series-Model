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
p is the number of autoregressive terms,the value of ‘p’ is determined using the PACF plot.
MA term is used to defines number of past forecast errors used to predict the future values. 
The parameter ‘q’ in arima represents the MA term,q is the number of lagged forecast errors in the prediction equation.
ACF plot is used to identify the correct ‘q’ value.
d is the number of nonseasonal differences needed for stationarity.
Order of differencing  specifies the number of times the differencing operation is performed on series to make it stationary. 
ARIMA(1,0,0) = first-order autoregressive: if the series is stationary and autocorrelated, perhaps it can be predicted as a multiple of its own previous value, plus a constant.
ARIMA(0,1,0) = random walk:  If the series is not stationary, the simplest possible model for it is a random walk model, which can be considered as a limiting case of an AR(1) model in which the autoregressive coefficient is equal to 1, i.e., a series with infinitely slow mean reversion. 
ARIMA(1,1,0) = differenced first-order autoregressive model: If the errors of a random walk model are autocorrelated, perhaps the problem can be fixed by adding one lag of the dependent variable to the prediction equation.
ARIMA(0,1,1) without constant = simple exponential smoothing: Another strategy for correcting autocorrelated errors in a random walk model is suggested by the simple exponential smoothing model. Recall that for some nonstationary time series (e.g., ones that exhibit noisy fluctuations around a slowly-varying mean), the random walk model does not perform as well as a moving average of past values.
ARIMA(0,1,1) with constant = simple exponential smoothing with growth: By implementing the SES model as an ARIMA model, you actually gain some flexibility. First of all, the estimated MA(1) coefficient is allowed to be negative: this corresponds to a smoothing factor larger than 1 in an SES model, which is usually not allowed by the SES model-fitting procedure. Second, you have the option of including a constant term in the ARIMA model if you wish, in order to estimate an average non-zero trend.ARIMA(0,2,1) or (0,2,2) without constant = linear exponential smoothing: Linear exponential smoothing models are ARIMA models which use two nonseasonal differences in conjunction with MA terms. 
ARIMA(0,2,1) or (0,2,2) without constant = linear exponential smoothing: Linear exponential smoothing models are ARIMA models which use two nonseasonal differences in conjunction with MA terms. 
ARIMA(1,1,2) without constant = damped-trend linear exponential smoothing:It extrapolates the local trend at the end of the series but flattens it out at longer forecast horizons to introduce a note of conservatism, a practice that has empirical support. 

