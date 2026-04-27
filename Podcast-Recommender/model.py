import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("podcasts.csv")

data['description'] = data['description'].fillna('')
data['genre'] = data['genre'].fillna('')

data['combined'] = data['genre'] + " " + data['description']

tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(data['combined'])

similarity = cosine_similarity(matrix)

def recommend(podcast):
    podcast = podcast.lower()

    if podcast not in data['title'].str.lower().values:
        return ["Podcast not found"]

    index = data[data['title'].str.lower() == podcast].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    top = scores[1:6]

    return [data.iloc[i[0]]['title'] for i in top]