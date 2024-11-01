import wikipediaapi
from bs4 import BeautifulSoup as bs
import requests
import sys
# from apiHandler import *
def get_first_elements(Page_Title,size = 5):
    wiki = wikipediaapi.Wikipedia('WikipediaTree (test@hotmail.fr)', 'en')
    page = wiki.page(Page_Title)
    if (page.exists()):
        page_title = page.title.replace(" ", "_")
        page_url = page.fullurl
        print(page_title)
        summary = page.summary
        response = requests.get(f"https://en.wikipedia.org/w/api.php?action=parse&page={page_title}&format=json&prop=text")

        if response.status_code != 200:
            return[]
        else:
            page_content = response.json()['parse']['text']['*']
            soup = bs(page_content, 'html.parser')
            
            all_links = list(set([link.get_text() for link in soup.find_all('a') if link.get_text() in summary and len(link.get_text())> 1]))
            links_index = [[words, summary.index(words)]for words in all_links if summary.index(words)>0]
            links_index.sort(key= lambda x : x[1])
           
            if len(links_index) == 0:
                print("This page does not exists, be more precise:")
            else:
                if len(links_index) < size:
                    size = len(links_index)
                else:
                    for x in range(size):
                        print(links_index[x][0])
    else:
        print("Page does not exists")


print(sys.argv)
if len(sys.argv) == 3: 
    get_first_elements(sys.argv[1], int(sys.argv[2]))
elif len(sys.argv) == 2:    
    get_first_elements(sys.argv[1])
else:
    print("Welcome to WikipediaTree, type a word you want to search:\n")
    # get_first_elements(input("")
