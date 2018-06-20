import urllib
import urllib.request
from bs4 import BeautifulSoup
import os


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


playerdatasaved = ""
soup = make_soup("https://www.basketball-reference.com/players/a/")
for record in soup.findAll('tbody'):
    playerdata = ""

    for data in record.findAll('tr'):
        playerdata = playerdata+","+data.text

    if len(playerdata)!=0:
        playerdatasaved =playerdatasaved + "\n" + playerdata[1:]

header="PLAYER,FROM,TO,POS,HT,WT,BIRTH DATE,COLLEGE"
file = open(os.path.expanduser("bb1.txt"),"wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))
