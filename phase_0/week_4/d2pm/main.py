import streamlit as st
from PIL import Image
import numpy as np

#################### set up config #############################
img = Image.open('2-4.jpg')

st.set_page_config(
    page_title="Milestone 1",
    page_icon= img,
    layout="centered", #wide
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Creating Streamlit"
    }
)


# ##################### IMPORT IMAGE #############################
# img = Image.open('2-4.jpg')

# st.title('EIFFEL TOWER')
# st.image(img, caption='eiffel tower', use_column_width=True)

# ####################### MAKE COLUMNS #################################
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("eiffel tower")
#     st.image(img)
#     st.markdown('tambahan kolom 1')

# with col2:
#     st.header('Ini kolom ke -2')

# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")

# ############## MAKE COLUMNS USING RATIO ###############################
# st.title('Making column using ratio')

# col1, col2 = st.columns([3, 1])
# data = np.random.randn(10, 1)

# col1.subheader("A wide column with a chart")
# col1.line_chart(data)

# col2.subheader("A narrow column with the data")
# col2.write(data)

# ######################### EXPANDER ###################################
# st.title('EXPANDER')

# st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

# with st.expander("See explanation"):
#   st.write("""
#      The chart above shows some numbers I picked for you.
#      I rolled actual dice for these, so they're *guaranteed* to
#      be random.
#   """)

#   st.image("https://static.streamlit.io/examples/dice.jpg")

# ######################### CONTAINER ###################################
# st.title('CONTAINER with Notation')

# with st.container():
#     st.write("This is inside the container")

#     # You can call any Streamlit command, including custom components:
#     st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")

# st.title('CONTAINER with variable')
# c = st.container()

# c.write('this is inside container 1')

# st.write('this is outside container')

# c.write('this is inside container 2')

# ###################################################

################## if - else for multipage ##############################
st.sidebar.title('Page Selection')
pages = st.sidebar.selectbox('Select a Page: ', ['Data Visualization', 'Hypotesis Testing'])

if pages == 'Data Visualization':
    st.title('DATA VISUALIZATION')
    st.header('Demo Pages for Data Viz')

    st.image(img, caption='eiffel tower', use_column_width=True)

    st.markdown('input your data viz here')
else:
    st.title('HYPOTHESIS TESTING')
    st.header('Demo Pages for Hypotesis Testing')

    st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
    st.markdown('input your hypotesis testing here')