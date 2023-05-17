import pickle
import requests
from flask import Flask, render_template, request,jsonify
from src.pipeline.prediction_pipeline import PredictPipeline
from src.pipeline.training_pipeline import TrainingPipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction_pipeline = PredictPipeline()
    movies,model=prediction_pipeline.movie_list()
    # print(movies)
    if request.method == 'POST':
        selected_movie = request.form['movie']
        recommended_movie_names,recommended_movie_posters = prediction_pipeline.recommend(selected_movie)
        return render_template('recommendations.html', recommended_movie_names=recommended_movie_names, recommended_movie_posters=recommended_movie_posters)
    return render_template('index.html', movie_list=movies['title'].values)

@app.route('/train',methods = ['GET','POST'])
def train():
    training_pipeline=TrainingPipeline()
    training_pipeline.initiate_training()
    return jsonify({'message': 'model successfully trained.'})
        

if __name__ == '__main__':
    # training_pipeline = TrainingPipeline()
    # training_pipeline.initiate_training()

    # prediction_pipeline = PredictPipeline()
    # movies,model=prediction_pipeline.mivie_list()
    # print(movies)

    # movies = pickle.load(open('movie_list.pkl', 'rb'))
    # similarity = pickle.load(open('similarity.pkl', 'rb'))
    app.run(host='0.0.0.0',port=5000,debug=True)
