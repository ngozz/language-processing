from gensim.models import Word2Vec
sentences = [["I", "love", "this", "movie"], ["I", "hate", "this", "movie"], ["This", "movie", "is", "okay"]]
model = Word2Vec(sentences, min_count=1)
print(model.wv['love'])  # Vector của từ 'love'
print(model.wv['hate'])  # Vector của từ 'hate'
