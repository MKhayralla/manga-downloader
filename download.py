#from selenium import webdriver #run an automated web browser
#from selenium.webdriver.chrome.options import Options #chrome options for selenium
#browser options
#chrome_options = Options()
#chrome_options.add_argument('--headless')

#download files
from requests import get

#manipulate html
from bs4 import BeautifulSoup as bs

#input arguments
import argparse

#create pdf
from PIL import Image

#delete images after making pdf
from os import remove

#manga url's
from manga import create_link

def generate_img_url(url):
    return url[url.find('&url=')+5:] if url.find('&url=') > -1 else url

def save_img(url, chapter_number, page_number):
    file_name = chapter_number+ str(page_number)+ url[url.rfind('.'):]
    print('downloading {} from {}'.format(file_name, url))
    res = get(url)
    with open(file_name, 'wb') as target:
        for chunk in res:
            target.write(chunk)
        target.close()
    return file_name

def download_chapter(manga, chapter_number):
    print('loading chapter {} page'.format(chapter_number))
    link = create_link(manga, chapter_number)
    print(link)
    # browser = webdriver.Chrome(options = chrome_options)
    # browser.get(link)
    # images = browser.find_elements_by_tag_name('img')
    # urls = list(map(lambda x: x.get_attribute('src'), images))
    # browser.close()
    res = get(link)
    soup = bs(res.content, 'html.parser')
    images = soup.findAll('img')
    urls = list(map(lambda x: x['src'], images))
    print('page loaded')
    print('found {} images'.format(len(urls)))
    image_urls = list(map(lambda x: generate_img_url(x), urls))
    image_urls_final = [u for u in image_urls if u[u.rfind('.'):] == '.png' or u[u.rfind('.'):] == '.jpg']
    print('found {} image urls'.format(len(image_urls_final)))
    files = []
    for i, url in enumerate(image_urls_final):
        files.append(save_img(url, chapter_number, i))
    print('creating {}.pdf'.format(chapter_number))
    img_list = [Image.open(f).convert('RGB') for f in files]
    img_list[0].save('{}.pdf'.format(chapter_number), save_all = True, append_images = img_list[1:])
    print('deleting image files')
    for file in files:
        remove(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='attack on titan manga downloader')
    parser.add_argument('manga', nargs='?', default='attack', choices=['attack', 'nanatsu'], help='manga name')
    parser.add_argument('-c', '--chapters',dest='chapters', help='chapters numbers', nargs='+')
    args = parser.parse_args()
    manga = args.manga
    chapters = args.chapters
    for chapter in chapters:
        download_chapter(manga, chapter)