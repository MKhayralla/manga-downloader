#from selenium import webdriver #run an automated web browser
#from selenium.webdriver.chrome.options import Options #chrome options for selenium
#browser options
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-extensions')

#get the page
from requests import get

#manipulate html
from bs4 import BeautifulSoup as bs

import os

def read_chapter(chapter_number):
    #browser = webdriver.Chrome(options = chrome_options)
    print('loading chapter {} page...'.format(chapter_number))
    #browser.get('https://kisslightnovels.info/novel/solo-leveling/solo-levelingi-{}'.format(chapter_number))
    html = get('https://kisslightnovels.info/novel/solo-leveling/solo-levelingi-{}'.format(chapter_number)).content
    print('page loaded, creating chapter text file')
    #div = browser.find_element_by_class_name('text-left')
    #paragraphs = div.find_elements_by_tag_name('p')
    soup = bs(html, 'html.parser')
    div = soup.find('div', {'class' : 'text-left'})
    paragraphs = div.findAll('p')
    text = [p.text for p in paragraphs]

    #browser.quit()
    if 'downloads' not in os.listdir():
        os.mkdir('downloads')
    cwd = os.getcwd()
    with open(r'{}/downloads/solo_leveling_novel_{}.txt'.format(cwd, str(chapter_number)), 'a') as target:
        for t in text:
            target.write('{}\n'.format(t))
        target.close()
    print('chapter printed successfully')
