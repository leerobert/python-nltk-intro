# Sample code for stemming responses

import nltk, re
raw = open("reviews.txt").read() # read in the entire file as a single raw string
tokens = nltk.word_tokenize(raw) # tokenizes the raw string
text = nltk.Text(tokens)         # generate the text object
clean_text = ["".join(re.split("[.,;:!?'`-]", word)) for word in text]

from nltk.corpus import stopwords
stopwords = stopwords.words("english")
more_stopwords = ["", "nt", "cyberdyne"]
for word in stopwords:
    more_stopwords.append(word)
important_words = [word for word in clean_text if word.lower() not in more_stopwords]
lower_important_words = [word.lower() for word in important_words] 

# Set up a Porter Stemmer
from nltk.stem import porter  
stemmer = porter.PorterStemmer()

# Stem each word in the normalized important words list
stems = [stemmer.stem(word) for word in lower_important_words]

# Remove duplicates of the same stem by creating a set on the stem list
unique_stems = set(stems)
print unique_stems 
print "Total stems = ", len(stems), " | Unique stems = ", len(unique_stems)
