# data_viewer

This repository is intended as a way to quickly view a dataset and provides the basic information commonly obtained when performing exploratory data analysis. 

This is achieve by using pandas, plotly and streamlit to process, visualize and serve the data. 

##### Problem
Performing EDA repeatedly over datasets can be  tedious. 

##### Solution 
Automate this process using a script. Getting the results within performing EDA on each file. 

##### Intended result
This will save some coding time and more effort can be spent on exploring the data itself.

### Repository structure
|Filename|Remarks
|-|-|
|/data/|location to store csv file|
|main.py|streamlit script written in python|
|requirements.txt|dependencies to run this|
|README.md|Description of this repository|

### How to use
##### Prerequisite
Python 3.11

1. Create an environment and activate it.
   ``` 
   # create the environment
   python -m venv venv
   
   # activate the environment
   # For macOS/Linux
   source venv/bin/activate

   # For Windows
   venv\Scripts\activate
   ```
2. Install dependencies.
   
   ```pip install -r requirements ```

3. Run the app
   ```
   streamlit run main.py
   ```

### Limitations:
1. Currently works with csv files for now


### Things to do
1. Highlight cells which has any missing data. Yellow cells for >10% and Red for <10%.
2. Display unique values in a cell.
3. Visualization tab - for simple plots so show column distribution univariate analysis.