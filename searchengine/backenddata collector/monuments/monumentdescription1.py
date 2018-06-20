from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os




theurl = urlopen(Request("http://www.culturalindia.net/monuments/india-gate.html", headers={'User-Agent': 'Mozilla'}))
soup = BeautifulSoup(theurl,"html.parser")

header="INDIA GATE\n"
file = open(os.path.expanduser("mm2.txt"),"wb")
for record in soup.findAll("div"):
    for data in record.findAll("p"):
        set = data.text
        print(set)
        file.write(bytes(header, encoding="ascii", errors='ignore'))
        file.write(bytes(set, encoding="ascii", errors='ignore'))
file.close()

f = open('mm2.txt', 'r+')
n = f.read().replace(',', ',\n')
f.truncate(0)
f.write(n)
f.close()


