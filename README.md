# data_viewer

This repository is intended to provide a way to quickly view results. 
Using pandas, ploty and streamlit to provide you with a quick way to understand you data quickly. 

##### Problem
Performing EDA repeatedly over 
### Repository structure
|Filename|Remarks
|-|-|
|/data/|location to store csv file|
|main.py|streamlit script written in python|
|requirements.txt|dependencies to run this|

### How to use
1. Create an environment and activate it.
   ``` 
   python -m venv venv
   
   # Activate the environment
   # On macOS/Linux
   source venv/bin/activate
   # On Windows
   # venv\Scripts\activate
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