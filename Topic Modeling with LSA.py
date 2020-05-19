from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline

documents = ["doc1.txt", "doc2.txt", "doc3.txt"] 
  
vectorizer = TfidfVectorizer(stop_words='english', 
                             use_idf=True, 
                             smooth_idf=True)
                             
svd_model = TruncatedSVD(n_components=100,        
                         algorithm='randomized',
                         n_iter=10)

svd_transformer = Pipeline([('tfidf', vectorizer), 
                            ('svd', svd_model)])
                            
svd_matrix = svd_transformer.fit_transform(documents)
