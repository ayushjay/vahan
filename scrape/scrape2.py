#from .forms import SelectCarForm
import requests
from lxml import html

url = 'https://www.carwale.com/bmw-cars/x1/'
path = '//*[@id="root"]/div[3]/div[2]/div[4]/div[1]/div[1]/div[13]/div/div[2]/section/div/div[1]/ul/li[1]/div/div[1]/div[3]/div[1]/div/div[1]/text()'
paxh = '//*[@id="root"]/div[3]/div[2]/div[4]/div[1]/div[1]/div[13]/div/div[2]/section/div/div[1]/ul/li[2]/div/div[1]/div[3]/div[1]/div/div[1]/text()'




response = requests.get(url)
byte_data = response.content
source_code = html.fromstring(byte_data)

tree = source_code.xpath(path) 

print (tree)
#print (len(tree))
print(tree[0].text_content())



