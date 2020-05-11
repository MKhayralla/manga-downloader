manga_dict = {
    'attack' : 'https://ww7.readsnk.com/chapter/shingeki-no-kyojin-chapter',
    'nanatsu' : 'https://ww3.read7deadlysins.com/chapter/nanatsu-no-taizai-chapter',
    'piece' : 'https://ww7.readonepiece.com/chapter/one-piece-chapter',
    'hunter' : 'https://ww2.readhxh.com/chapter/hunter-x-hunter-chapter',
    'attack-colored' : 'https://ww7.readsnk.com/chapter/shingeki-no-kyojin-colored-chapter',
    'tgre' : 'https://tokyoghoulre-manga.com/manga/tokyo-ghoul-re-chapter'
}
def create_link(manga, chapter):
    if manga == 'hunter':
        return '{}-{}'.format(manga_dict[manga], int(chapter))
    return '{}-{:03d}'.format(manga_dict[manga], int(chapter))