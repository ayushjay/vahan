"""Experimented with scraping"""
#from .forms import SelectCarForm
import requests
from lxml import html

url = 'https://www.cardekho.com/user-reviews/bmw-x1'


"""
path = '//*[@id="rf01"]/div[1]/div/div[1]/main/div/div[1]/div[2]/section/div/div[2]/ul/li[4]/div/div/div[2]/p/span/text()'
response = requests.get(url)
byte_data = response.content
source_code = html.fromstring(byte_data)

tree = source_code.xpath(path) 

print (tree)
#print (len(tree))
print(tree[0].text_content())
"""


page = requests.get(url)
reviews = html.fromstring(page.content) 
int = []
for i in range(30):
    int.append(i)

reviewsList = reviews.xpath('//*[@id="rf01"]/div[1]/div/div[1]/main/div/div[1]/div[2]/section/div/div[2]/ul/li[4]/div/div/div[2]/p/span/text()')
                            
print(reviewsList) 


#for k,v in SelectCarForm:

#def hello():
#    print ("hello")
