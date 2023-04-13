import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rename={
    'x1':'Meal(Inexpensive)',
    'x2':'Meal(Mid-Range)',
    'x3':'McMeal',
    'x4':'Domestic_Beer(restaurant)',
    'x5':'Imported_Beer(restaurant)',
    'x6':'Cappuccino',
    'x7':'Coke/Pepsi',
    'x8':'Water(restaurant)',
    'x9':'Milk',
    'x10':'Bread',
    'x11':'Rice',
    'x12':'Eggs',
    'x13':'Cheese',
    'x14':'Chicken_Fillets',
    'x15':'Beef_Round',
    'x16':'Apple',
    'x17':'Banana',
    'x18':'Oranges',
    'x19':'Tomato',
    'x20':'Potato',
    'x21':'Onion',
    'x22':'Lettuce',
    'x23':'Water(market)',
    'x24':'Bottle_of_Wine',
    'x25':'Domestic_Beer(market)',
    'x26':'Imported_Beer(market)',
    'x27':'Cigarettes',
    'x28':'One-way_Ticket',
    'x29':'Monthly_Pass',
    'x30':'Taxi_Start',
    'x31':'Taxi_1km',
    'x32':'Taxi_1hour_Waiting',
    'x33':'Gasoline',
    'x34':'Volkswagen',
    'x35':'Toyota',
    'x36':'Basic_for_Apartment',
    'x37':'Prepaid_Mobile_Tariff_Local',
    'x38':'Internet',
    'x39':'Fitness_Club',
    'x40':'Tennis_Court_Rent',
    'x41':'Cinema',
    'x42':'Preschool',
    'x43':'International_Primary_School',
    'x44':'Jeans',
    'x45':'Summer_Dress',
    'x46':'Running_Shoes',
    'x47':'Business_Shoes',
    'x48':'Apartment(1_bedroom)_in_City_Centre',
    'x49':'Apartment(1_bedroom)_Outside_of_Centre',
    'x50':'Apartment(3_bedrooms)_in_City_Centre',
    'x51':'Apartment_(3_bedrooms)_Outside_of_Centre',
    'x52':'Price_to_Buy_Apartment_in_City_Centre',
    'x53':'Price_to_Buy_Apartment_Outside_of_Centre',
    'x54':'Net_Salary',
    'x55':'Mortgage_Interest_Rate',
    'x56':'data_quality'
}

def load_and_process(url_or_path_to_csv_file):
    #Draling with missing values, Update column names, no issuess on capitalization, 
    new_df = pd.read_csv(url_or_path_to_csv_file).rename(columns=rename).dropna()
    new_df_filtered = new_df[new_df['data_quality']==1]
    
    return new_df_filtered

def create_necessity_dataframe(dataframe):
    #removing unnecessary columns
    new_df = dataframe[['city','country','Milk','Bread','Rice','Eggs','Cheese','Chicken_Fillets','Beef_Round','Apple','Banana',
                        'Oranges','Tomato','Potato','Onion','Lettuce','Water(market)','One-way_Ticket','Monthly_Pass','Gasoline',
                        'Basic_for_Apartment','Internet','Preschool','International_Primary_School','Jeans','Summer_Dress',
                        'Running_Shoes','Business_Shoes','Apartment(1_bedroom)_in_City_Centre',
                        'Apartment(1_bedroom)_Outside_of_Centre']]
    return new_df


def create_luxuary_dataframe(dataframe):
    #removing unnecessary columns
    new_df = dataframe.drop(columns=['Milk','Bread','Rice','Eggs','Cheese','Chicken_Fillets','Beef_Round','Apple','Banana','Oranges',
                                     'Tomato','Potato','Onion','Lettuce','Water(market)','One-way_Ticket','Monthly_Pass','Gasoline',
                                     'Basic_for_Apartment','Internet','Preschool','International_Primary_School','Jeans',
                                     'Summer_Dress','Running_Shoes','Business_Shoes','Apartment(1_bedroom)_in_City_Centre',
                                     'Apartment(1_bedroom)_Outside_of_Centre','Mortgage_Interest_Rate','data_quality','Net_Salary'])
    return new_df

def load_and_process_2nd_data(url_or_path_to_csv_file):
    new_df = pd.read_csv(url_or_path_to_csv_file).drop(["city_ascii","province_id","lat","lng","timezone","ranking","postal","id"], axis=1)
    return new_df

def necessity_dataframe_by_category(dataframe):
    #create aggregated columns
    df_sorted_n = dataframe[['city','country']]
    df_sorted_n = df_sorted_n.assign(fruits_n=(dataframe['Apple']+dataframe['Banana']+dataframe['Oranges']+dataframe['Tomato']
                             +dataframe['Potato']+dataframe['Onion']+dataframe['Lettuce'])/7).assign(food_n=(dataframe['Milk']+dataframe['Bread']+dataframe['Rice']+dataframe['Eggs']+dataframe['Cheese']+dataframe['Chicken_Fillets']+dataframe['Water(market)'])/8).assign(transportation_n=(dataframe['One-way_Ticket']+dataframe['Monthly_Pass']+dataframe['Gasoline'])/3).assign(accommodation_n=(dataframe['Basic_for_Apartment']+dataframe['Internet']+dataframe['Apartment(1_bedroom)_in_City_Centre']+dataframe['Apartment(1_bedroom)_Outside_of_Centre'])/4).assign(Net_Salary=dataframe['Net_Salary'])
    
    return df_sorted_n
    
    
                                      
def luxuary_dataframe_by_category(dataframe):
    df_sorted_l = dataframe[['city','country']]
    df_sorted_l = dataframe.assign(food_l=lambda x: (x['McMeal']+x['Meal(Inexpensive)']+x['Meal(Mid-Range)'])/3).assign(drinks_l=lambda x:(x['Domestic_Beer(restaurant)'] + x['Imported_Beer(restaurant)'] + x['Cappuccino'] + x['Coke/Pepsi'] + x['Water(restaurant)'] + x['Bottle_of_Wine'] + x['Domestic_Beer(market)'] + x['Imported_Beer(market)'])/8).assign(transportation_l=lambda x:  (x['Taxi_Start'] + x['Taxi_1km'] + x['Taxi_1hour_Waiting'] + (x['Volkswagen']*(1/1000))+(x['Toyota']*(1/1000)) + x['Prepaid_Mobile_Tariff_Local'])/6).assign(accommodation_l = lambda x:(x['Apartment(3_bedrooms)_in_City_Centre'] + x['Apartment_(3_bedrooms)_Outside_of_Centre'] + x['Price_to_Buy_Apartment_in_City_Centre'] + x['Price_to_Buy_Apartment_Outside_of_Centre'])/4).assign(entertainment_l = lambda x:(x['Fitness_Club']+ x['Tennis_Court_Rent']+x['Cinema']+x['Jeans']+x['Summer_Dress']+x['Running_Shoes']+x['Business_Shoes'])/7).assign(Net_Salary=lambda x: x['Net_Salary'])

    return df_sorted_l[['city','country','food_l','drinks_l','transportation_l','accommodation_l','entertainment_l','Net_Salary']]