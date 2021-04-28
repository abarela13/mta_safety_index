import pandas as pd

def describe_df(df):
    describe_df = pd.DataFrame(df.min(), columns=['min'])
    describe_df['max'] = df.max()
    describe_df['mean'] = df.mean()
    describe_df['std'] = df.std()
    return describe_df

def identify_nulls(df):
    print('------------------Rows with Nulls------------------')
    return df[df.isnull().any(axis=1)]

def possible_outliers(df, column, row_value):
    print('-------------Rows with Possible Errors-------------')
    list = list(df.column == row_value)
    return list

def identify_duplicates(df, *args):
    print('--------------Possible Duplicate Rows--------------')
    columns = [column for column in args]
    dupes_df = df[df.duplicated(subset=columns, keep=False)]
    return dupes_df.sort_values(columns)

    # idx = df.index.iloc(row_index)
    # df.iloc[idx - 1 : idx + 1]

    # for file in listdir(dir):
    #     f = path.join(dir, file)

    #     if path.isfile(f):
    #         try:
    #             lists.append(pd.read_csv(f, na_values = -1))
    #         except:
    #             raise Exception('Filetype was invalid')

    # df = pd.concat(lists)

    # return df[df.isnull().any(axis=1)]