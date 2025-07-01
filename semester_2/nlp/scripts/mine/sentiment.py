import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def compound_to_score(compound):
    if compound <= -0.6:
        return 1
    elif compound <= -0.2:
        return 2
    elif compound < 0.2:
        return 3
    elif compound < 0.6:
        return 4
    else:
        return 5

input_file = '../../data/sample_input.csv'
output_file = 'scores.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    sentences = [row[0] for row in reader]

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for sentence in sentences:
        compound = analyzer.polarity_scores(sentence)['compound']
        score = compound_to_score(compound)
        writer.writerow([score])