# Sample code for examining frequencies
import nltk, re
raw = open("reviews.txt").read() # read in the entire file as a single raw string
tokens = nltk.word_tokenize(raw) # tokenizes the raw string
text = nltk.Text(tokens)         # generate the text object
clean_text = ["".join(re.split("[.,;:!?'`-]", word)) for word in text]

fdist = nltk.FreqDist(clean_text)
print "Distribution before normalization of stop words\n", fdist, "\n"

from nltk.corpus import stopwords
stopwords = stopwords.words("english")
more_stopwords = ["", "nt", "cyberdyne"]
for word in stopwords:
    more_stopwords.append(word)
important_words = [word for word in clean_text if word.lower() not in more_stopwords]
lower_important_words = [word.lower() for word in important_words] 

fdist_normalized = nltk.FreqDist(lower_important_words)
print "Distribution after normalization of stop words\n", fdist_normalized
