from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
# function to print sentiments
# of the sentence.
def getSentiment4():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()
        # Create a SentimentIntensityAnalyzer object.
        myObj = SentimentIntensityAnalyzer()
    
        
        myDict = myObj.polarity_scores(content)
        
        
        print("Overall sentiment dictionary is : ", myDict)
        print("sentence was rated as ", myDict['neg']*100, "% Negative")
        print("sentence was rated as ", myDict['neu']*100, "% Neutral")
        print("sentence was rated as ", myDict['pos']*100, "% Positive")
        score = 50*myDict['neu'] + 100*myDict['pos']
        print("Overall score is: " + str(score))
    
        print("Sentence Overall Rated As", end = " ")
    
        # decide sentiment as positive, negative and neutral
        if myDict['compound'] >= 0.05 :
            print("Positive")
    
        elif myDict['compound'] <= - 0.05 :
            print("Negative")
    
        else :
            print("Neutral")

print(getSentiment4())
    