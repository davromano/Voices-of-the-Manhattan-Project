from bs4 import BeautifulSoup
import requests
import re
from page_scraper import page_scraper
import pandas as pd

def main():
    main_url = 'https://ahf.nuclearmuseum.org/voices/oral-histories/'
    results = []

    # Loop through pages 1 to 60
    for page in range(1, 61):
        if page == 1:
            current_url = main_url
        else:
            current_url = f'{main_url}?_paged={page}'
        
        main_response = requests.get(current_url)
        main_soup = BeautifulSoup(main_response.content, 'html.parser')

        post_list = main_soup.find('div', {'class': 'post-list'})
        post_list_items = post_list.find_all('div', {'class': 'post-list-item'})

        urls = [item.find('a')['href'] for item in post_list_items]

        for url in urls:
            result = page_scraper(url)
            results.append(result)
        print(page)

    # Convert the list of dictionaries into a DataFrame
    results_df = pd.DataFrame(results)

    # Set the interviewee names as the index
    results_df.set_index('name', inplace=True)

    # Export the DataFrame to a CSV file
    results_df.to_csv('results.csv')

if __name__ == "__main__":
    main()