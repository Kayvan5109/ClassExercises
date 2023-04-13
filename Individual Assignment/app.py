import pickle
import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


# Load the SVM model and vectorizer from pickle files
with open("best_svm_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# Define a function to preprocess the user input
def preprocess_input(input_text):
    preprocessed_text = input_text.lower().strip()
    return preprocessed_text


# Define a function to classify the user input
def classify_sentiment(input_text):
    preprocessed_text = preprocess_input(input_text)
    X = vectorizer.transform([preprocessed_text])
    y_pred = model.predict(X)[0]
    return y_pred


# Define the Streamlit app
def app():
    # Set page title and icon
    st.set_page_config(page_title="Drug Review Sentiment Classifier", page_icon=":pill:")

    # Set app header
    st.header("Drug Review Sentiment Classifier")

    # Load the test dataset for performance evaluation
    test_df = pd.read_csv('test.csv')

    # Preprocess the test dataset
    test_df["text"] = test_df["benefits_review"] + " " + test_df["side_effects_review"] + " " + test_df["comments_review"]
    test_df["sentiment"] = test_df["rating"].apply(lambda x: 1 if x >= 5 else 0)
    X_test = vectorizer.transform(test_df["text"])
    y_test = test_df["sentiment"]

    # Evaluate the model performance on the test dataset
    test_preds = model.predict(X_test)
    test_acc = accuracy_score(y_test, test_preds)
    test_f1 = f1_score(y_test, test_preds)


    #Choosing the best model 
    st.subheader("Model Selection")
    st.write(f"After trying a Logstic Regression, SVM, and XGBoost model,  the SVM was chosen as the final model")
    st.write(f"The Logistic Regression model had an Accuracy Score of 0.8161290322580645 on the training dataset")
    st.write(f"The Logistic Regression model had F1 score of .8956043956043956 on the training dataset")
    st.write(f"The SVM model had an Accuracy Score of 0.8338709677419355 on the training dataset")
    st.write(f"The SVM model had F1 score of 0.8997078870496592 on the training dataset")
    st.write(f"The XGBoost model had an Accuracy Score of 0.8096774193548387 on the training dataset")
    st.write(f"The XGBoost model had F1 score of 0.8867562380038387 on the training dataset")

    # Display the model performance on the test dataset
    st.subheader("Model Performance on Test Dataset")
    st.write(f"Accuracy: {test_acc:.2f}")
    st.write(f"F1 Score: {test_f1:.2f}")

    # Show dataset summary and insights
    st.subheader("Dataset Summary and Insights")
    st.write(f"Number of reviews: {len(test_df)}")
    st.write(f"Number of positive reviews: {sum(test_df['sentiment'] == 1)}")
    st.write(f"Number of negative reviews: {sum(test_df['sentiment'] == 0)}")
    st.write(f"We can see that there is a slightly higher than 3 to 1 ratio of positive to negative reviews")
    st.write("")
    st.write("Here are some sample reviews:")
    st.write(test_df[["text", "sentiment"]].sample(n=5, random_state=42))

    # Show model summary and techniques used to improve it
    st.subheader("Model Summary and Techniques Used to Improve It")
    st.write("The model used in this app is a Support Vector Machine (SVM) classifier trained on a dataset of patient reviews on various prescription drugs. The goal of the model is to predict whether a patient's review is positive or negative based on the text of the review.")
    st.write("To improve the model performance, we used the following techniques:")
    st.write("- Text preprocessing: We cleaned and normalized the text data to remove noise and reduce sparsity.")
    st.write("- Feature engineering: We used the Term Frequency-Inverse Document Frequency (TF-IDF) vectorization technique to convert the text data into numerical features.")
    st.write("- Hyperparameter tuning: We used a grid search cross-validation approach to find the optimal hyperparameters for the SVM classifier.")


    # Show the user interface for testing the model
    st.subheader("Test the Model")
    user_input = st.text_input("Enter a drug review:", "")
    if user_input:
        y_pred = classify_sentiment(user_input)
        if y_pred == 1:
            st.write("The review is positive :smile:")
        else:
            st.write("The review is negative :disappointed:")

if __name__ == "__main__":
    app()


    