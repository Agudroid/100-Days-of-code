import requests
from bs4 import BeautifulSoup

def get_movies_page() -> str:
    page = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
    return page.content 
    
def get_html_page() -> BeautifulSoup:
    page = get_movies_page()
    page_html = BeautifulSoup(page, "html.parser")
    return page_html

def find_titles(html : BeautifulSoup) -> list:
    title_list = html.find_all("h3", class_="title")
    movie_list = [title.text for title in title_list]
    print(movie_list.reverse())
    return movie_list

def export_movies(movies_list: list):
    with open('movies.txt', mode="w") as file:
        for movie in movies_list:
            print(movie)
            file.write(f"{movie}\n")
    pass
    
html_page = get_html_page()
titles = find_titles(html_page)
export_movies(movies_list=titles)
