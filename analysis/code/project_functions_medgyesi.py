import pandas as pd
import numpy as np
import folium

def load_and_process(url_or_path_to_csv_file):

    df = pd.read_csv("../data/processed/cost-of-living-RENAMED.csv")
    
# Two method chains, split into two as mentioned during feedback.

    canada_df = df.query('country == "Canada"')
    canada_df = (canada_df
             .rename(columns={'x48 (apartment 1BR city center)': 'apartment 1BR city center', 'x49 (apartment 1BR outside center)': 'apartment 1BR outside center', 
                              'x50 (apartment 3BR city center)': 'apartment 3BR city center', 'x51 (apartment 3BR outside center)': 'apartment 3BR outside center',
                              'x52 (price per sqm city center)': 'price per sqm city center', 'x53 (price per sqm outside center)': 'price per sqm outside center', 
                              'x54 (average monthly net salary)': 'average monthly net salary', 'x55 (mortgage interest rate)': 'mortgage interest rate'})
             
             .assign(price_per_sqm = lambda x: x[['price per sqm city center', 'price per sqm outside center']].mean(axis=1))
             .assign(affordability_ratio = lambda x: x[['apartment 1BR city center', 'apartment 1BR outside center', 'apartment 3BR city center', 
                                                        'apartment 3BR outside center','price per sqm city center','price per sqm outside center']].sum(axis=1) / x['average monthly net salary'])
)
    canada_df = (canada_df
             .rename(columns={'price_per_sqm': 'price per sqm', 'affordability_ratio':'affordability ratio'})
             .sort_values(by=['affordability ratio'], ascending=False)
             .dropna()
)
    return canada_df

def new_map(df, aff_col, lat_col, lng_col, city_col):
    map = folium.Map(location=[df[lat_col].mean(), df[lng_col].mean()], zoom_start=5)
    for index, row in df.iterrows():
        ratio = row[aff_col]
        if ratio > 3.0:
            color = 'red'
        else:
            color = 'green'
        folium.Marker([row[lat_col], row[lng_col]], popup=row[city_col], icon=folium.Icon(color=color)).add_to(map)
        
    return map
