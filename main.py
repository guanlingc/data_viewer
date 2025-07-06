import os
import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.express as px
from helpers import column_summary, column_unique_values, load_data

st.set_page_config(layout='wide', page_title="Quick Data Viewer")

# define the folder location where the csv should be kept
source_folder_location = './data/'

# define common filetypes and store in variable
allowed_ext = ('.csv', '.xlsx', '.json')
file_list = [files for files in os.listdir(source_folder_location) if files.endswith(allowed_ext)]
# I would like a sidebar to select the csv files to display
st.sidebar.title('File selection')
chosen_file = st.sidebar.selectbox("Select file",file_list)

# pass in the chosen file
df = load_data(source_folder_location,chosen_file)
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
    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric('### Number of Rows', df.shape[0])
    with col2:
        st.metric('### Number of Columns', df.shape[1])
    with col3:
        st.metric('### Number of Duplicates', df.duplicated().sum())

    st.markdown('#### Column information')
    st.dataframe(sum_df)

    st.markdown("#### Unique values for Column")
    st.dataframe(unique_df)

    st.markdown('#### Basic statistics')
    st.dataframe(df.describe())

    st.markdown('#### Correlation of the Features')
    corr = df.corr(numeric_only=True)
    heatmap_fig = px.imshow(corr, text_auto=True)
    st.plotly_chart(heatmap_fig)
    


with tab2:
    st.markdown("### Univariate Visualizer")
    # Let user select a column for histogram (only numeric columns)
    columns = df.columns
    # create 2 dropbox for user to chose columns to display and highlight
    column_choice, color_choice = st.columns(2)
    with column_choice:
        # 
        selected_col = st.selectbox("Select a numeric column to plot histogram:", columns)
        bins = st.slider("Number of bins", min_value=1, max_value=100, value=5) 
            
    with color_choice:
        color_plot = st.selectbox("Select a column to highlight the plot", columns, index=None)        

    # create 2 values inputs to define the range for both axis
    y_axis, x_axis = st.columns(2)
    with y_axis:
        # use value inputs NOT sliders,  2 inputs to create a range 
        y_min = st.number_input("#### Y-axis min", value=None)
        y_max = st.number_input("#### Y-axis max", value=None)

    with x_axis:
        x_min = st.number_input("#### X-axis min", value=None)
        x_max = st.number_input("#### X-axis max", value=None)

    
    fig = px.histogram(df, x=selected_col, 
                       nbins=bins, 
                       color=color_plot,
                       title=f"Histogram of {selected_col}")
    
    fig.update_yaxes(range=[y_min, y_max])
    fig.update_xaxes(range=[x_min, x_max])


    st.plotly_chart(fig, use_container_width=True)
