import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html,'html.parser')
    innermovietags = soup.select('td.titleColumn a')
    movietags = soup.select('td.titleColumn')
    ratings = soup.select('td.posterColumn span[name=ir]')


    def get_year(movie_tag):
        movie_split =  movie_tag.text.split()
        year = movie_split[-1]
        return year
    years = [get_year(tag) for tag in movietags]
    actor_list = [tag['title'] for tag in innermovietags]
    titles = [tag.text for tag in innermovietags]
    ratings_movie = [float(tag['data-value']) for tag in ratings]

    n_movies = len(titles)
    while(True):
        idx = random.randrange(0,n_movies)
        print(f' Movie : {titles[idx]} {years[idx]}, rating: {ratings_movie[idx] :.1f}, actors are : {actor_list[idx]}')

        user_input = (input("Another Movie (y/n)")).lower()
        if user_input != 'y':
            break

if __name__ == '__main__':
    main()