import helper_functions.constants as c
import numpy as np
import pandas as pd

variable_ids = c.VARIABLE_IDS

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def request_url(start_day, start_month, end_day, end_month, variable_id):
    """Helper function for importing data from online. 
    Creates the URL based on the parameters for quering the data."""
    url =  f"https://api.fingrid.fi/v1/variable/{variable_id}/events/csv?start_time=2022-" 
    url += f"{start_month}-{start_day}T00%3A00%3A00z&end_time=2022-{end_month}-{end_day}T23%3A59%3A00z"

    return url

def get_whole_year(value_id, file_name):
    """Helper function for downloading data from Fingrid's online service."""
    dfs = []
    for i in range(len(months)):
        dfs.append(pd.read_csv(request_url(1, i+1,months[i],i+1, value_id), parse_dates=[0,1], index_col=0))
        print(i+1)
    df = pd.concat(dfs)
    df.to_csv("./data/" + file_name + ".csv", sep='\t', encoding='utf-8')
    return df

def get_master_df():
    """Returns the dataframe with all data from the folder data."""
    data_conversion = c.DATA_CONVERSION_NAMES
    dfs = []

    for item in data_conversion:
        temp = pd.read_csv(item, sep="\t", index_col=0, parse_dates=["start_time"])
        temp = temp.rename(columns = {"value": data_conversion[item]})
        temp = temp[data_conversion[item]]
        dfs.append(temp)

    master_df = pd.concat(dfs, axis = 1)


    consumption = pd.read_csv("./data/Electricity_consumption.csv", sep="\t", index_col=0, parse_dates=[0])
    production = pd.read_csv("./data/Electricity_production_in_Finland.csv", sep="\t", index_col=0, parse_dates=[0])


    consumption = consumption.rename(columns = {"value": "Consumption"})
    consumption = consumption["Consumption"]
    production = production.rename(columns = {"value" : "Production"})
    production = production["Production"]

    return master_df