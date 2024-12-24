from gensim.models.doc2vec import Doc2Vec, TaggedDocument
documents = [TaggedDocument(words=["Elon", "Musk", "is", "the", "CEO", "of", "Tesla"], tags=["1"]),
             TaggedDocument(words=["The", "Eiffel", "Tower", "is", "located", "in", "Paris"], tags=["2"])]
model = Doc2Vec(documents, vector_size=20, window=2, min_count=1, workers=4)
print(model.dv["1"])  # Lấy vector của câu 1
print(model.dv["2"])  # Lấy vector của câu 2