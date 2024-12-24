from gensim import corpora
from gensim.models import LdaModel

# Dữ liệu văn bản
texts = [['eiffel', 'tower', 'is', 'located', 'in', 'paris'],
         ['built', 'for', '1889', 'worlds', 'fair'],
         ['famous', 'landmark']]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# LDA mô hình
lda = LdaModel(corpus, num_topics=2, id2word=dictionary)
print(lda.print_topics())
