import urllib
import urllib.request
from bs4 import BeautifulSoup
import os


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


playerdatasaved = ""
soup = make_soup("https://www.basketball-reference.com/players/b/")
for record in soup.findAll('tbody'):
    playerdata = ""

    for data in record.findAll('tr'):
        playerdata = playerdata+","+data.text

    if len(playerdata)!=0:
        playerdatasaved =playerdatasaved + "\n" + playerdata[1:]

header="PLAYER,FROM,TO,POS,HT,WT,BIRTH DATE,COLLEGE"
file = open(os.path.expanduser("bb2.csv"),"wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))

def make_func(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


playerdatasaved = ""
soup = make_soup("https://www.basketball-reference.com/players/c/")
for record in soup.findAll('tbody'):
    playerdata = ""

    for data in record.findAll('tr'):
        playerdata = playerdata + "," + data.text

    if len(playerdata) != 0:
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "PLAYER,FROM,TO,POS,HT,WT,BIRTH DATE,COLLEGE"
file = open(os.path.expanduser("bb3.csv"), "wb")
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii", errors='ignore'))

