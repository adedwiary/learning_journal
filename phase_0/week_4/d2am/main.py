import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from PIL import Image

# #########################Set up config######################################################
# st.set_page_config(
#     page_title="Milestones 1",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.google.com',
#         'Report a bug': "https://www.github.com/adedwiary",
#         'About': "# Creating Streamlit"
#     }
# )

# st.set_option('deprecation.showPyplotGlobalUse', False)

# st.title('Anita, Wenny, Elita, Prabowo')

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# """
# # My first app
# Here's our first attempt at using data to create a table:
# """

# df= pd.read_csv('train.csv')
# df

# '''
# # Chart
# '''
# # chart_data = pd.DataFrame(
# #      np.random.randn(20, 3),
# #      columns=['a', 'b', 'c'])

# # st.line_chart(chart_data)

# '''# map'''
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# ''' # Checkbox'''
# show_df= st.checkbox('Show dataframe')
# st.write(show_df)
# if show_df:
#     st.write(df)

# chart_data = df['Age']
# st.line_chart(chart_data)

# ''' select box'''
# option= st.selectbox(
#     'pilih kolom Age',
#     df['Age']
#     )

# 'your selected option is ', option

# option_2 = st.sidebar.selectbox(
#     'Pilih kolom Pclass',
#      df['Pclass'])

# 'You selected:', option_2

# left_column, right_column = st.columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#   right_column.write("Woohoo!")

# expander = st.expander("FAQ")
# expander.write("Here you could put in some really, really long explanations...")

# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')

# '''# radio button'''

# kolom = st.radio(
#     'pilih kolom?',
#     ('Age', 'Survived', 'Pclass'))
# if kolom =='Age':
#     st.write(df.Age)
# elif kolom=='Survived':
#     st.write(df.Survived)
# else:
#     st.write(df.Pclass)

# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])
# st.write('You selected:', options)

# kolom_survivied = st.radio (
#     'periksa kolom survived', df.Survived.unique())

# st.write(df[df.Survived==kolom_survivied])

# '''select box '''
# survived_pclass=st.selectbox(
#     'pilih pclass', df.Pclass.unique()
# )

# st.write(df[
#     (df.Pclass == survived_pclass) &
#     (df.Survived == kolom_survivied)
# ])

# values = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)

# values2= st.slider(
#     'select a range of values',
#     0.0, df.Age.max(), (10.0, 60.0))

# st.write('Values:', values2)
# st.write(df[(df.Age>=values2[0]) & (df.Age <= values2[1])])

# '''# matplotplib'''
# st.bar_chart(df[(df.Age>=values2[0]) & (df.Age <= values2[1])].Age)


# '''# selectbox + matplotlib'''
# list_columns= ['Age', 'Fare']
# df_titanic_select= st.selectbox('pilih kolom', list_columns)
# plt.hist(df[df_titanic_select])

# st.pyplot()

# ''' # Image'''

# img = Image.open('pict.jpg')

# st.title('ANTARIKSA')
# st.image(img, caption='Antariksa', use_column_width=True)

# ''' # Membuat Kolom '''
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("Antariksa")
#     st.image(img)

# with col2:
#     st.header('Ini kolom ke-2')

# with col3:
#     st.image("https://fastly.4sqi.net/img/general/600x600/3185742_GAVz2uwmY5sfMGQ_IqPbtATRYegNNNGTlBnXeWf48AU.jpg")

# ''' # Membuat Kolom 2 '''

# st.title('Making columns using ratio')

# col1, col2 = st.columns([3, 1])
# data = np.random.randn(10, 1)

# col1.subheader("A wide column with a chart")
# col1.line_chart(data)

# col2.subheader("A narrow column with the data")
# col2.write(data)

# st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

# ''' # Expander '''


# with st.expander("See explanation"):
#   st.write("""
#      The chart above shows some numbers I picked for you.
#      I rolled actual dice for these, so they're *guaranteed* to
#      be random.
#   """)

#   st.image("https://static.streamlit.io/examples/dice.jpg")

# ''' # Container '''

# st.title('CONTAINER with Notation')

# with st.container():
#     st.write("This is inside the container")
    
#   # You can call any Streamlit command, including custom components:
#     st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")

# st.title('CONTAINER with variable')
# c = st.container()

# c.write('This is inside the container 1')

# st.write('This is outside the container')

# c.write('This is inside the container 2')

#################### if else for multipage ####################
pages = st.sidebar.selectbox('Select a page: ', ['Data Visualization', 'Hypotesis Testing'])

if pages == 'Data Visualization':
    st.title('DATA VISUALIZATION')
    st.header('Demo Pages for data visualization')
    st.markdown('input your data visualization here')

else:
    st.title('HYPOTHESIS TESTING')
    st.header('Demo Pages for Hypothesis Testing')
    st.markdown('input your hypothesis testing here')

st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

''' Expander '''

with st.expander("See explanation"):
    st.write("""
     The chart above shows some numbers I picked for you.
     I rolled actual dice for these, so they're *guaranteed* to
     be random.""")

