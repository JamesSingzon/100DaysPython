import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

movies_html = response.text

soup = BeautifulSoup(movies_html, "html.parser")

ascending_movies = []
movies = soup.find_all(name="img", class_="landscape")
for movie in movies:

    rank_and_title = movie.get("title")
# rank = rank_and_title.split()[0]
# title = rank_and_title.split()[1].lstrip()
# print(rank_and_title)

    ascending_movies.insert(0, rank_and_title)

with open("movies.txt", mode="w") as file:
    for movie in ascending_movies:
        file.write(f"{movie}\n")