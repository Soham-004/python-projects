import pandas as pd

# Load the dataset
df = pd.read_csv("SMSSpamCollection", sep='\t', names=["label", "message"])

print(df.head())

#cleaning the data
# Convert labels to numbers
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Remove duplicates
df = df.drop_duplicates()

# Optional: Lowercase
df['message'] = df['message'].str.lower()

#text to number conversion
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english')

X = vectorizer.fit_transform(df['message'])
y = df['label']

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

import pickle

pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))