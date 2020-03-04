#download files
from requests import get

#color mask
from masks import color_mask
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
#helper functions
from helpers import initiate_app, generate_img_url

#solo leveling novel
from sln import read_chapter as solo

def save_img(url, chapter_number, page_number):
    file_name = chapter_number+ str(page_number)+ url[url.rfind('.'):]
    print('downloading {} from {}'.format(file_name, url))
    res = get(url)
    with open(file_name, 'wb') as target:
        for chunk in res:
            target.write(chunk)
        target.close()
    return file_name

def download_chapter(manga, chapter_number, mask):
    if manga == 'sln':
        solo(chapter_number)
        return
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
    image_urls_final = [u for u in image_urls if u[u.rfind('.')+1:].lower() in ['png', 'jpg']]
    print('found {} image urls'.format(len(image_urls_final)))
    files = []
    for i, url in enumerate(image_urls_final):
        try:
            files.append(save_img(url, chapter_number, i))
        except:
            continue
    print('creating {}.pdf'.format(chapter_number))
    img_list = []
    if mask is not None:
        for f in files:
            try:
                img = Image.open(f).convert('RGB')
                img_list.append(color_mask(img, mask))
            except:
                continue
    else:
        for f in files:
            try:
                img_list.append(Image.open(f).convert('RGB'))
            except:
                continue
    pdf_path = initiate_app()
    img_list[0].save(r'{}/{}_{}.pdf'.format(pdf_path, manga, chapter_number), save_all = True, append_images = img_list[1:])
    print('deleting image files')
    for file in files:
        remove(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='popular manga downloader')
    parser.add_argument('manga', nargs='?', default='attack',
    choices=['hunter', 'attack', 'nanatsu', 'sln', 'piece', 'attack-colored'],
    help='manga name, defaulted to "attack"')
    parser.add_argument('-c', '--chapters',dest='chapters', help='chapters numbers to download, set if not using start and end')
    parser.add_argument('-s', '--start', dest='start', help='starting chapter to download, you should set -e or --end to use this option')
    parser.add_argument('-e', '--end', dest='end', help='last chapter to download, you should set -s or --start to use this option')
    parser.add_argument('-m', '--mask', dest='mask', help='color mask to cover the page with (for reducing eye strain)',
    choices=['red', 'green', 'blue', 'yellow'])
    args = parser.parse_args()
    manga = args.manga
    mask = args.mask
    if args.start is not None and args.end is not None:
        chapters = [str(i) for i in range(int(args.start), int(args.end) + 1)]
    elif args.chapters is not None:
        chapters = args.chapters.split(' ')
    else:
        parser.print_help()
        exit()

    for chapter in chapters:
        download_chapter(manga, chapter, mask)