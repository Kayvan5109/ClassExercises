import streamlit as st 
import numpy as np 
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline 
import pickle

with open('pipeline.pk1', 'rb',) as f: 
    pipeline = pickle.load(f) 

df = pd.read_csv('reddit_posts.csv')
df = df.loc[df.selftext.notna(), :]

st.dataframe(df.selftext.sample(5))

test_docs = [doc for doc in df.selftext] 

predictions = pipeline.predict(test_docs)

df['predictions'] = predictions
df = df.loc[:, ['selftext', 'predictions']]

st.dataframe(df)
