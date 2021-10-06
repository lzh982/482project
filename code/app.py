from flask import Flask
import streamlit as st
import csv
import datetime as dt
import json
import os
import statistics
import time
import numpy as np
import pandas as pd
import requests
#In order to run streamlit app, go to terminal and type streamlit run app.py

#function to get request from any APIs url
def app(): 
    def get_request(url, parameters=None):

        try:
            response = requests.get(url=url, params=parameters)
        except SSLError as s:
            print('SSL Error:', s)
            
            for i in range(5, 0, -1):
                print('\rWaiting... ({})'.format(i), end='')
                time.sleep(1)
            print('\rRetrying.' + ' '*10)              
            
            # recusively try again
            return get_request(url, parameters)

        if response:
            return response.json()
        else:
            # response is none usually means too many requests. Wait and try again 
            print('No response, waiting 10 seconds...')
            time.sleep(10)
            print('Retrying.')
            return get_request(url, parameters)

    #URL for steamspy API
    url = "https://steamspy.com/api.php"
    parameters = {"request": "all"}

    # request 'all' from steam spy and parse into dataframe
    json_data = get_request(url, parameters=parameters)
    steam_spy_all = pd.DataFrame.from_dict(json_data, orient='index')

    # generate sorted app_list dataframe from steamspy data
    app_list = steam_spy_all[['appid', 'name','price','discount','initialprice']].sort_values('price').reset_index(drop=True)

    #Create title
    st.title("GAMES FROM THE STEAM STORE")
    st.markdown("-----")

    #Create header
    st.header("Select Game")

    #Creates a select box on streamlit and stores selected game into variable
    game = st.selectbox("Select Game",app_list['name'])

    #Generates dataframe with selected game's attributes and cleans data 
    attributes_df = app_list[app_list['name']==game]

    #Converts columns from string to float
    attributes_df['price'] = attributes_df['price'].str.replace(',','').astype(float)
    attributes_df['discount'] = attributes_df['discount'].str.replace(',','').astype(float)
    attributes_df['initialprice'] = attributes_df['initialprice'].str.replace(',','').astype(float)

    #Converts prices to decimals 
    attributes_df['price'] = attributes_df['price']/100
    attributes_df['discount'] = attributes_df['discount']/100
    attributes_df['initialprice'] = attributes_df['initialprice']/100

    #Prints each specific attribute from game requested by user
    st.write("Game Title: ", attributes_df['name'])
    st.write("Current Price: ", attributes_df['price'])
    st.write("Current Discount: ", attributes_df['discount'])
    st.write("Initial Price: ", attributes_df['initialprice'])


