from webbrowser import get
from textblob import TextBlob


def getSentiment():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()
        analysis = TextBlob(content)
        #for line in f.read().split('\n'):
        #    analysis = TextBlob(line)

        #print (analysis.sentiment.polarity)
        polarity = round(analysis.sentiment.polarity * 5 + 5,2)
        subjectivity = analysis.sentiment.subjectivity

        if subjectivity <= 0.25:
            subjectivity = 'is not opinion-based'
        elif subjectivity <= 0.5:
            subjectivity = 'is somewhat opnion-based'
        elif subjectivity <= 0.75:
            subjectivity = 'is opinion-based'
        elif subjectivity <= 1:
            subjectivity = 'is highly opnion-based'            

        return polarity, subjectivity

#print (analysis.sentiment)


print(getSentiment())
