"""Experimented with scraping team-bhp"""
#from .forms import SelectCarForm
import requests
from lxml import html
import time


def happyScrape2(brand,model):
    time.sleep(1)
    
    if brand == 'BMW' and model == 'X1':
        url = 'https://www.team-bhp.com/forum/luxury-imports-niche/213083-looking-buying-bmw-x1-need-advice.html'

    elif brand == 'BMW' and model == 'X3':
        url = 'https://www.carwale.com/bmw-cars/x3-2018-2022/user-reviews/'
    elif brand == 'BMW' and model == 'X5':
        url = 'https://www.carwale.com/bmw-cars/x5/user-reviews/'
    elif brand == 'BMW' and model == 'X7':
        url = 'https://www.carwale.com/bmw-cars/x7/user-reviews/'
    elif brand == 'BMW' and model == '3S':
        url = 'https://www.carwale.com/bmw-cars/3-series/user-reviews/'
    elif brand == 'BMW' and model == '5S':
        url = 'https://www.carwale.com/bmw-cars/5-series-2017-2021/user-reviews/'
    elif brand == 'BMW' and model ==' 7S':
        url = 'https://www.carwale.com/bmw-cars/7-series/user-reviews/'
    elif brand == 'HN' and model == 'AM':
        url = 'https://www.carwale.com/honda-cars/amaze/user-reviews/'
    elif brand == 'MR' and model == 'EC':
        url = 'https://www.carwale.com/mercedes-benz-cars/e-class/user-reviews/'
    elif brand == 'AU' and model == 'A4':
        url = 'https://www.carwale.com/audi-cars/a4/user-reviews/'
    elif brand == 'AU' and model == 'A8':
        url = 'https://www.carwale.com/audi-cars/a8-l-2018-2022/user-reviews/'
    elif brand == 'AU' and model == 'A3':
        url = 'https://www.carwale.com/audi-cars/a3/user-reviews/'
    elif brand == 'AU' and model == 'A6':
        url = 'https://www.carwale.com/audi-cars/a6/user-reviews/'
    elif brand == 'AU' and model == 'Q2':
        url = 'https://www.carwale.com/audi-cars/q2/user-reviews/'
    elif brand == 'AU' and model == 'Q5':
        url = 'https://www.carwale.com/audi-cars/q5-2018-2020/user-reviews/'
    elif brand == 'AU' and model == ' Q7':
        url = 'https://www.carwale.com/audi-cars/q7-2015-2020/user-reviews/'
    else:
        url = ''


    
    path = '//*[starts-with(@id,"post_message_")]'
    source_code = html.fromstring(requests.get(url).content)

    scrapeList2 = []


    for e in source_code.xpath(path):
        #print(e.text_content())
        scrapeList2.append(e.text_content())
    
    with open(r'./scrape/scrapeListFile.txt', 'a') as f:
        for item in scrapeList2:
            # write each item on a new line
            f.write("%s\n" % item)




"""
path = '///*[@id="post_message_4657893"]'
response = requests.get(url)
byte_data = response.content
source_code = html.fromstring(byte_data)

tree = source_code.xpath(path) 

print (tree)

print(tree[0].text_content())

"""
"""
page = requests.get(url)
reviews = html.fromstring(page.content) 

int = []
for i in range(30):
    int.append(i)
reviewsList = reviews.xpath('//*[@id="post_message_4655158"]')
                            
print(reviewsList) 
"""

#for k,v in SelectCarForm:

#def hello():
#    print ("hello")
