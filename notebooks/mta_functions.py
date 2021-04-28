from sqlalchemy import create_engine
from os import path, listdir, remove
from dateutil.parser import parse
from datetime import timedelta
from hashlib import md5
import pandas as pd
import requests

def delete_directory_files(dir):
    for file in listdir(dir):
        try:
            remove(path.join(dir, file))
        except:
            raise Exception(f'Unable to delete {file}')

def download_files(weeks, start_date):
    date_time_obj = parse(start_date)
    turnstiles_folder = '../data/turnstiles'

    # delete_directory_files(turnstiles_folder)

    for week in range(weeks):
        file_date = date_time_obj + timedelta(week * 7)
        file_name = f'turnstile_{str(file_date.year)[2:]}{str(file_date.month).zfill(2)}{str(file_date.day).zfill(2)}.txt'
        file_url = f'http://web.mta.info/developers/data/nyct/turnstile/{file_name}'

        if not (path.isfile(f'{turnstiles_folder}/processed/{file_name}')) or (path.isfile(f'{turnstiles_folder}/processing/{file_name}')):
            r = requests.get(file_url)
    
            with open(f'{turnstiles_folder}/processing/{file_name}', 'wb') as f:
                f.write(r.content)

def df_from_directory(dir):
    lists = []

    for file in listdir(dir):
        f = path.join(dir, file)

        if path.isfile(f):
            try:
                lists.append(pd.read_csv(f, na_values = -1))
            except:
                raise Exception('Filetype was invalid')

    df = pd.concat(lists)

    return df

def df_append_to_table(df, table_name):
    # establish connection to sqlite database
    engine = create_engine('sqlite:///../data/db/mta.db', echo = False)
    conn = engine.connect()

    # conn.execute('')

    # create table from dataframe
    df.to_sql(table_name, conn, if_exists='replace', index = True)
    
    # close connection
    conn.close()

def df_from_table(table_name):
    # establish connection to sqlite database
    engine = create_engine('sqlite:///../data/db/mta.db', echo = False)
    conn = engine.connect()

    # Drop table exists if exists
    df = pd.read_sql(f'SELECT * FROM {table_name}', engine)
    
    # close connection
    conn.close()

    return df

def create_hashed_column(str, max_length):
    return md5(str.encode('utf-8')).hexdigest().upper()[:max_length]

# print(create_hashed_column('N039R25101-00-0196 STBCIND03/27/202000:00:00', 16))
# print(create_hashed_column('N409R26800-00-04METROPOLITAN AVGLIND01/05/202016:00:00', 16))

# def concat_column_values(df, *columns):
#     df['Name'] =  + df['LastName'].map(str)

def concat_columns(df, columns):
    return df[columns].values.sum(axis=1)

# def create_hashed_column(df, new, old):
#     df[new] = pd.DataFrame(df[old])[0].str.encode('utf-8').apply(lambda x: (sha512(x).hexdigest().upper()))
    # df[new_column] = pd.DataFrame(df[list(columns)].values.sum(axis=1))[0].str.encode('utf-8').apply(lambda x: (sha512(x).hexdigest().upper()))
    # return df

 # Create filtered list of top x ranked stations during timeframe
def topStations(input_dataframe, top_x):
    top_stations = set()

    for idx, row in input_dataframe.iterrows():
        top_stations |= set(row[row > 0].sort_values(ascending=False).head(top_x).index)

    return list(top_stations)