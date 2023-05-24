# Movie Recommendation system

This project is a movie recommendar which suggest 5 similar genres movies as per your selection.

For this project using the TMDB kaggle [data]

The model has been trained on the IMDB movie [Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

Posters and images has been fetched through IDMB API. 

I am using stramlit to demonstrate the web app but in end to end project i am using flask for more accessability.


## Software & Tools Requirements
1. [Github]("https://github.com/manish7065")
2. [VS Code IDE]("https://code.visualstudio.com/")
3. [Git CLI]("https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line")
4. [Docker](https://www.docker.com/)

<br>

## Project Architecture

![Architech Image](/docs/architech.png)
<br>

## Home page 
![Training page](/docs/training1.png)<br>
![Training page](/docs/training2.png)

<br>

## Movie selection page

![Training page](/docs/recommender.png)

<br>

## Recommended movies

![Training page](/docs/spider_man.png)
![Training page](/docs/avatar.png)



# To run the project on your follow stepwise:

## Clone the repo
```
git clone https://github.com/manish7065/movie_recommander.git
```

## Create New Environment
```
python -m venv env
```
## Install the requirements
```
pip install -r requirements
```

## Run the web app.
```
python main.py
```