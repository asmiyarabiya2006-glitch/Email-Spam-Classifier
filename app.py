from flask import Flask, render_template, request
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Create Flask app
app = Flask(__name__)


# Load dataset
df = pd.read_csv("data/spam.csv", encoding="latin-1")

# Keep required columns
df = df[["v1", "v2"]]

# Rename columns
df.columns = ["label", "message"]

# Convert labels into numbers
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})


# Split data
X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Convert text into numbers
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# Train model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

print("Spam classifier model trained successfully!")


# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        message = request.form["message"]

        message_tfidf = vectorizer.transform([message])

        prediction = model.predict(message_tfidf)

        if prediction[0] == 1:
            result = "SPAM"
        else:
            result = "HAM"

    return render_template(
    "index.html",
    result=result,
    accuracy=round(accuracy * 100, 2)
)


# Run application
if __name__ == "__main__":
    app.run(debug=True)