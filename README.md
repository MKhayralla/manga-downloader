# manga-downloader
###### Mahmoud Khayrallah
a script to download famous manga

### available manga
<ul>
<li> attack on titan (SNK)</li>
<li> 7 deadly sins (nanatsu no taizai)</li>
</ul>

### how to start

use ` pip install -r requirements.txt ` in the terminal

### simple usage

` $ python download.py [-h] [-c CHAPTERS [CHAPTERS ...]] [{attack,nanatsu}] `

positional arguments:

  {attack,nanatsu}      manga name, defaulted to "attack"

optional arguments:

  -h, --help            show help message and exit

  -c CHAPTERS [CHAPTERS ...], --chapters CHAPTERS [CHAPTERS ...]

                        chapters numbers to download, set if not using start
                        and end
  -s START, --start START

                        starting chapter to download, you should set -e or
                        --end to use this option
                        
  -e END, --end END     last chapter to download, you should set -s or --start
                        to use this option

### getting help

` $ python download.py --help `
