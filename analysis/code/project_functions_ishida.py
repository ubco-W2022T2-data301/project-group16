import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rename = ['city','country','Meal(Inexpensive)','Meal(Mid-Range)','McMeal','Domestic_Beer(restaurant)',
          'Imported_Beer(restaurant)','Cappuccino','Coke/Pepsi','Water(restaurant)','Milk','Bread','Rice','Eggs','Cheese',
          'Chicken_Fillets','Beef_Round','Apple','Banana','Oranges','Tomato','Potato','Onion','Lettuce','Water(market)',
          'Bottle_of_Wine','Domestic_Beer(market)','Imported_Beer(market)','Cigarettes','One-way_Ticket','Monthly_Pass',
          'Taxi_Start','Taxi_1km','Taxi_1hour_Waiting','Gasoline','Volkswagen','Toyota','Basic_for_Apartment',
          'Prepaid_Mobile_Tariff_Local','Internet','Fitness_Club','Tennis_Court_Rent','Cinema','Preschool',
          'International_Primary_School','Jeans','Summer_Dress','Running_Shoes','Business_Shoes',
          'Apartment(1_bedroom)_in_City_Centre','Apartment(1_bedroom)_Outside_of_Centre',
          'Apartment(3_bedrooms)_in_City_Centre','Apartment_(3_bedrooms)_Outside_of_Centre','Price_to_Buy_Apartment_in_City_Centre',
          'Price_to_Buy_Apartment_Outside_of_Centre','Net_Salary','Mortgage_Interest_Rate','data_quality']

def clean(dataframe):
    # Drop cities with NaN value
    new_df = dataframe.dropna()
    # Drop data needs to be improved
    new_df_filtered = new_df[new_df['data_quality']==1]
    
    return new_df