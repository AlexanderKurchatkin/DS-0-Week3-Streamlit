import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
#path = '/home/alexander/Elbrus/datasets/tips.csv'
tips = pd.read_csv(path)

st.sidebar.title('О приложении')
st.sidebar.info("Это приложение демонстрирует  Распределение счетов, чаевых и выручки по дням недели и времени обслуживания")

st.write("""
# Исследование по чаевым - [датасет tips.csv]
""")
         
st.write("""
Гистограмма Total Bill
""")

fig,ax=plt.subplots()
sns.histplot(tips['total_bill'])
plt.xlabel('total bill')
plt.ylabel('sum')
st.pyplot(fig)

st.write("""
Scatterplot, показывающий связь между Total Bill & Tip
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.xlabel('total bill')
plt.ylabel('tips')
st.pyplot(fig)

st.write("""
График, связывающий Total Bill & Tip & Size
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size', palette='coolwarm')
plt.xlabel('total bill')
plt.legend(title='Size', loc='upper left')
plt.ylabel('tips')
st.pyplot(fig)

st.write("""
Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу
""")

fig,ax=plt.subplots()
sns.scatterplot(x='tip', y='day', size='tip', hue='sex', data=tips, palette={'Male': 'blue', 'Female': 'red'})
plt.xlabel('tips')
plt.ylabel('day of the week')
st.pyplot(fig)

st.write("""
Box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)
""")

fig,ax=plt.subplots()
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
plt.xlabel('day of the week')
plt.ylabel('total bill')
st.pyplot(fig)