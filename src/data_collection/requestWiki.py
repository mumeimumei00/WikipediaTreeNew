import wikipediaapi
from bs4 import BeautifulSoup as bs
import requests
import sys
# from apiHandler import *
def get_first_elements(Page_Title):
    wiki = wikipediaapi.Wikipedia('WikipediaTree (test@hotmail.fr)', 'en')
    page = wiki.page(Page_Title)
    page_title = page.title.replace(" ", "_")
    page_url = page.fullurl
    # print(page_title)
    # print(page_url)
    summary = page.summary
    response = requests.get(f"https://en.wikipedia.org/w/api.php?action=parse&page={page_title}&format=json&prop=text")
    
    # print(response.status_code)
    if response.status_code != 200:
        return[]
    else:
        # print(summary)
        page_content = response.json()['parse']['text']['*']
        soup = bs(page_content, 'html.parser')
        # all_links = [[link.get_text(), summary.index(link.get_text())] for link in soup.find_all('a') if link.get_text() in summary and len(link.get_text())> 1 and summary.index(link.get_text())>0]
        all_links = list(set([link.get_text() for link in soup.find_all('a') if link.get_text() in summary and len(link.get_text())> 1]))
        links_index = [[words, summary.index(words)]for words in all_links if summary.index(words)>0]
        links_index.sort(key= lambda x : x[1])
        # all_links = set(all_links)
        # print(links_index)
        for x in range(5):
            print(links_index[x][0])


                    
get_first_elements(sys.argv)
