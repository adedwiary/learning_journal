import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('First App')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df= pd.read_csv('train.csv')
df

'''
# Chart
'''
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

'''# map'''
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

''' # Checkbox'''
show_df= st.checkbox('Show dataframe')
st.write(show_df)
if show_df:
    st.write(df)

chart_data = df['Age']
st.line_chart(chart_data)

''' select box'''
option= st.selectbox(
    'pilih kolom Age',
    df['Age']
    )

'your selected option is ', option

option_2 = st.sidebar.selectbox(
    'Pilih kolom Pclass',
     df['Pclass'])

'You selected:', option_2

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

'''# radio button'''

kolom = st.radio(
    'pilih kolom?',
    ('Age', 'Survived', 'Pclass'))
if kolom =='Age':
    st.write(df.Age)
elif kolom=='Survived':
    st.write(df.Survived)
else:
    st.write(df.Pclass)

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)

kolom_survivied = st.radio (
    'periksa kolom survived', df.Survived.unique())

st.write(df[df.Survived==kolom_survivied])

'''select box '''
survived_pclass=st.selectbox(
    'pilih pclass', df.Pclass.unique()
)

st.write(df[
    (df.Pclass == survived_pclass) &
    (df.Survived == kolom_survivied)
])

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

values2= st.slider(
    'select a range of values',
    0.0, df.Age.max(), (10.0, 60.0))

st.write('Values:', values2)
st.write(df[(df.Age>=values2[0]) & (df.Age <= values2[1])])

'''# matplotplib'''
st.bar_chart(df[(df.Age>=values2[0]) & (df.Age <= values2[1])].Age)


# ''' # plotly '''
# import plotly.express as px
# fig= px.histogram(df[(df.Age>=values2[0]) & (df.Age <= values2[1])].Age, x='Age', nbins=20)
# st.plotly_chart(fig)

''' selectbox + matplotlib'''
list_columns= ['Age', 'Fare']
df_titanic_select= st.selectbox('pilih kolom', list_columns)
plt.hist(df[df_titanic_select])

st.pyplot()
