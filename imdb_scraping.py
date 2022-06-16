from bs4 import BeautifulSoup
import requests




try:

    #gets html source code
    source = requests.get("https://www.imdb.com/chart/top/")

    source.raise_for_status()  #throws error if source is invalid
    
    soup = BeautifulSoup(source.text, 'html.parser') #takes html content and parses it, storing in variable soup

    movies = soup.find('tbody', class_= 'lister-list').find_all('tr')

    for movie in movies:

        name = movie.find('td', class_='titleColumn').a.text
        
        rank = movie.find('td', class_='titleColumn').get_text(strip= True).split('.')[0]

        year = movie.find('td', class_='titleColumn').span.text.strip('()')

        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text


    

        print(rank, name, year, rating)
        
        

    #print(len(movies)) 
    #print(movies)


except Exception as e:
    print(e)


