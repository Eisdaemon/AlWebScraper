import requests, os, bs4, re
from pathlib import Path
url = 'https://stammalexanderlion.de/fahrten-fotos/'
#Creates Folder
p = Path('E:/Bilder/AL')
os.makedirs (p, exist_ok = True)
Fahrten = []
#Gets websites, bypasse DDos protextion
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
res.raise_for_status
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#Gets all Bookmark
for a in soup.find_all('a', href= True, rel = 'bookmark'):
    Fahrten.append(a['href'])
#print(Fahrten)

for numBook in range(len(Fahrten)):
    #New Link
    bookMark = Fahrten[numBook]
    bilder = []
    num = 0
    #Make Magic bs4
    raj = requests.get(bookMark, headers={'User-Agent': 'Mozilla/5.0'})
    raj.raise_for_status
    stew = bs4.BeautifulSoup(raj.text, 'html.parser')
    print(bookMark)
    link, name = bookMark.split('/termine/')
    name, nothing = name.split('/')
    c = Path(p / name)
    os.makedirs(c, exist_ok = True)    
    print(name)
    #Get all Image Link
    for b in stew.find_all('a', {"class": "lightbox"}):
        bilder.append(b['href'])
        picUrl = bilder[num]
        print('Downloading %s...' % picUrl)
        print('\n')
        try:
            ras = requests.get(picUrl, headers={'User-Agent': 'Mozilla/5.0'})
            ras.raise_for_status()
        except:
            print('Something went wrong for %s' % picUrl)
        imageFile = open(os.path.join(c, os.path.basename(picUrl)), 'wb')
        for chunk in ras.iter_content(100000000):
            imageFile.write(chunk)
        imageFile.close
        num = num +1
print('All pictures Downloaded')