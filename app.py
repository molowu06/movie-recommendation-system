import streamlit as st
if "name" not in st.session_state:
    st.session_state["name"] = ""
import pandas as pd
import numpy as np
import time 
#pandas = powerful python library, used to create data frames
#can read data form csv files
#*** when ever streamlit doesnt update, type in python -m streamlit run app.py 

st.title("Hello Streamlit 🎉")
st.write("Streamlit is working!")

#find folder with cd.vscode
# use ls to find last used folder
st.write("first time using chart")
df = pd.DataFrame({# can also use st.table, or st.table(df) to make it interactive
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
    )
st.dataframe(dataframe.style.highlight_max(axis=0))
#highlight max number in colums
#st.dataframe(dataframe) for static tables

#charts 
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c']
    )
st.line_chart(chart_data)

#maps
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#widget
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


# You can access the value at any point with:
st.text_input("Your name", key="name")
st.session_state.name

#show and hide data 
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)



genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

st.write("You selected:", genre)

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'





