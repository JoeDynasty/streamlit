import streamlit as st
st.title("My CE App") # Set the title of your page
st.header('Data Visulization Section') # Set a header for a section 
st.subheader('Subsection: Pie Chart Analysis') # Sets subheader for a subsection 
st.text('This section focuses on data proprocessing.') 
st.markdown('**This is some bold text**')

import pandas as pd

data = {
  'Age': [45, 55, 56, 67],
  'Name': ['John', 'Lisa', 'Max', 'Chris']
}

df.pd.DataFrame(data)

age = st.slider('your age', min_value = 0, max_value = 100) # Returns the value sected by the user

if st.button('Say Hello'): # Return True if the user clikcs the button
  st.write('Hello!')
             
show_df = st.checkbox('Show DataFrame')
             
if show_df:
  st.write(df)
