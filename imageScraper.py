# Simple tool for scraping images from web directories
# Works for images which are named using numbers 

# USAGE:
#       py imageScraper.py <url> <localPath> <firstNumber> <lastNumber>
# EXAMPLE: 
#       py imageScraper.py http://kam-szalma.sk/images/gallery/referencie/ imageScraperOutput/ 1 100

import urllib.request as ul
import requests
import sys
import os

welcome = print("\n\t* This is a simple tool for scraping images from web directories",
                "\n\t* Images need to be named by numbers only and the default extension is .jpg (needs to be changed in source)", 
                "\n\t*\n\t* USAGE:\n\t*\tpy imageScraper.py <url> <localPath> <firstNumber> <lastNumber>",
                "\n\t* EXAMPLE:\n\t*\tpy imageScraper.py http://kam-szalma.sk/images/gallery/referencie/ imageScraperOutput/ 1 100")

try:
    url = sys.argv[1]
    localPath = sys.argv[2]
    first = int(sys.argv[3])
    last = int(sys.argv[4]) + 1

    if not os.path.isdir(localPath):
        os.mkdir(localPath)

    for x in range(first,last):
        s_url = url + str(x) + ".jpg"
        response = requests.get(s_url)

        if(response.status_code == 200):
            print ("[+] found :- ",s_url)
            s_localPath = localPath + str(x) + ".jpg"
            ul.urlretrieve(s_url ,s_localPath)

        else:
            print ("[-] Not found :- ",s_url)

except IndexError:
    welcome
    print("\n# ERROR: INVALID NUMBER OF ARGUMENTS GIVEN")

except ValueError:
    welcome
    print("\n# ERROR: INVALID TYPE OF ARGUMENTS GIVEN")



