from gensim.models import Word2Vec
sentences = [["apple", "is", "a", "fruit"], ["apple", "is", "a", "tech", "company"]]
model = Word2Vec(sentences, min_count=1)
print(model.wv.similarity('apple', 'fruit'))  # Đo độ tương tự giữa apple và fruit
print(model.wv.similarity('apple', 'tech'))   # Đo độ tương tự giữa apple và tech
