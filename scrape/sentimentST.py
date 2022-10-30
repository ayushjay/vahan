#does sentiment analysis using spacyTextblob, producing same results as Textblob
#spacytextblob is a pipeline component that enables sentiment analysis using the TextBlob
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob



def getSentiment2():
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')   
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()
        senAnalysis = nlp(content)
        polarity = round(senAnalysis._.blob.polarity * 5 + 5,2)
        subjectivity = senAnalysis._.blob.subjectivity
        if subjectivity <= 0.25:
            subjectivity = 'is not opinion-based'
        elif subjectivity <= 0.5:
            subjectivity = 'is somewhat opnion-based'
        elif subjectivity <= 0.75:
            subjectivity = 'is opinion-based'
        elif subjectivity <= 1:
            subjectivity = 'is highly opnion-based'   

        return polarity, subjectivity

print(getSentiment2())