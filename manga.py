manga_dict = {
    'attack' : 'https://ww7.readsnk.com/chapter/shingeki-no-kyojin-chapter',
    'nanatsu' : 'https://ww3.read7deadlysins.com/chapter/nanatsu-no-taizai-chapter'
}
def create_link(manga, chapter):
    return '{}-{:03d}'.format(manga_dict[manga], int(chapter))