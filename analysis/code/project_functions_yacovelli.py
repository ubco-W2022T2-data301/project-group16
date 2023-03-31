import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign()
          
      )

    # Make sure to return the latest dataframe

    return df2 


def kelowna_index(df,cols:list,col_name:str):
 """
  Calculate a catagorical index, Kelowna BC Canada serving as baseline (100).
   
  Arguments:
    df -- DataFrame
    cols -- (list) list of columns that the index will be composed of
    col_name -- (str) Name of new 'index' column, ie: housing
  """
 df[f"{col_name}_cost"] = df[cols].sum(axis=1)
 df[f"{col_name}_index"] = df[f"{col_name}_cost"] /  df[df['city'] =='Kelowna'][f"{col_name}_cost"].values[0] * 100
 df.drop(columns=[f"{col_name}_cost"],inplace=True)
 return df
  