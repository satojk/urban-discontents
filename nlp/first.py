import logging
from gensim.test.utils import common_texts
from gensim.test.utils import datapath
from gensim.models.ldamulticore import LdaMulticore
from gensim.corpora.dictionary import Dictionary

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

common_dictionary = Dictionary(common_texts)
common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]

lda = LdaMulticore(common_corpus, num_topics=10)

temp_file = datapath("model")
lda.save(temp_file)

other_texts = [
  ['computer', 'time', 'graph'],
  ['survey', 'response', 'eps'],
  ['human', 'system', 'computer']
]
other_corpus = [common_dictionary.doc2bow(text) for text in other_texts]

print("\n\nAbout to throw in something...\n\n")

unseen_doc = other_corpus[0]
vector = lda[unseen_doc]

print("\n\nThrown!!! Showing vector\n\n")
print(vector)
print("\n\nshown\n\n")

lda.update(other_corpus)
vector = lda[unseen_doc]
