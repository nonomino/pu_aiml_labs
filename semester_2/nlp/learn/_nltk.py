import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import words

# Downloads
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('words')

# Sample text
text = "I am running home. Then I will eat dinner."

# Sentence tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Word frequency distribution
fdist = FreqDist(tokens)
print("Word Frequency:", fdist.most_common())

# Stemming
stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in tokens]
print("Stems:", stems)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in tokens]
print("Lemmas:", lemmas)

# Dictionary lookup
english_vocab = set(words.words())
valid_words = [word for word in tokens if word.lower() in english_vocab]
print("Words in dictionary:", valid_words)
