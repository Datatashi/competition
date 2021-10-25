import streamlit as st
import pandas as pd
import numpy as np

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

###############################################################33
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


#####################################################################

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [27.45, 90.45],
#     columns=['lat', 'lon'])
#
# st.map(map_data)
###########################################################################

# import datetime
# today = st.date_input("today is ", datetime.datetime.now())
#
# the_time = st.time_input("The time is ", datetime.time())

############################################################################

x = st.slider('x')  # this is a widget
st.write(x, 'squared is', x * x)

#############################################################################


# # Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
#
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',

    0.0, 100.0, (25.0, 75.0)
)

##############################################################
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
#################################################################
#
# st.text('Fixed width text')
# st.markdown('_Markdown_') # italic
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.write(['st', 'is <', 3]) # list
# st.title('My title')
# st.header('My header')
# st.subheader('My subheader')
# st.code('for i in range(8): foo()')
# # * optional kwarg unsafe_allow_html = True
# st.caption('This is a small text in caption')

###################################################

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

    st.write("This is outside the container")
    st.write("*"*30)

##############################################################

# container = st.container()
# container.write("This is inside the container")
# st.write("This is outside the container")

# Now insert some more in the container
# container.write("This is inside too")

##############################################################

# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")
#
# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")
#
# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")