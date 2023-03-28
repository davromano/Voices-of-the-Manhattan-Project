
from bs4 import BeautifulSoup
import requests
import re

# URL of the web page to scrape
url = 'https://ahf.nuclearmuseum.org/voices/oral-histories/richard-moneys-interview/'

# Send a GET request to the URL and get the response
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div element with the class name "is-layout-constrained entry-content wp-block-post-content"
div = soup.find('div', {'class': 'is-layout-constrained entry-content wp-block-post-content'})

# Get all the paragraphs inside the div element
paragraphs = div.find_all('p')

# Print the text content of each paragraph
#for p in paragraphs:
    #print(p.get_text())

# Find the interviewee name
name_tag = soup.find('h1', {'class': 'wp-block-post-title'})
name_temp = name_tag.text.strip()
name = re.sub(r"’s Interview$", "", name_temp)

print("Interviewee Name:", name)

# Find the locations list
locations_tag = soup.find('div', {'class': 'inline-comma-separated-list mb-10 mt-10 nm-cdt-field'})
content_tag = locations_tag.find('div', {'class': 'content'})
locations_list = content_tag.find('ul')
locations = [li.text.strip() for li in locations_list.find_all('li')]

print("Locations:", locations)


# Find the biography
biography_tag = soup.find('div', {'class': 'abstract nm-text-field'})
biography_content_tag = biography_tag.find('div', {'class': 'content'})
biography = biography_content_tag.find('p').text.strip()

print("Biography:", biography)

# Find the interview date
date_tag = soup.find('div', {'class': 'inline-comma-separated-list mb-10 nm-text-field'})
date_content_tag = date_tag.find('div', {'class': 'content'})
interview_date = date_content_tag.text.strip()

print("Interview Date:", interview_date)

# Find the interview locations
interview_locations_tag = soup.find_all('div', {'class': 'inline-comma-separated-list mb-10 nm-cdt-field'})[0]
interview_locations_content_tag = interview_locations_tag.find('div', {'class': 'content'})
interview_locations_list = interview_locations_content_tag.find('ul')
interview_locations = [li.text.strip() for li in interview_locations_list.find_all('li')]

print("Interview Locations:", interview_locations)


# Find the list of collections
collections_tag = soup.find_all(class_='inline-comma-separated-list mb-10 nm-cdt-field')[1]
collections_content_tag = collections_tag.find('div', {'class': 'content'})
collections_list = collections_content_tag.find('ul')
collections = [li.text.strip() for li in collections_list.find_all('li')]

print("Collections:", collections)


subjects_tag = soup.find_all(class_='inline-comma-separated-list mb-10 mt-10 nm-cdt-field')[1]
subjects_content_tag = subjects_tag.find('div', {'class': 'content'})
subjects_list = subjects_content_tag.find('ul')
subjects = [li.text.strip() for li in subjects_list.find_all('li')]

print("Subjects:", subjects)

tags_tag = soup.find_all(class_='inline-comma-separated-list mb-10 mt-10 nm-cdt-field')[2]
tags_content_tag = tags_tag.find('div', {'class': 'content'})
tags_list = tags_content_tag.find('ul')
tags = [li.text.strip() for li in tags_list.find_all('li')]

print("Tags:", tags)