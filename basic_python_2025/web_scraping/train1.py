import requests
import bs4
import re

def site_scraping(*args):
    '''
    this functions gets site url and return title, image linkes
    first get website url, then special class name
    '''
    response = requests.get(args[0])
    data = response.text
    
    html_structure = bs4.BeautifulSoup(data, features='html.parser')
    
    # Get the title of the page
    title = html_structure.title.text
    image_links = []

    # Get all images on the page
    for img in html_structure.find_all('img'):
        image_links.append(img['src']) 
    
    # get data from special class name
    data_from_special_class_name_list = html_structure.find_all(class_=args[1])
    data_from_special_class_name = [re.sub(r'[\n\t\u200c]+', '', data.text).strip() for data in data_from_special_class_name_list]

    
    # get export
    title_data = print("the title of site is ==>" ,title + "\n")
    image_url_data = print("the image links of site is ==>", image_links )
    special_class_name_data = print("the data from special class name is ==>", data_from_special_class_name )
    
    return title_data, image_url_data, special_class_name_data 

site_url = ''
special_class_name = ""

site = site_scraping(site_url, special_class_name)
print(site)