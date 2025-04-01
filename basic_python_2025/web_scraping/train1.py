import requests
from bs4 import BeautifulSoup
import re

def site_scraping(url, class_name):
    """
    Scrape a website and return title, image links, and data from a specific class name.
    
    Args:
        url (str): The URL of the website to scrape.
        class_name (str): The class name to extract data from.

    Returns:
        tuple: A tuple containing the title, image links, and extracted data from the given class.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    html_structure = BeautifulSoup(response.text, 'html.parser')

    # Extract the title
    title = html_structure.title.text.strip() if html_structure.title else "No title found"

    # Extract image links
    image_links = [img.get('src', '') for img in html_structure.find_all('img') if img.get('src')]

    # Extract data from the specified class name and clean it
    data_from_special_class_name = [
        re.sub(r'[\n\t\u200c]+', '', data.get_text()).strip()
        for data in html_structure.find_all(class_=class_name)
    ]

    # Output the extracted data
    print("The title of the site is ==> ", title)
    print("The image links of the site are ==> ", image_links)
    print("The data from the special class name are ==> ", data_from_special_class_name)

    return title, image_links, data_from_special_class_name

# Example usage
site_url = 'https://example.com'
special_class_name = 'example-class'

site = site_scraping(site_url, special_class_name)
print("Extracted Data: ", site)
