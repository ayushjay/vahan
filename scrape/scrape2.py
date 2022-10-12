"""Experimented with scraping team-bhp"""
#from .forms import SelectCarForm
import requests
#The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt
#html5lib is a pure-python library for parsing HTML
from lxml import html
import time


def happyScrape2(brand,model):
    time.sleep(1)
    
    if brand == 'BMW' and model == 'X1':
        url = 'https://www.team-bhp.com/forum/luxury-imports-niche/213083-looking-buying-bmw-x1-need-advice.html'

    elif brand == 'BMW' and model == 'X3':
        url = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/247865-review-2022-bmw-x3-lci.html'
    elif brand == 'BMW' and model == 'X5':
        url = 'https://www.team-bhp.com/forum/indian-car-scene/202166-4th-gen-bmw-x5-now-launched.html'
    elif brand == 'BMW' and model == 'X7':
        url = 'https://www.team-bhp.com/forum/indian-car-scene/211463-bmw-x7-launched-rs-98-90-lakh.html'
    elif brand == 'BMW' and model == '3S':
        url = 'https://www.team-bhp.com/forum/official-new-car-reviews/228796-review-bmw-330i-g20.html'
    elif brand == 'BMW' and model == '5S':
        url = 'https://www.team-bhp.com/forum/luxury-imports-niche/238922-advice-buying-bmw-5-series-lci.html'
    elif brand == 'BMW' and model ==' 7S':
        url = 'https://www.team-bhp.com/forum/indian-car-scene/211465-bmw-7-series-facelift-launched-rs-1-22-crore.html'
    
    elif brand == 'MR' and model == 'EC':
        url = 'https://www.team-bhp.com/forum/official-new-car-reviews/185529-driven-2017-mercedes-e-class.html'
    elif brand == 'AU' and model == 'A4':
        url = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/248015-2022-audi-a4-premium-review-case-base-spec.html'
    elif brand == 'AU' and model == 'A8':
        url = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/224958-driven-audi-a8l-review-3-0-v6-turbo-petrol.html'
    elif brand == 'AU' and model == 'A3':
        url = 'https://www.team-bhp.com/forum/official-new-car-reviews/154206-audi-a3-official-review.html'
    elif brand == 'AU' and model == 'A6':
        url = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/243367-my-audi-a6-45-tfsi-ownership-review.html'
    elif brand == 'AU' and model == 'Q2':
        url = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/229489-driven-audi-q2-unveiling-review.html'
    elif brand == 'AU' and model == 'Q5':
        url = 'https://www.team-bhp.com/forum/official-new-car-reviews/243690-2021-audi-q5-facelift-review.html'
    elif brand == 'AU' and model == ' Q7':
        url = 'https://www.team-bhp.com/forum/test-drives-initial-ownership-reports/58174-my-first-exotic-suv-audi-q7.html'
    else:
        url = ''


    
    path = '//*[starts-with(@id,"post_message_")]'
    source_code = html.fromstring(requests.get(url).content)

    scrapeList2 = []

    #lineBR = "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    for e in source_code.xpath(path):
        #print(e.text_content())
        scrapeList2.append(e.text_content())
        #scrapeList2.append(lineBR)
    
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
