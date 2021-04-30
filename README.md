# MTA Safety Index

## Abstract
The goal of this project was to use MTA subway data and Arrest reports to assist tourists and non-locals in avoiding crime and navigating around the MTA network safely.

## Design
- Created ingest pipeline for MTA data for preperation into database
- Classifying Arrest Data into "Primary" categories

## Data
- [2020 NYPD Arrest Data](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date)
- [2020 MTA Data (March to May)](http://web.mta.info/developers/data/nyct/turnstile)

## Algorithms
- md5 hashing to create unique ID for entries (observations) to avoid conflict with future incoming data
- Identifying selectable number of top stations for given dataframe
- Correcting Arrest Data latitude and longitude contained within the space between two points

## Tools
- Tableau
- Seaborn
- Excel
- Matplotlib
- VSCode