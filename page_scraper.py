
from bs4 import BeautifulSoup
import requests
import re

def page_scraper(url):

    # Send a GET request to the URL and get the response
    response = requests.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div element with the class name "is-layout-constrained entry-content wp-block-post-content"
    div_element = soup.find('div', {'class': 'is-layout-constrained entry-content wp-block-post-content'})
    transcript=div_element.text
    transcript = transcript.replace('\xa0', ' ')
    transcript = transcript.replace('\n', ' ')
    
    # Find the interviewee name
    name_tag = soup.find('h1', {'class': 'wp-block-post-title'})
    name_temp = name_tag.text.strip()
    #name = re.sub(r"’s Interview$", "", name_temp)
    name=name_temp.split("’s Interview")[0]
    
    #this is an auxiliary function because in some pages location is missing, so we have to manage this exception
    divs_1 = soup.find_all('div', {'class': 'inline-comma-separated-list mb-10 mt-10 nm-cdt-field'})

    manhattan_locations_div = None
    for div in divs_1:
        label = div.find('div', {'class': 'label'})
        if label and label.text.strip() == "Manhattan Project Locations:":
            manhattan_locations_div = div
            break
    
    if(manhattan_locations_div!=None):
        content_tag = manhattan_locations_div.find('div', {'class': 'content'})
        locations_list = content_tag.find('ul')
        locations = [li.text.strip() for li in locations_list.find_all('li')]
        for i in range(0,len(locations)):
            locations[i]=locations[i].split(",")[0]
    else:
        locations=[]

    # Find the biography
    biography_tag = soup.find('div', {'class': 'abstract nm-text-field'})
    biography_content_tag = biography_tag.find('div', {'class': 'content'})
    biography = biography_content_tag.find('p').text.strip()

    # Find the interview date
    date_tag = soup.find('div', {'class': 'inline-comma-separated-list mb-10 nm-text-field'})
    if date_tag !=None:
        date_content_tag = date_tag.find('div', {'class': 'content'})
        interview_date = date_content_tag.text.strip()
    else:
        interview_date=[]

    divs_2 = soup.find_all('div', {'class': 'inline-comma-separated-list mb-10 nm-cdt-field'})

    # Find the Collections div
    collections_div = None
    for div in divs_2:
        label = div.find('div', {'class': 'label'})
        if label and label.text.strip() == "Collections:":
            collections_div = div
            break

    # Find the Location of the Interview div
    location_of_interview_div = None
    for div in divs_2:
        label = div.find('div', {'class': 'label'})
        if label and label.text.strip() == "Location of the Interview:":
            location_of_interview_div = div
            break

    # Find the interview locations
    if(location_of_interview_div!=None):
        interview_locations_content_tag = location_of_interview_div.find('div', {'class': 'content'})
        interview_locations_list = interview_locations_content_tag.find('ul')
        interview_locations = [li.text.strip() for li in interview_locations_list.find_all('li')]
    else:
        interview_locations = []


    # Find the list of collections
    if(collections_div!=None):
        collections_content_tag = collections_div.find('div', {'class': 'content'})
        collections_list = collections_content_tag.find('ul')
        collections = [li.text.strip() for li in collections_list.find_all('li')]
    else:
        collections = []

    subjects_div = None
    for div in divs_1:
        label = div.find('div', {'class': 'label'})
        if label and label.text.strip() == "Subjects:":
            subjects_div = div
            break

    if(subjects_div!=None):
        subjects_content_tag = subjects_div.find('div', {'class': 'content'})
        subjects_list = subjects_content_tag.find('ul')
        subjects = [li.text.strip() for li in subjects_list.find_all('li')]
    else:
        subjects=[]

    tags_div = None
    for div in divs_1:
        label = div.find('div', {'class': 'label'})
        if label and label.text.strip() == "Tags:":
            tags_div = div
            break
    
    if(tags_div!=None):
        tags_content_tag = tags_div.find('div', {'class': 'content'})
        tags_list = tags_content_tag.find('ul')
        tags = [li.text.strip() for li in tags_list.find_all('li')]
    else:
        tags=[]
    
    return {
        "name": name,
        "transcript": transcript,
        "locations": locations,
        "biography": biography,
        "interview_date": interview_date,
        "interview_locations": interview_locations,
        "collections": collections,
        "subjects": subjects,
        "tags": tags
    }

