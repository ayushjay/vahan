"""Experimented with scraping"""
#from .forms import SelectCarForm
import requests
from lxml import html

url = 'https://www.team-bhp.com/forum/luxury-imports-niche/213083-looking-buying-bmw-x1-need-advice.html'



path = '//*[@id="post_message_4655158"]'
response = requests.get(url)
byte_data = response.content
source_code = html.fromstring(byte_data)

tree = source_code.xpath(path) 

print (tree)

print(tree[0].text_content())


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
