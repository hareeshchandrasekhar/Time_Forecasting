import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import matplotlib
from matplotlib import pyplot 
import warnings
import seaborn as sns



#%matplotlib inline


warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pickle
from pandas.tseries.offsets import DateOffset
from statsmodels.tsa.arima.model import ARIMA


# load the model from disk
yearly_model = pickle.load(open(r'Forecast_arima.pkl', 'rb'))

#monthly_model = load(open(r'C:\Users\Subash S\PycharmProjects\P130_Deployment\CO2_Forecast_arima_monthly.pkl', 'rb'))

st.title("Forecasting $CO_2$ Emission")
st.sidebar.subheader("Select CO2 Emission")
nav = st.sidebar.radio("", ["Yearly"])





































data2 = pd.read_csv(r"C:\Users\chandra shekhar\Desktop\project p143\Deployment\CO2 dataset.csv",header=0, index_col=0,parse_dates=True )


final_arima = ARIMA(data2['CO2'],order = (3,1,4))
final_arima = final_arima.fit()
















if nav == "Yearly":

    st.sidebar.subheader("Select the Years to Forecast from 2015")
    #year = st.sidebar.slider("", 2015, 2034, step=1)
    year = st.slider("Select number of Year from 2015", 1, 100, step=1)
    
    

    st.sidebar.subheader("To Forecast till the Selected Years\n Please Click on the 'Forecast' Button")

    pred_yearly = pd.DataFrame()
    pred_yearly['CO2 Yearly Emission'] = yearly_model.forecast(year)
    
    
    
    

    if st.sidebar.button("Forecast"):
        st.subheader(f"$CO_2$ Emission Forecasted from year 2015")
        pred_yearly
        fig = plt.figure(figsize=(12, 4), dpi=100)
        plt.plot(pred_yearly['CO2 Yearly Emission'], label='Auto regression forecast (ARIMA)')
        plt.title('Forecast for next {} years from 2015'.format(year))
        plt.legend(loc='best')

        st.subheader("Line plot for the Forecasted data")
        st.pyplot(fig)
        
        
        

        
    
    
        pred = pred_yearly['CO2 Yearly Emission']
   
      
        

        st.subheader(" plot of the entire data")
        fig1=plt.figure(figsize=(10,4))
        plt.plot(data2.CO2, label='original')
        plt.plot(pred, label='Predicted')
        plt.title('Forecast')
        plt.legend(loc='upper left', fontsize=8)
        st.pyplot(fig1)
        
       
        
        
        
        
        
        
        
        
        
        
        
        

if nav == "Monthly":

    st.sidebar.subheader("Select the Number of Months to Forecast from 2014 February")
    month = st.sidebar.slider("", 2, 120, step=1)

    st.sidebar.subheader("To Forecast till the Selected Months\n Please Click on the 'Forecast' Button")

    #pred_monthly = pd.DataFrame()
    #pred_monthly['CO2 Monthly'] = monthly_model.forecast(month)

    if st.sidebar.button("Forecast"):
        st.subheader(f"$CO_2$ Emission Forecasted from Feb 2014")
        #pred_monthly
        fig1 = plt.figure(figsize=(12, 4), dpi=100)
        #plt.plot(pred_monthly['CO2 Monthly'], label='Auto regression forecast (ARIMA)')
        plt.title('Forecast for next {} months from 2014 Feb'.format(month))
        plt.legend(loc='best')

        st.subheader("Line plot for the Forecasted data")
        st.pyplot(fig1)
