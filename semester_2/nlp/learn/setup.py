import nltk
import os

resources_to_check = [
    'tokenizers/punkt',
    'corpora/stopwords',
    'taggers/averaged_perceptron_tagger',
    'corpora/words',
    'corpora/wordnet',
    'omw-1.4'
]

def check_and_download_resources():
    for resource in resources_to_check:
        try:
            nltk.data.find(resource)
            print(f"Resource '{resource}' is already downloaded.")
        except LookupError:
            print(f"Resource '{resource}' not found. Downloading...")
            nltk.download(resource)
            print(f"Resource '{resource}' downloaded successfully.")

check_and_download_resources()

