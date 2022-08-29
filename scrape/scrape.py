import requests
from bs4 import BeautifulSoup


def happyScrape():


    url = 'https://www.carwale.com/honda-cars/amaze/user-reviews/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    cw_result = requests.get(url, headers=headers)

    #cw_soup = BeautifulSoup(cw_result.text, 'html.parser')
    cw_soup = BeautifulSoup(cw_result.text, 'html5lib')

    #print (BeautifulSoup(cw_result.text,'html5lib'))


    scrapeList  =[] 

    #myPosts = cw_soup.find_all('div', class_='o-eZTujG o-eemiLE o-cYdrZi o-fyWCgU undefined')
    scrapeListHtml = cw_soup.find_all('div', {'class': 'o-eZTujG o-eemiLE o-cYdrZi o-fyWCgU undefined'})

    for data in scrapeListHtml:
        scrapeList.append(data.text)






    print (scrapeList)



    
    with open(r'./scrape/scrapeListFile.txt', 'w') as f:
        for item in scrapeList:
            # write each item on a new line
            f.write("%s\n" % item)


#happyScrape()
        


