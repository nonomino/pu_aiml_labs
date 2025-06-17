import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords, words
from nltk.metrics.distance import edit_distance

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")
nltk.download("stopwords")
nltk.download("words")

text = "The rain in Spain stays mainy in the plain. What a glorious feeling of singing in the rain. I am singing, and dancing in the rain."

lower_text = text.lower()
tokens = word_tokenize(lower_text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
correct_spellings = set(words.words())

def get_tag(tag):
    if tag.startswith("NN"): return "n"
    if tag.startswith("JJ"): return "a"
    if tag.startswith("RB"): return "r"
    if tag.startswith("VB"): return "v"
    return "n"

tagged = pos_tag(tokens)

print("Lowercase Tokens:")
print(tokens)

print("\nStemmed Tokens:")
print([stemmer.stem(t) for t in tokens])

print("\nLemmatized Tokens:")
print([lemmatizer.lemmatize(t, pos=get_tag(tag)) for t, tag in tagged])

print("\nStopword Removed:")
print([t for t in tokens if t not in stop_words])

print("\nSpell Correction (Edit Distance 1):")
for t in tokens:
    if t.isalpha() and t not in correct_spellings:
        candidates = [w for w in correct_spellings if abs(len(w) - len(t)) < 2 and edit_distance(t, w) == 1]
        print(f"{t} -> {candidates}")
