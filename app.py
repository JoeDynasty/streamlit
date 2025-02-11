import streamlit as st
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

st.title("My CE App") # Set the title of your page
st.header('Data Visulization Section') # Set a header for a section 
st.subheader('Subsection: Pie Chart Analysis') # Sets subheader for a subsection 
st.text('This section focuses on data proprocessing.') 
st.markdown('**This is some bold text**')

data = {
  'Age': [45, 55, 56, 67],
  'Name': ['John', 'Lisa', 'Max', 'Chris']
}

df = pd.DataFrame(data)

age = st.slider('your age', min_value = 0, max_value = 100) # Returns the value sected by the user

if st.button('Say Hello'): # Return True if the user clikcs the button
  st.write('Hello!')
             
show_df = st.checkbox('Show DataFrame')
             
if show_df:
  st.write(df)

df['Adult'] = df['Age'].apply(lambda x: 'Yes' if x >= 18 else 'No')

st.dataframe(df)

iris = datasets.load_iris()
df = pd.DataFrame(data = iris.data, columns = iris.feature_names)

st.dataframe(df)

st.write(df.describe())
feature = st.selectbox('Select a feature', df.columns)

fig, ax = plt.subplots()
ax.hist(df[feature], bins = 20)

ax.set_title(f'Histogram of {feature}')
ax.set_xlabel(feature)
ax.set_ylabel('Frequency')

st.pyplot(fig)
