# manga-downloader
###### Mahmoud Khayrallah
a script to download famous manga

### available manga
<ul>
<li> attack on titan (SNK)</li>
<li> 7 deadly sins (nanatsu no taizai)</li>
<li> solo leveling (light novel)</li>
<li> one piece </li>
<li> hunterXhunter (hunter) </li>
</ul>

### how to start

use ` pip install -r requirements.txt ` in the terminal

### simple usage

` $ python download.py [-h] [-c CHAPTERS [CHAPTERS ...]] [-s START] [-e END] [-m {red,green,blue,yellow}] [{attack,nanatsu,......}] `

positional arguments:

  {attack,nanatsu,sln,piece,hunter}

                        manga name, defaulted to "attack"

optional arguments:

  -h, --help

                        show help message and exit

  -c CHAPTERS [CHAPTERS ...], --chapters CHAPTERS [CHAPTERS ...]

                        chapters numbers to download, set if not using start
                        and end
  -s START, --start START

                        starting chapter to download, you should set -e or
                        --end to use this option
                        
  -e END, --end END

                        last chapter to download, you should set -s or --start
                        to use this option

   -m {red,green,blue,yellow}, --mask {red,green,blue,yellow}
                        color mask to cover the page with (for reducing eye
                        strain)

### getting help

` $ python download.py --help `
