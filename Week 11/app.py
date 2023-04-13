import streamlit as st 
import pandas as pd 
import numpy as np 
from google.cloud import firestore 
import os 
from datetime import datetime 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'khoobehiproject1-d15ce14710df.json'

db = firestore.Client()

st.sidebar.select_slider(label = 'date slider' options = df['date'])

reddit = db.collection(u'reddit')

posts = list(reddit.stream())

docs_dict = list(map(lambda x: x.to_dict(), posts))
df = pd.DataFrame(docs_dict)

df['date'] = df['created'].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y/%m/%d'))
df = df.loc[:, ['date', 'selftext', 'sentiment']]


st.dataframe(df)


