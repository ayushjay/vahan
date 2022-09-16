from webbrowser import get
from textblob import TextBlob


def getSentiment():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()
        analysis = TextBlob(content)
        #for line in f.read().split('\n'):
        #    analysis = TextBlob(line)

        #print (analysis.sentiment.polarity)
        return round(analysis.sentiment.polarity * 5 + 5,2)

#print (analysis.sentiment)


print(getSentiment())
