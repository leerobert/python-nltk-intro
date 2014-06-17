import sys, numpy

## NLTK imports
from nltk.cluster import KMeansClusterer, euclidean_distance
import nltk.corpus
import nltk.stem

## Define module wide constants
stemmer_func = nltk.stem.snowball.EnglishStemmer().stem 
stopwords = set(nltk.corpus.stopwords.words('english') + ["cyberdyne"])
DEFAULT_NUM_CLUSTERS = 5
 
def normalize_word(word):
    return stemmer_func(word.decode('utf-8').lower())
 
def get_words(survey):
    words = set()
    for response in survey:
        for word in response.split():
            words.add(normalize_word(word))
    return list(words)
 
def vectorspaced(response):
    ''' Returns a vector of 1's for all the normalized words in the answer
	that are not a stop word as defined by the NLTK stopwords corpora.
	0's are inserted otherwise. 
	@param response The survey response to generate a vector for 
    '''
    response_components = [normalize_word(word) for word in response.split()]    
    return numpy.array([
        word in response_components and not word in stopwords
        for word in words], numpy.short)
 
if __name__ == '__main__':
 
    num_clusters = DEFAULT_NUM_CLUSTERS
    if len(sys.argv) == 2:
        num_clusters = int(sys.argv[1])
 
    with open("reviews.txt") as survey_file:
 
        responses = [line.strip() for line in survey_file.readlines()]
 
        words = get_words(responses)
 
	cluster = KMeansClusterer(num_clusters, euclidean_distance,
			repeats=100, avoid_empty_clusters=True)
        cluster.cluster([vectorspaced(response) for response in responses if response])
 
        classified_examples = [
                cluster.classify(vectorspaced(response)) for response in responses
            ]
 
        for cluster_id, title in sorted(zip(classified_examples, responses)):
            print cluster_id, title
