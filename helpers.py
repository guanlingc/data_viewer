import os
import pandas as pd
import plotly.express as px
import streamlit as st


def load_data(source_folder, chosen_file):
    """
    Loads data from a specified file within a source folder into a pandas DataFrame.
    Parameters:
        source_folder (str): The path to the folder containing the data file.
        chosen_file (str): The name of the file to load. Supported formats are .csv, .xlsx, and .json.
    Returns:
        pandas.DataFrame: The loaded data as a DataFrame.
    Raises:
        Displays a Streamlit error and stops execution if the file type is unsupported.
    """
    # get the file path 
    file_path = os.path.join(source_folder, chosen_file)
    # load data into a DataFrame based on file type
    if chosen_file.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif chosen_file.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    elif chosen_file.endswith('.json'):
        df = pd.read_json(file_path)
    else:
        st.error("Unsupported file type.")
        st.stop()
    return df

def column_summary(df):
    """
    Generate a summary of each column in a pandas DataFrame, including data type, count of non-null values, 
    count and percentage of missing values.
    Parameters:
        df (pandas.DataFrame): The DataFrame to summarize.
    Returns:
        pandas.DataFrame: A DataFrame containing the summary statistics for each column, with the following columns:
            - 'Column Name': Name of the column.
            - 'Data Type': Data type of the column.
            - 'Count': Number of non-null (non-missing) values in the column.
            - 'Missing values count': Number of missing (null) values in the column.
            - 'Missing values Percentage': Percentage of missing values in the column, rounded to two decimal places.
    """

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
    """
    Summarizes the unique values or value ranges for each column in a DataFrame.
    Parameters:
        df (pandas.DataFrame): The input DataFrame to analyze.
    Returns:
        pandas.DataFrame: A DataFrame with the following columns:
            - 'Column': The name of the column.
            - 'Unique Count': The number of unique (non-NA) values in the column.
            - 'Values / Range': For numeric columns, the minimum and maximum values as a range string.
                               For non-numeric columns, up to 5 unique values as a comma-separated string,
                               followed by "..." if there are more than 5 unique values.
    """

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

