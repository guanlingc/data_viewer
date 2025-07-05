import os
import streamlit as st
import pandas as pd 
import plotly.express as px

st.set_page_config(layout='wide')

# define the folder location where the csv should be kept
source_folder_location = './data/'

# defines a location to observe for common filetypes
allowed_ext = ('.csv', '.xlsx', '.json')
file_list = [files for files in os.listdir(source_folder_location) if files.endswith(allowed_ext)]
# I would like a sidebar to select the csv files to display
st.sidebar.title('File selection')
chosen_file = st.sidebar.selectbox(
    "Select file",
    (file_list),
)

# turns filepath into a dataframe
file_path = os.path.join(source_folder_location, chosen_file)
if chosen_file.endswith('.csv'):
    df = pd.read_csv(file_path)
elif chosen_file.endswith('.xlsx'):
    df = pd.read_excel(file_path)
elif chosen_file.endswith('.json'):
    df = pd.read_json(file_path)
else:
    st.error("Unsupported file type.")
    st.stop()

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

        # append this to column_summaries as a dictionary
        column_summaries.append({
            'Column Name': column,
             'Data Type': column_dtype,
             'Count': no_of_non_nulls,
             'Missing values count': no_of_nulls,
             'Missing values Percentage': percentage_of_null_value,
            })
    # convert to a dataframe
    sum_df = pd.DataFrame(column_summaries)
    return sum_df

def column_unique_values(df):
    unique_info = []
    for col in df.columns:
        n_unique = df[col].nunique(dropna=True)
        if pd.api.types.is_numeric_dtype(df[col]):
            val_range = f"{df[col].min()} - {df[col].max()}"
            unique_info.append({
                "Column": col,
                "Unique Count": n_unique,
                "Values / Range": val_range
            })
        else:
            uniques = df[col].dropna().unique()
            # Show up to 5 unique values, then "..."
            if n_unique > 5:
                display_uniques = ", ".join(map(str, uniques[:5])) + ", ..."
            else:
                display_uniques = ", ".join(map(str, uniques))
            unique_info.append({
                "Column": col,
                "Unique Count": n_unique,
                "Values / Range": display_uniques
            })
    unique_df = pd.DataFrame(unique_info)
    return unique_df

sum_df = column_summary(df)
unique_df = column_unique_values(df)
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
        st.metric('### Number of Rows', df.shape[0])
    with col2:
        st.metric('### Number of Columns', df.shape[1])

    st.markdown('#### Column information')
    st.dataframe(sum_df)

    st.markdown("#### Unique values for Column")
    st.dataframe(unique_df)

    st.markdown('#### Basic statistics')
    st.dataframe(df.describe())

with tab2:
    st.markdown("### Column Distribution")
    # Let user select a column for histogram (only numeric columns)
    columns = df.columns
    col1, col2 = st.columns(2)
    with col1:
        #
        selected_col = st.selectbox("Select a numeric column to plot histogram:", columns)
        bins = st.slider("Number of bins", min_value=1, max_value=100, value=5)
        
            
    with col2:
        color_plot = st.selectbox("Select a column to highlight the plot", columns, index=None)        
        


    
    fig = px.histogram(df, x=selected_col, 
                       nbins=bins, 
                       color=color_plot,
                       title=f"Histogram of {selected_col}")
    
    


    st.plotly_chart(fig, use_container_width=True)