from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

url = 'https://www.imdb.com/chart/top/'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

ul = soup.find('ul', class_='ipc-metadata-list')

if not ul:
    print("❌ Could not find the movie list. IMDb may be blocking or hiding it with JavaScript.")
else:
    list_items = ul.find_all('li', class_='ipc-metadata-list-summary-item')
with open('movies.txt', 'w') as f:
    for li in list_items:
        name_tag = li.find('h3')
        movie_name = name_tag.text.strip() if name_tag else "Unknown Title"

        meta_div = li.find('div', class_='cli-title-metadata')
        details_spans = meta_div.find_all('span') if meta_div else []

        year = details_spans[0].text.strip() if len(details_spans) > 0 else "N/A"
        duration = details_spans[1].text.strip() if len(details_spans) > 1 else "N/A"
        age_rating = details_spans[2].text.strip() if len(details_spans) > 2 else "N/A"

        movie_rating = li.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
        rating_spans = movie_rating.find_all('span')
        rating = rating_spans[0].text.strip() if len(rating_spans) > 0 else "N/A"
        people_rated = rating_spans[1].text.strip() if len(rating_spans) > 0 else "N/A"
        
        f.write(f"{movie_name}\n")
        f.write(f"Release Year: {year}\n")
        f.write(f"Duration: {duration}\n")
        f.write(f"Age Rating: {age_rating}\n")
        f.write(f"Movie Rating: {rating}\n")
        f.write(f"People Rated: {people_rated}\n")
        f.write('-' * 40 +'\n')

        print(f"{movie_name} | Year: {year} | Duration: {duration} | Age Rating: {age_rating} | Movie Rating: {rating} | People Rated: {people_rated}")
        print("movies.txt Saved!")
        

            
            


            