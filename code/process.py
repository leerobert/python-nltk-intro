# Sample code for processing a file containing lines of raw text
import nltk

raw = open("reviews.txt").read() # read in the entire file as a single raw string
tokens = nltk.word_tokenize(raw) # tokenizes the raw string
text = nltk.Text(tokens)         # generate the text object

# Cleaning the text of punctuation
import re
clean_text = ["".join(re.split("[.,;:!?'`-]", word)) for word in text]

# Generating the list of stopwords
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
important_words = [word for word in clean_text if word.lower() not in stopwords]

# Adding to the list of stop words our own "black-list"
more_stopwords = ["", "nt", "cyberdyne"]
for word in stopwords:
    more_stopwords.append(word)
important_words = [word for word in clean_text if word.lower() not in more_stopwords]

# Lastly, we can normalize the text by lowercasing all the words
lower_important_words = [word.lower() for word in important_words] 

# Print the list to standard out
print lower_important_words
