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

st.header('My Sentiment Model')
df = pd.read_csv("IMDB_movie_reviews_labeled.csv")
st.subheader('Training Data Sample')
st.dataframe(df.sample(5))
st.write(df.sentiment.value_counts())

pipeline = None

if st.button("Build My Pipeline"):
    ##Creating the pipeline/model 
    X = df.loc[:, ['review']]
    y = df.sentiment 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, stratify = y)
    X_train_docs = [doc for doc in X_train.review] 
    pipeline = Pipeline([
        ('vect', TfidfVectorizer(ngram_range = (1,2), stop_words = 'english', max_features = 10000)), 
        ('cls', LinearSVC()) 
    ])
    pipeline.fit(X_train_docs, y_train) 
    training_accuracy = cross_val_score(pipeline, X_train_docs, y_train, cv = 5).mean()
    st.subheader('Model Performance')
    st.write('Training Accuracy', training_accuracy)
    predicted = pipeline.predict([doc for doc in X_test.review])
    validation_accuracy = accuracy_score(y_test, predicted)
    st.write('Validation Accuracy', validation_accuracy)
    with open('pipeline.pk1', 'wb') as f: 
        pickle.dump(pipeline, f)




st.subheader("Testing the Model")
review_text = st.text_area("Movie Review")

if st.button('Predict'):
    with open('pipeline.pk1', 'rb') as f: 
        pipeline = pickle.load(f)
        sentiment = pipeline.predict([review_text]) 
        st.write('Predicted sentiment is:', sentiment)