from curses import use_default_colors
import requests
from bs4 import BeautifulSoup
import csv


items = []
#####models-for-advertising
url = 'https://depositphotos.com/stock-photos/models-for-advertising.htm'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
req = requests.get(url,header)
soup = BeautifulSoup(req.content, 'html.parser')
with open("file.csv", 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Page URL","Custom label"]
            )
for i in soup.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg = i.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg,'models-for-advertising.']
        )
for foto in range(1, 5):
    url1 = f'https://depositphotos.com/stock-photos/models-for-advertising.html?offset={foto*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req1 = requests.get(url1,headers)
    soup1 = BeautifulSoup(req1.content, 'html.parser')
    for q in soup1.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imeg1 = q.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imeg1,'models-for-advertising.']
        )
#####beauty-and-fashion
url2='https://depositphotos.com/stock-photos/beauty-and-fashion.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
reqo1 = requests.get(url2,header)
soup2 = BeautifulSoup(reqo1.content, 'html.parser')
for w in soup2.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg2 = w.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg2,'beauty-and-fashion.']
        )
for foto1 in range(1, 10):
    url3 = f'https://depositphotos.com/stock-photos/beauty-and-fashion.html?offset={foto1*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req2 = requests.get(url3,headers)
    soup3 = BeautifulSoup(req2.content, 'html.parser')
    for e in soup3.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs1 = e.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs1,'beauty-and-fashion.']
        )

####stock-photos/shopping.
url7 = 'https://depositphotos.com/stock-photos/shopping.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
reqo4 = requests.get(url7,header)
soup6 = BeautifulSoup(reqo4.content, 'html.parser')
for r in soup6.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg4 = r.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg4,'stock-photos/sale.']
        )
for foto34 in range(1, 10):
    url8 = f'https://depositphotos.com/stock-photos/shopping.html?offset={foto34*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req5 = requests.get(url8,headers)
    soup7 = BeautifulSoup(req5.content, 'html.parser')
    for t in soup7.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs5 = t.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs5,'stock-photos/shopping.']
        )
####stock-photos/sale
url4 = 'https://depositphotos.com/stock-photos/sale.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
req3 = requests.get(url4,header)
soup4 = BeautifulSoup(req3.content, 'html.parser')
for y in soup4.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg3 = y.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg3,'stock-photos/sale.']
        )
for foto2 in range(1, 10):
    url9 = f'https://depositphotos.com/stock-photos/sale.html?offset={foto2*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req4 = requests.get(url9,headers)
    soup5 = BeautifulSoup(req4.content, 'html.parser')
    for u in soup5.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs2 = u.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs2,'stock-photos/sale.']
        )
####stock-photos/fantasy-and-unicorns.
url5 = 'https://depositphotos.com/stock-photos/fantasy-and-unicorns.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
req7 = requests.get(url5,header)
soup8 = BeautifulSoup(req7.content, 'html.parser')
for o in soup8.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg5 = o.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg5,'stock-photos/fantasy-and-unicorns.']
        )
for foto6 in range(1, 3):
    url10 = f'https://depositphotos.com/stock-photos/fantasy-and-unicorns.html?offset={foto6*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req6 = requests.get(url10,headers)
    soup9 = BeautifulSoup(req6.content, 'html.parser')
    for p in soup9.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs3 = p.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs3,'stock-photos/fantasy-and-unicorns.']
        )

####stock-photos/banners
url11 = 'https://depositphotos.com/stock-photos/banners.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
req8 = requests.get(url11,header)
soup10 = BeautifulSoup(req8.content, 'html.parser')
for z in soup10.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg6 = z.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg6,'stock-photos/banners.']
        )
for foto10 in range(1, 10):
    URL1 = f'https://depositphotos.com/stock-photos/banners.html?offset={foto10*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req9 = requests.get(URL1,headers)
    soup11 = BeautifulSoup(req9.content, 'html.parser')
    for x in soup11.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs10 = x.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs10,'stock-photos/banners.']
        )
####stock-photos/social-media
url12 = 'https://depositphotos.com/stock-photos/social-media.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
req11 = requests.get(url12,header)
soup12 = BeautifulSoup(req11.content, 'html.parser')
for c in soup12.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg7 = c.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg7,'stock-photos/social-media.']
        )
for foto11 in range(1, 10):
    url32 = f'https://depositphotos.com/stock-photos/social-media.html?offset={foto11*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req12 = requests.get(url32,headers)
    soup13 = BeautifulSoup(req12.content, 'html.parser')
    for v in soup13.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs11 = v.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs11,'stock-photos/social-media.']
            )
####stock-photos/fireworks.
url13 = 'https://depositphotos.com/stock-photos/fireworks.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
req13 = requests.get(url13,header)
soup14 = BeautifulSoup(req13.content, 'html.parser')
for b in soup14.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg8 = b.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg8,'stock-photos/fireworks.']
        )
for foto12 in range(1, 10):
    url34 = f'https://depositphotos.com/stock-photos/fireworks.html?offset={foto12*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req14 = requests.get(url34,headers)
    soup15 = BeautifulSoup(req14.content, 'html.parser')
    for n in soup15.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs13 = n.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs13,'stock-photos/fireworks.']
            )
####stock-photos/black-friday-and-cyber-monday
url14 = 'https://depositphotos.com/stock-photos/black-friday-and-cyber-monday.html'
header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
req15 = requests.get(url14,header)
soup16 = BeautifulSoup(req15.content, 'html.parser')
for f in soup16.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
    imeg10 = f.find('a').get('href')
    with open("file.csv", 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [imeg10,'stock-photos/black-friday-and-cyber-monday.']
        )
for foto13 in range(1, 11):
    url21 = f'https://depositphotos.com/stock-photos/black-friday-and-cyber-monday.html?offset={foto13*100}'
    # print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req16 = requests.get(url21,headers)
    soup17 = BeautifulSoup(req16.content, 'html.parser')
    for g in soup17.find('div', class_='flex-files flex-files_xwide flex-files_like-grid _slider'):
        imegs12 = g.find('a').get('href')
        with open("file.csv", 'a', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
            [imegs12,'stock-photos/black-friday-and-cyber-monday.']
            )