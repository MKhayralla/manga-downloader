import os

#url decoding
from urllib.parse import unquote

def initiate_app():
    if ('downloads' not in os.listdir()):
        os.mkdir('downloads')
    return ('{}/downloads'.format(os.getcwd()))

def generate_img_url(url):
    result = url[url.find('&url=')+5:] if url.find('&url=') > -1 else url
    result = unquote(result)
    extention = result.rfind('.')
    try:
        return result[0:extention+4]
    except:
        return result
    