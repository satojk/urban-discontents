import logging
#from gensim.test.utils import common_texts
from gensim.test.utils import datapath
from gensim.utils import simple_preprocess
from gensim.models.ldamulticore import LdaMulticore
from gensim.corpora.dictionary import Dictionary
from bs4 import BeautifulSoup
import os

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

texts = []
for filename in ['codigo_civil.txt', 'codigo_processual.txt', 'constituicao.txt']:
    with open('data/{}'.format(filename)) as in_fp:
        texts.append(simple_preprocess(in_fp.read()))

common_dictionary = Dictionary(texts)
common_corpus = [common_dictionary.doc2bow(text) for text in texts]

lda = LdaMulticore(common_corpus, num_topics=10, workers=4, passes=60)

temp_file = datapath("model")
lda.save(temp_file)

with open('data/inquilinato.txt', 'r') as in_fp:
    text = simple_preprocess(in_fp.read())
other_corpus = [common_dictionary.doc2bow(text)]

print("\nAbout to throw in something...\n")

unseen_doc = other_corpus[0]
vector = lda.get_document_topics(unseen_doc)

print("\nThrown!!! Showing vector")
print(vector)
print("shown\n")

print(lda.get_term_topics('despejo'))

lda.update(other_corpus)
vector = lda[unseen_doc]
