#Requests is a HTTP library for the Python programming language. The goal of the project is to make HTTP requests simpler and more human-friendly.
import requests
from bs4 import BeautifulSoup


def happyScrape(brand, model):
    if brand == 'BMW' and model == 'X1':
        url = 'https://www.carwale.com/bmw-cars/x1/user-reviews/'
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


    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    cw_result = requests.get(url, headers=headers)

    #cw_soup = BeautifulSoup(cw_result.text, 'html.parser')
    #Beautiful Soup gives us a BeautifulSoup object, which represents the document as a nested data structure from html
    cw_soup = BeautifulSoup(cw_result.text, 'html5lib')

    #print (BeautifulSoup(cw_result.text,'html5lib'))


    scrapeList  =[] 

    #myPosts = cw_soup.find_all('div', class_='o-eZTujG o-eemiLE o-cYdrZi o-fyWCgU undefined')
    scrapeListHtml = cw_soup.find_all('div', {'class': 'o-eZTujG o-eemiLE o-cYdrZi o-fyWCgU undefined'})
    lineBR = "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    for data in scrapeListHtml:
        scrapeList.append(data.text)
        scrapeList.append(lineBR)






    print (scrapeList)



    
    with open(r'./scrape/scrapeListFile.txt', 'w') as f:
        for item in scrapeList:
            # write each item on a new line
            f.write("%s\n" % item)
    

#happyScrape()
        


