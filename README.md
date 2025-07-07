# data_viewer

* Project Title:    Data Viewer
* Video Link:       https://youtu.be/28J2AI_3ZtY
* Name:             Chan Guan Ling
* Github Username:	guanlingc
* edX Username:		Guan_Ling_Chan
* Country: 			Singapore
* Data of recording:7 July 2025

# Description

This repository is intended as a quick way to view a dataset and provides the basic information commonly obtained when performing exploratory data analysis.


### Problem
-----------
Initial Exploratory Data Analysis (EDA) of a dataset is crucial in getting a glimpse of what the data is telling you. It will also inform you of what kind of techniques that are appropriate to clean the data or perform feature engineering for subsequent model training.

EDA typically consist of the same few steps, such as looking at it's shape, information of each columns, missing values etc.

This is usually done in a jupyter notebook and involves writing the same codes and generating a multitude of visualizations which becomes hard to keep track within the notebook itself.

### Solution
------------
The solution is a simple visualization app that displays all the relevant information that is typically investigated during EDA. This is achieved by automat this process by using a script to process the information. In the ideal world, the user just has to deposit the dataset in a folder and the script does the rest.

### Libraries used
|Library|Purpose|
|-|-|
|Pandas|A popular library for Data Manipulation and amongst Data Scientist|
|Plotly|A popular for Visualization of the Data|
|Seaborn|Used to generate the heatmap of the Data|
|Streamlit|Quick Way to deploy the FrontEnd which incorporates markdown language and some styling elements to rapidly deploy initial proof-of-concepts|

### Choice of libraries
-----------------------
Pandas is chosen as it is one of the most popular libraries for data manipulation. While there are other libraries such as Polars, Dask or Modin. Pandas is the most popular and therefore is integrated into other libraries as well. Polars is new and might have some compatibility issues, Dask specialises in parallel computing and modin is also experiemental. For Datasets less than 1M rows, Pandas is the perfect choice. For larger datasets, consider spark or dask.

Ploty is the visualization library of choice. Firstly, it is interactive, when you hover your mouse of the plot, the mouse cursor will display the information of the data point that you have currently highlighted. Secondly its visuals are more modern making it look cleaner compared to matplotlib which makes diagrams just as good but it looks much older.
Plotly express also allows the user to directly save plots as .png files which is a really neat feature for keeping diagrams for presentation purposes.

Streamlit is a library that allows you to quickly deploy a interative web applicaiton. The main benefits chose is that it simplifies the deployment proess instead of using HTML and CSS. Some of the nice features includes a hot reload, so you dont have to re-initialse the whole thing and it has integration with the pandas library and plotly as well making it an ideal choice


### Design
-----------
There are visualizers are split into 3 sections namely overview, univariate and bivariate comparisions. This is intended to allow the the user to understand the general sensus of the data before narrowing the scope down to a single column.

The overview page provides a snippet of the data itself. After which it shows the information dervied for `df.shape` and `df.info()`. Next would be missing values and unique values. The viewer shows you what unique values are present and any form of missing values exist within the dataset. Next would be, some statistical information of the dataset.

The next 2 pages provides the user with a interactive plot area. It allows user to choose the column information which they would like to investigate. Other features included is the ability to set the range of both x-axis and y-axi. The diagram can also be highlight with a column of interest to observe the distribution as well.

### Repository structure
| Filename      | Purpose/Remarks                        |
|---------------|----------------------------------------|
| `/data/`      | Folder to store your data files        |
| `main.py`     | Main Streamlit app script              |
| `helpers.py`  | Helper functions for data processing   |
| `requirements.txt` | Python dependencies               |
| `README.md`   | This documentation                     |


### How to use
##### Prerequisite
Python 3.11

1. Clone the repository
   ```
   git clone https://github.com/guanlingc/data_viewer.git
   cd data_viewer

2. Create an environment and activate it.
   ```
   # create the environment
   python -m venv venv

   # activate the environment
   # For macOS/Linux
   source venv/bin/activate

   # For Windows
   venv\Scripts\activate
   ```
3. Install dependencies.

   ```pip install -r requirements ```

4. Place your `csv`/`xlsx`/`json` file into the data folder

5. Run the app
   ```
   streamlit run main.py
   ```

### Limitations:
1. Performance drops as the file gets larger.



