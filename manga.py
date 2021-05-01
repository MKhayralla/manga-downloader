manga_dict = {
    'attack' : 'https://ww7.readsnk.com/chapter/shingeki-no-kyojin-chapter',
    'nanatsu' : 'https://ww3.read7deadlysins.com/chapter/nanatsu-no-taizai-chapter',
    'piece' : 'https://ww7.readonepiece.com/chapter/one-piece-chapter',
    'hunter' : 'https://ww2.readhxh.com/chapter/hunter-x-hunter-chapter',
    'attack-colored' : 'https://ww7.readsnk.com/chapter/shingeki-no-kyojin-colored-chapter',
    'tgre' : 'https://manganelo.com/chapter/read_tokyo_ghoulre/chapter',
    'jjk' : 'https://www.read-jujutsu-kaisen.com/manga/jujutsu-kaisen-chapter',
    'demon' : 'https://demonslayer-mangaonline.com/manga/demon-slayer-kimetsu-no-yaiba-chapter',
    'demon-colored' : 'https://ww5.demonslayermanga.com/chapter/kimetsu-no-yaiba-digital-colored-comics-chapter'
}
def create_link(manga, chapter):
    if manga in ['hunter', 'jjk', 'demon']:
        return '{}-{}'.format(manga_dict[manga], int(chapter))
    if manga == 'tgre':
        return '{}_{}'.format(manga_dict[manga], int(chapter))
    return '{}-{:03d}'.format(manga_dict[manga], int(chapter))
