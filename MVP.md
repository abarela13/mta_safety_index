# MVP

2020 MTA and Crime Complaint Data

## Workflow

1. Download and prepare database tables via 'db_preprocessing'.

2. EDA and data cleaning via 'mta_eda'.



## Notebooks

### db_preprocessing

- Minimal cleaning and preparation of raw data for the creation of tables.

### mta_eda

- Generating unique ids for turnstiles and turnstiles entries.

- Addressing duplicate values.

- Creation of additional date related columns.

- Calculating traffic per turnstile per entry.

### arrest

- Cleaning the complaint data of 2020
- Preparing data for vizualizations in tableau
- Standarize and group similar crimes
- Filter out irrelevant crime that travelers would be concerned with

### stations_coordinates

- Cleaning and standardizing naming of stations for creation of table.

- Joined with 'stations' table

## Python files

### mta_functions

MTA specific helper functions

- Downloading of files.
- Creation of dataframe from downloaded files.
- Creation of tables from dataframes.
- Creation of dataframe from tables.
- Creation of columns with hashed values.
- Generation of concatenated strings for use in hash function.
- Identification of top 'x' station via set parameter.

### eda

General helper functions for the purpose of EDA

### mta_plots

Used for the creation of plots for mta data (will create similar for arrest data)