import pandas as pd
import json

df = pd.read_csv('movies_initial.csv') # read csv file

df.to_json('movies.json', orient='records') # convert to json file

with open('movies.json', 'r') as file:
    movies = json.load(file)

for i in range(100):
    movie = movies[i]
    print(movie)
    break