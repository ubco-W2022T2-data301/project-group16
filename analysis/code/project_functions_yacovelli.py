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
          .rename(columns = {
    'x1': 'x1 (meal cheap)',
    'x2': 'x2 (meal mid-range)',
    'x3': 'x3 (McMeal)',
    'x4' : 'x4 (beer domestic)',
    'x5': 'x5 (beer imported)',
    'x6': 'x6 (cappuccino)',
    'x7': 'x7 (Coke/Pepsi)',
    'x8': 'x8 (water resto)',
    'x9': 'x9 (milk)',
    'x10': 'x10 (bread)',
    'x11': 'x11 (rice)',
    'x12': 'x12 (eggs)',
    'x13': 'x13 (cheese local)',
    'x14': 'x14 (chicken fillets)',
    'x15': 'x15 (beef round)',
    'x16': 'x16 (apples)',
    'x17': 'x17 (bananas)',
    'x18': 'x18 (oranges)',
    'x19': 'x19 (tomatoes)',
    'x20': 'x20 (potatoes)',
    'x21': 'x21 (onions)',
    'x22': 'x22 (lettuce)',
    'x23': 'x23 (water 1.5L)',
    'x24': 'x24 (wine mid-range)',
    'x25': 'x25 (beer domestic 0.5L)',
    'x26': 'x26 (beer imported 0.33L)',
    'x27': 'x27 (cigarettes)',
    'x28': 'x28 (One-Way ticket transit)',
    'x29': 'x29 (monthly pass transit)',
    'x30': 'x30 (taxi start)',
    'x31': 'x31 (taxi 1km)',
    'x32': 'x32 (Taxi 1hr wait)',
    'x33': 'x33 (Gas 1L)',
    'x34': 'x34 (Volkswagen Golf)',
    'x35': 'x35 (Toyota Corolla Sedan)',
    'x36': 'x36 (basic utilities)',
    'x37': 'x37 (mobile tariff 1min)',
    'x38': 'x38 (internet)',
    'x39': 'x39 (fitness club)',
    'x40': 'x40 (tennis court rent)',
    'x41': 'x41 (cinema ticket)',
    'x42': 'x42 (preschool)',
    'x43': 'x43 (primary school)',
    'x44': 'x44 (jeans)',
    'x45': 'x45 (summer dress)',
    'x46': 'x46 (Nike running shoes)',
    'x47': "x47 (men's business shoes)",
    'x48': 'x48 (apartment 1BR city center)',
    'x49': 'x49 (apartment 1BR outside center)',
    'x50': 'x50 (apartment 3BR city center)',
    'x51': 'x51 (apartment 3BR outside center)',
    'x52': 'x52 (price per sqm city center)',
    'x53': 'x53 (price per sqm outside center)',
    'x54': 'x54 (average monthly net salary)',
    'x55': 'x55 (mortgage interest rate)',
}) 
)
    
    df2 = df2[[
    'city', 'country', 

    'x3 (McMeal)', #McDonalds

    #Groceries
    'x9 (milk)','x10 (bread)', 'x11 (rice)', 'x12 (eggs)', 'x13 (cheese local)',
    'x14 (chicken fillets)', 'x15 (beef round)', 'x16 (apples)',
    'x17 (bananas)', 'x18 (oranges)', 'x19 (tomatoes)', 'x20 (potatoes)',
    'x21 (onions)', 'x22 (lettuce)', 'x23 (water 1.5L)', 

    #Transport
    'x28 (One-Way ticket transit)', 'x29 (monthly pass transit)',
    'x30 (taxi start)', 'x31 (taxi 1km)', 'x32 (Taxi 1hr wait)',
    'x33 (Gas 1L)', 
    "x34 (Volkswagen Golf)", "x35 (Toyota Corolla Sedan)", 
   
    #Basic
    'x36 (basic utilities)',

    #Shelter
    'x48 (apartment 1BR city center)',
    'x49 (apartment 1BR outside center)', 'x50 (apartment 3BR city center)',
    'x51 (apartment 3BR outside center)', 'x52 (price per sqm city center)',
    'x53 (price per sqm outside center)',

    #Monthly net salary (after tax)
    'x54 (average monthly net salary)',  

    'data_quality']].copy()

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
  