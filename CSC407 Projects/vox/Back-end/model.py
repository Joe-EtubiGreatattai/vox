import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Read in the dataset
conversations_df = pd.read_csv("voxSpeechTrain/movie_conversations.tsv", delimiter="\t", skiprows=32288)
lines_df = pd.read_csv("voxSpeechTrain/movie_lines.tsv", delimiter="\t", skiprows=32288)



# Merge the two dataframes
merged_df = pd.merge(conversations_df, lines_df, on='lineID')

# Create the input and output data
X = merged_df['text']
y = merged_df['character_name']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a CountVectorizer to convert the text data into numerical data
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Create a Multinomial Naive Bayes model
clf = MultinomialNB()

# Train the model on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Print the accuracy of the model
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model to disk
import pickle
with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump(clf, f)
