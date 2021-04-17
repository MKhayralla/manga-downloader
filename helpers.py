import os
import re

#url decoding
from urllib.parse import unquote

def initiate_app():
    if ('downloads' not in os.listdir()):
        os.mkdir('downloads')
    return ('{}/downloads'.format(os.getcwd()))

def generate_img_url(url):
    result = url[url.find('&url=')+5:] if url.find('&url=') > -1 else url
    result = unquote(result)
    match = re.match(r'.*\.(jpg|png|jpeg)', result)
    return match.group(0) if match else result
    