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

tab1, tab2, tab3 = st.tabs(['Dataset Overview', 'Univariate Visualizer', 'Bivariate Visualizer'])
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
    # Let user select a column for histogram (only numeric columns)
    columns = df.columns
    # create 2 dropbox for user to chose columns to display and highlight

    selected_col = st.selectbox("Select a numeric column to plot histogram:", columns, index=0, key = 1)
    bins = st.slider("Number of bins", min_value=1, max_value=100, value=5, key=2) 

    # create 2 values inputs to define the range for both axis
    y_axis, x_axis = st.columns(2)
    with y_axis:
        # use value inputs NOT sliders,  2 inputs to create a range 
        y_min = st.number_input("#### Y-axis min", value=None, key=3)
        y_max = st.number_input("#### Y-axis max", value=None, key=4)

    with x_axis:
        x_min = st.number_input("#### X-axis min", value=None, key=5)
        x_max = st.number_input("#### X-axis max", value=None, key=6)

    color_plot = st.selectbox("Select a column to highlight the plot", columns, index=None, key =7 )        
    # create the plot
    fig = px.histogram(df, x=selected_col, 
                       nbins=bins, 
                       color=color_plot,
                       title=f"Histogram of {selected_col}")
    
    fig.update_yaxes(range=[y_min, y_max])
    fig.update_xaxes(range=[x_min, x_max])

    # display the plot
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    y_axis, x_axis = st.columns(2)
 
    # create 2 values inputs to define the range for both axis
    with y_axis:
        st.write("### Y-axis")
        bivariate_y_col = st.selectbox("Select a numeric column to plot histogram:", columns, index=1, key =8)
        # use value inputs NOT sliders,  2 inputs to create a range 
        bivariate_y_min = st.number_input("#### Y-axis min", value=None, key=10)
        bivariate_y_max = st.number_input("#### Y-axis max", value=None, key=11)

    with x_axis:
        st.write("### X-axis")
        bivariate_x_col = st.selectbox("Select a numeric column to plot histogram:", columns, index=2, key =12)
        bivariate_x_min = st.number_input("#### X-axis min", value=None, key=13)
        bivariate_x_max = st.number_input("#### X-axis max", value=None, key=14)

    bivariate_bins = st.slider("Number of bins", min_value=1, max_value=100, value=5, key=9) 
    bivariate_color_plot = st.selectbox("Select a column to highlight the plot", columns, index=None, key =15)    

    # create the plot
    bivariate_fig = px.histogram(df, x = bivariate_x_col, y = bivariate_y_col,
                        color = bivariate_color_plot,
                        title = f"Diagram of {bivariate_x_col} against {bivariate_y_col}")
    
    bivariate_fig.update_yaxes(range = [y_min, y_max])
    bivariate_fig.update_xaxes(range = [x_min, x_max])

    # display the plot
    st.plotly_chart(bivariate_fig, use_container_width=True)