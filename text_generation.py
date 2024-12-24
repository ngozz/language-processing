from gensim.models import Word2Vec
sentences = [["I", "love", "this", "movie"], ["It", "was", "amazing"], ["I", "will", "watch", "it", "again"]]
model = Word2Vec(sentences, min_count=1)
# Tạo một câu mới từ các từ vựng đã học