import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd
import requests


class PredictPipeline:
    def __init__(self):
        pass
    
    def mivie_list(self):
            movie_data_path = os.path.join('artifacts','movie_data.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            movies = load_object(movie_data_path)
            model=load_object(model_path)
            return movies,model
    
    def fetch_poster(self,movie_id):
        try:

            url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
            data = requests.get(url)
            data = data.json()
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path

        except Exception as e:
            raise CustomException(e,sys)
        

    def recommend(self,movie):
        try:
            movies,model=self.mivie_list()

            index = movies[movies['title'] == movie].index[0]
            distances = sorted(list(enumerate(model[index])), reverse=True, key=lambda x: x[1])
            recommended_movie_names = []
            recommended_movie_posters = []
            for i in distances[1:6]:
                # fetch the movie poster
                movie_id = movies.iloc[i[0]].movie_id
                recommended_movie_posters.append(self.fetch_poster(movie_id))
                recommended_movie_names.append(movies.iloc[i[0]].title)

            return recommended_movie_names,recommended_movie_posters

        except Exception as e:
            raise CustomException(e,sys)
        
