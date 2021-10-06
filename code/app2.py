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
from epicstore_api import EpicGamesStoreAPI, OfferData

def app():
    st.title("Games from Epic Store")
    st.markdown("-----")
    st.header("To Be Implemented...")
    
    """
    Print all games in filter range
    """
    api = EpicGamesStoreAPI()
    games = api.fetch_store_games(
        product_type='games/edition/base|bundles/games|editors',
        # Default filter in store page.
        count=30,
        sort_by='releaseDate',
        sort_dir='DESC',
        with_price=True,
    )
    epic_df = pd.DataFrame.from_dict(games, orient='index')
    #app_list = epic_df[['title','price']].reset_index(drop=True)
    #st.write('API Response:\n', json.dumps(games, indent=4))
    #st.write(epic_df)

