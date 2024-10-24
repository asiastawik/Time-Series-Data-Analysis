# Time Series Data Analysis and Visualization with Pandas

## Project Overview
This project involves analyzing time series datasets (extracted from R) using the `pandas` library. The tasks focus on loading, manipulating, and visualizing the data from a dataset named `a10.csv`. The project ensures compatibility across operating systems (Windows, Linux, Mac) and showcases different methods of data aggregation and visualization.

## Task 1: Download and Prepare Datasets
Download and unpack the archive containing the datasets (T02+L02 CSV files) from the specified location and place them in the `data` folder. This folder will be referenced in later tasks.

## Task 2: Loading the Dataset with Pandas
- The script imports the `pandas` library (`import pandas as pd`) and loads the `a10.csv` dataset from the `data` folder.
- The file path is constructed using `os.path.join(data, filename)` to ensure cross-platform compatibility.
- The dataset is loaded using `pd.read_csv()` with the "Month" column used as the index and automatic date parsing.
- A plot is generated for the "Cost" column from the dataset.

## Task 3: Aggregating Data and Plotting
Using the data loaded in Task 2:
- **Quarterly Aggregation:** The dataset is aggregated using the `resample()` method to compute quarterly minima, and the results are plotted.
- **Yearly Aggregation:** The dataset is aggregated to compute yearly minima, maxima, and means. These values are plotted in a single figure, enabling comparison of the trends over time.

## Task 4: Creating a Yearly Seasonal Plot
In this task, the dataset is used to produce a yearly seasonal plot:
- This plot visualizes the seasonality of the data on a yearly basis.
- **Hint for Plotting:** Do not parse the dates while loading the data this time. Use `a10.index` to access the index and split the strings on whitespace to manipulate the data.
- The `.loc[]` operator is used to select specific subsets of the dataframe for plotting.

## Libraries Used
- **Pandas** for data manipulation, time series analysis, and data aggregation.
- **Matplotlib** for data visualization.
