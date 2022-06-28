from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np


df = pd.read_csv("shared_articles.csv")
df = df[df["soup"].notna()]


count = CountVectorizer(stop_words = 'english')
count_matrix = count.fit_transform(df1['soup'])
cosine_sim2 = cosine_similarity(count_matrix,count_matrix)
df1 = df1.reset_index()
indices = pd.Series(df1.index,index = df1["title"])
def getrecommendation(title,cosine_sim):
  idx = indices['title']
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores,key = lambda x:x[1],reverse = True)
  sim_scores = sim_scores[1:11]
  article_indices = [i[0] for i in sim_scores]
  return df2['title'].iloc[article_indices]