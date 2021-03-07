from nltk.corpus import wordnet
import nltk
import random
from nltk.stem import PorterStemmer
Stemmer = PorterStemmer()

synonyms = []
antonyms = []


def DeUnderscore(word):
    chars = []
    for i in word:
        if i == "_":
            chars.append(" ")
        else:
            chars.append(i)
    r = ""
    for i in chars:
        r = r + i
    return r

def GenerateSentence(sentenceType,about):
    w1 = []
    w2 = []
    word = ""
    word2 = None
    
    if sentenceType.lower() == "compliment":
        word = "nice"
        if random.randint(1,2) == 2:
            word2 = None
        else:
            word2 = "pretty"

    if sentenceType.lower() == "insult":
        word = "bad"
        if random.randint(1,2) == 2:
            word2 = None
        else:
            word2 = "very"
    
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            w1.append(l.name())

    if word2 != None:
        for syn in wordnet.synsets(word2):
            for l in syn.lemmas():
                w2.append(l.name()+" ")
    else:
        w2 = ["","",""]
    return "You "+about+" "+w2[random.randint(0,len(set(w2))-1)] + w1[random.randint(0,len(set(w1))-1)]

##print(DeUnderscore("Hello_there"))
##print(GenerateSentence("compliment","look"))
##print(GenerateSentence("compliment","look"))
##print(GenerateSentence("insult","look"))
##print(GenerateSentence("insult","look"))


def GenerateQuestion(sentence):
    #Sauce was originally invented in France
    #Where was sauce originally invented?
    
    
    qType = ""
    activated=False
    listOfMonths = "january, february, march, april, may, june, july, august, september, october, november, december,"
    #There are 7 days in a week
    words = nltk.word_tokenize(sentence)
    
    
    if words[0].lower() in ["there","i","they"]:
        
        if words[1].lower() in ["are","is","be","am","were","was"]:
            if words[2][0].lower() in "1234567890":
                qType = "many"

                newSentence = "How "+qType+" "+words[3].lower()+" "+words[1].lower()+' '+words[0].lower()
                words.remove(words[0])
                words.remove(words[0])
                words.remove(words[0])
                words.remove(words[0])
                for i in words:
                    newSentence = newSentence + " "+i.lower()

                return newSentence
                #print("hummiah hummiah")
                activated = True
            else:
                if words[3][0].lower() in "1234567890":
                    qType = "many"
                    print(words)
                    newSentence = "How "+qType+" "+words[4].lower()+" "+words[1].lower()+' '+words[0].lower()
                    words.remove(words[0])
                    words.remove(words[0])
                    words.remove(words[0])
                    words.remove(words[1])
                    words.remove(words[0])
                    print(words)
                    for i in words:
                        newSentence = newSentence + " "+i.lower()

                    return newSentence
                    #print("hummiah hummiah")
                    activated = True
    
    elif words[len(words)-1].lower() in listOfMonths or words[len(words)-2].lower() in listOfMonths or words[len(words)-3].lower() in listOfMonths:
        qType = "when"
        

        newSentence = "When is my birthday"
        for j in words:
            if j in ["on"]:
                for e in words:
                    if e.lower() =="was":
                        newSentence = "When "+"was "
                        words.remove("was")
                    elif e.lower() =="is":
                        newSentence = "When "+"is "
                        words.remove("is")
                for i in words:
                    if words.index(i) < words.index(j):
                        newSentence = newSentence + i.lower()+" "
                return newSentence
                activated = True

    #Sauce was originally invented in France
    #Where was sauce originally invented?
    elif "in" in words:
        inIndex = 0
        vIndex = 0
        for i in words:
            if i.lower() == "in":
                inIndex = words.index(i)
        for i in words:
            if i.lower() in ["was","were","is","are"]:
                vIndex = words.index(i)
        newSentence = "Where " +words[vIndex]+" "
        for i in words:
            if i not in ["was","were","is","are"] and words.index(i) < inIndex:
                newSentence = newSentence + i.lower()+" "
        
        words.remove(words[vIndex])
        return newSentence
        
print(GenerateQuestion("there are like 12389 gigabytes of data in my computer"))



##for syn in wordnet.synsets("goodbye"):
##    for l in syn.lemmas():
##        synonyms.append(DeUnderscore(l.name()))
##print(synonyms)

##    if words[len(words)-1].lower() in listOfMonths or words[len(words)-2].lower() in listOfMonths or words[len(words)-3].lower() in listOfMonths:
##        qType = "when"
##
##        newSentence = "When is my birthday"
##        for j in words:
##            if j in ["on"]:#["is","am","are","was","were"]:
##                newSentence = "When "+j+" "
##                for i in words:
##                    if words.index(i) < words.index(j):
##                        newSentence = newSentence + i.lower()+" "
##
##                return newSentence
                
                
        
print(GenerateQuestion("There are 7 days in a week"))
#print(GenerateQuestion("My birthday is on the 4th of july, 2020"))
#print(GenerateQuestion("The american declaration of independence was signed on the July, 4th, 1776"))
