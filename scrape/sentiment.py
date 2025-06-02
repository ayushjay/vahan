from textblob import TextBlob
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS



def getSentiment():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()
        # use LIST COMREHESION
        words = [word for word in content.split() if word.lower() not in ENGLISH_STOP_WORDS]
        new_text = " ".join(words)
        print(new_text)
        print("Old length: ", len(content))
        print("New length: ", len(new_text))


        
        analysis = TextBlob(new_text)
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
