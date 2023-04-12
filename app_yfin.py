import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import datetime


st.header('Данные о котировках компании Apple')
st.sidebar.title('О приложении')
st.sidebar.info("Это приложение демонстрирует  данные о котировках компании Apple c помощью библиотеки yfinance")
st.sidebar.info("Выберете дату")

today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('С какой даты', before)
end_date = st.sidebar.date_input('По какую дату', today)
data = yf.download('AAPL')
df = pd.DataFrame(data)

st.write('Цена открытия')
st.line_chart(df.Open)

st.write('Цена закрытия')
st.line_chart(df.Close)

st.write('Максимальная цена в ходе торгов')
st.line_chart(df.Low)

st.write('Минимальная цена в ходе торгов')
st.line_chart(df.High)




