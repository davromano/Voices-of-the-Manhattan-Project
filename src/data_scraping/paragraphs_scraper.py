
from bs4 import BeautifulSoup
import requests
import re

def paragraphs_scraper(url):
    # Send a GET request to the URL and get the response
    response = requests.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div element with the class name "is-layout-constrained entry-content wp-block-post-content"
    div_element = soup.find('div', {'class': 'is-layout-constrained entry-content wp-block-post-content'})

    # Find all paragraph elements within the div element
    paragraphs = div_element.find_all('p')

    # Process each paragraph
    HTML_transcript = ""
    for paragraph in paragraphs:
        # Remove the content inside <strong> tags
        strong_tags = paragraph.find_all('strong')
        for tag in strong_tags:
            tag.extract()

        # Append the paragraph with tags to HTML_transcript
        HTML_transcript += str(paragraph) + " "
    
    # Find the interviewee name
    name_tag = soup.find('h1', {'class': 'wp-block-post-title'})
    name_temp = name_tag.text.strip()
    #name = re.sub(r"’s Interview$", "", name_temp)
    name=name_temp.split("’s Interview")[0]

    # Find the interview date
    date_tag = soup.find('div', {'class': 'inline-comma-separated-list mb-10 nm-text-field'})
    if date_tag !=None:
        date_content_tag = date_tag.find('div', {'class': 'content'})
        interview_date = date_content_tag.text.strip()
    else:
        interview_date=[]
    
    return {
        "name": name,
        "interview_date": interview_date,
        "HTML_transcript": HTML_transcript,
    }
