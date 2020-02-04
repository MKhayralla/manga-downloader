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

def download_chapter(chapter_number):
    #browser = webdriver.Chrome(options = chrome_options)
    print('loading chapter {} page'.format(chapter_number))
    res = get('https://ww7.readsnk.com/chapter/shingeki-no-kyojin-chapter-{}/'.format(chapter_number))
    soup = bs(res.content, 'html.parser')
    print('page loaded')
    #images = browser.find_elements_by_tag_name('img')
    images = soup.findAll('img')
    print('found {} images'.format(len(images)))
    #urls = list(map(lambda x: x.get_attribute('src'), images))
    urls = list(map(lambda x: x['src'], images))
    image_urls = list(map(lambda x: generate_img_url(x), urls))
    image_urls_final = [u for u in image_urls if u[u.rfind('.'):] != '.gif']
    print('found {} image urls'.format(len(image_urls_final)))
    #browser.close()
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
    parser.add_argument('chapters', help='chapters numbers', nargs='+')
    chapters = parser.parse_args().chapters
    for chapter in chapters:
        download_chapter(chapter)