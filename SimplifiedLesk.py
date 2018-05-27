# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 00:16:50 2018

@author: Apurva
"""

from nltk.corpus import wordnet
from nltk.corpus import stopwords

def simplifiedLESK(word, sentence, removeStopWords):
    senses=wordnet.synsets(word)
    best_sense=senses[0]
    max_overlap=0
    context=[]
    context=sentence.split()
    overlap_dict={}
    if(removeStopWords == 'y' or removeStopWords == 'Y'):
        context=deleteStopWords(context)
    for sense in senses:
        gloss = sense.definition().split()
        signature = gloss
        examples=sense.examples()
        for example in examples:
            signature+=example.split()
            if(removeStopWords == 'y' or removeStopWords == 'Y'):
                signature=deleteStopWords(signature)
        overlap_count,overlap_words=computeOverlap(signature,context)
        overlap_dict[sense]=(overlap_count,overlap_words)
        if overlap_count>max_overlap:
            max_overlap=overlap_count
            best_sense=sense
    return (best_sense,max_overlap,overlap_dict)

def deleteStopWords(wordList):
    
    stopWords=stopwords.words('english')
    return [word for word in wordList if word not in stopWords]

def computeOverlap(signature,context):
    overlap_count=0
    overlap_words=[]
    for word in context:
        word_count=signature.count(word)
        if(word_count>0):
            overlap_count+=1
            overlap_words.append(word)
            
    return (overlap_count,overlap_words)


def main():
    
    word="bank" 
    sentence="The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities"
    removeStopWords = 'n'
    print("Do you want to remove stop words (y/n)")
    removeStopWords = input()
    best_sense,max_overlap,overlap_dict=simplifiedLESK(word, sentence, removeStopWords)
    
    print("***************************Word Overlap for each sense of the word bank in WordNet:********************************** \n")
    for sense in overlap_dict:
        print ("Sense Name\t: ",sense.name())
        print ("Gloss\t\t: ",sense.definition())
        print ("Overlap Count\t: ",overlap_dict[sense][0])
        print ("Overlap Words\t: ",overlap_dict[sense][1])
        print ("\n")

    print ("\n=================================================================================================================\n")
    print("********************************* Final chosen sense:*****************************************************************\n ")
    print ("Best Sense Name\t: ",best_sense.name())
    print ("Best Sense Gloss\t\t: ",best_sense.definition())
    print ("Best Sense Overlap Count\t: ",overlap_dict[best_sense][0])
    print ("Best Sense Overlap Words\t: ",overlap_dict[best_sense][1])
    print ("\n==================================================================================================================\n")

if __name__ == '__main__':
    main()