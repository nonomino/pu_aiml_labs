import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, cohen_kappa_score


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def to_dataframe(data):
    return pd.DataFrame({
        'text': [item['text'] for item in data],
        'lang': [item['langid'] for item in data]
    })


def run_model(model, X_train, y_train, X_test):
    model.fit(X_train, y_train)
    return model.predict(X_test)


train_data = to_dataframe(load_json("train.json"))
val_data = to_dataframe(load_json("valid.json"))

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_data['text'])
X_val = vectorizer.transform(val_data['text'])
y_train = train_data['lang']
y_val = val_data['lang']

for clf in [MultinomialNB(), LogisticRegression()]:
    preds = run_model(clf, X_train, y_train, X_val)
    print("Accuracy:", accuracy_score(y_val, preds))
    print("Kappa:", cohen_kappa_score(y_val, preds))

with open("output.txt", "w") as f:
    f.write("PUNIV01661\n")
    f.writelines([label + "\n" for label in preds])
