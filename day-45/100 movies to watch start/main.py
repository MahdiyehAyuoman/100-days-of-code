import re
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_website = response.text
# print(movie_website)


soup = BeautifulSoup(movie_website, 'html.parser')

## Get All 100 Top Movies Title
all_movies = soup.find_all(name='h3', class_="title")
all_movies_title = [title.get_text() for title in all_movies]
all_movies_title.reverse()
# print(all_movies_title)

## Make movies.txt file from the title of 100 top movies
with open('movies.txt', 'w', encoding='utf-8') as f:
    for titlle in all_movies_title:
        f.write(f"{titlle}\n")

f.close()
