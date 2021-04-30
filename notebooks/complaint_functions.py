import pandas as pd

# Fix borough values
def fix_borough_nulls(df, correct, min_lat, max_lat, min_long, max_long):
    mask = (df.BORO_NM != correct)\
        & (min_long < df['Longitude'])\
        & (df['Longitude'] < max_long)\
        & (min_lat < df['Latitude'])\
        & (df['Latitude'] < max_lat)

    index_values = df[mask].index

    df.iloc[index_values, [2]] = correct

    return index_values

# Swap borough values between existing values and correct ones
def swap_borough_values(df, current, correct, min_lat, max_lat, min_long, max_long):
    mask = (df.BORO_NM == current)\
        & (min_long < df['Longitude'])\
        & (df['Longitude'] < max_long)\
        & (min_lat < df['Latitude'])\
        & (df['Latitude'] < max_lat)

    index_values = df[mask].index

    df.iloc[index_values, [2]] = correct

    return index_values