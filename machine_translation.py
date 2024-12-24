from gensim.models import FastText
sentences = [["I", "love", "this", "movie"], ["J'aime", "ce", "film"]]  # Dữ liệu song ngữ
model = FastText(sentences, min_count=1)
