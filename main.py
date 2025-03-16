import os
import streamlit as st
import pandas as pd 

st.set_page_config(layout='wide')

#define the folder location where the csv should be kept
source_folder_location = './data/'
# defines a location to observe for csv files
file_list = [files for files in os.listdir(source_folder_location) if files.endswith('.csv')]
# I would like a sidebar to select the csv files to display
st.sidebar.title('File selection')
chosen_file = st.sidebar.selectbox(
    "Select file",
    (file_list),
)

# turns filepath into a dataframe
df=pd.read_csv(source_folder_location+chosen_file)

def column_summary(df):
    column_summaries=[]
    # '''This function is meant to collate the summary of a column within a dataframe'''
    # loop through every column in the dataframe
    for column in df.columns:
        # collect the data_type, missing data, etc
        column_dtype = df[column].dtype
        no_of_nulls = df[column].isnull().sum()
        no_of_non_nulls = df[column].notnull().sum()
        percentage_of_null_value= round((no_of_nulls/(len(df[column])))*100,2)
        no_of_distinct_values = df[column].nunique()

        # append this to column_summaries as a dictionary
        column_summaries.append({
            'column_name': column,
             'data_type': column_dtype,
             'count': no_of_non_nulls,
             'missing_values': no_of_nulls,
             'missing_values_percentage': percentage_of_null_value,
             'No. of unique values': no_of_distinct_values
            })
    sum_df = pd.DataFrame(column_summaries)
    return sum_df
sum_df = column_summary(df)
# Displaying the page

# Title of streamlit page
st.markdown('# Quick Data Analyzer')

tab1, tab2 = st.tabs(['Dataset Overview', 'Visualizations'])
with tab1:
    # display high level information of the dataset
    st.write(f'### Filename: "{chosen_file}"')
    st.markdown('##### Snippet of the file')
    st.dataframe(df.head())
    st.markdown('### Basic information')      
    col1,col2 = st.columns(2)
    with col1:
        st.metric('Number of Rows', df.shape[0])
    with col2:
        st.metric('Number of Columns', df.shape[1])

    st.markdown('##### Column information')
    st.dataframe(sum_df)
    st.markdown('##### Basic statistics')
    st.dataframe(df.describe())

