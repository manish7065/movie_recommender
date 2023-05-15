import pickle
import requests
from flask import Flask, render_template, request,jsonify
from src.pipeline.prediction_pipeline import PredictPipeline
from src.pipeline.training_pipeline import TrainingPipeline

app = Flask(__name__)

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_movie = request.form['movie']
        recommended_movie_names,recommended_movie_posters = prediction_pipeline.recommend(selected_movie)
        return render_template('recommendations.html', recommended_movie_names=recommended_movie_names, recommended_movie_posters=recommended_movie_posters)
    return render_template('index.html', movie_list=movies['title'].values)

@app.route('/train',methods = ['GET','POST'])
def train():
    # training_pipeline=TrainingPipeline()
    # training_pipeline.initiate_training()
    return jsonify({'message': 'model successfully trained.'})
        

if __name__ == '__main__':
    # training_pipeline = TrainingPipeline()
    # training_pipeline.initiate_training()

    prediction_pipeline = PredictPipeline()
    movies,model=prediction_pipeline.mivie_list()
    # print(movies)

    # movies = pickle.load(open('movie_list.pkl', 'rb'))
    # similarity = pickle.load(open('similarity.pkl', 'rb'))
    app.run(host='0.0.0.0',port=5000,debug=True)
