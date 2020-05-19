from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline

document = "doc1.txt"
  
vectorizer = TfidfVectorizer(stop_words='english', 
                             use_idf=True, 
                             smooth_idf=True)
                             
svd_model = TruncatedSVD(n_components=100,        
                         algorithm='randomized',
                         n_iter=10)

svd_transformer = Pipeline([('tfidf', vectorizer), 
                            ('svd', svd_model)])
                            
svd_matrix = svd_transformer.fit_transform(document)
