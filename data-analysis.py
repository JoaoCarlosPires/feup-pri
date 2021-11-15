import os
import sys
import shutil
import json
from collections import Counter
import itertools
import re


import numpy as np
import matplotlib.pyplot as plt

def getTmdbPlotAverage():

    rootdir = "movies"

    counter = 1

    tmdbPlotCounter = 0
    
    movieCounter = 0

    
    for subdir, dirs, files in os.walk(rootdir):
        if(files == ['details.txt', 'omdbContent.txt']):
        
            f = open(subdir + '/'+files[0], 'r')
            data=f.read()
            obj = json.loads(data)
            tmdbPlotCounter = tmdbPlotCounter + len(obj['overview'].split())
            movieCounter = movieCounter + 1
            f.close()

    return tmdbPlotCounter/movieCounter

def getOmdbPlotAverage():

    rootdir = "movies"

    
    omdbPlotCounter = 0
    movieCounter = 0

    
    for subdir, dirs, files in os.walk(rootdir):
        if(files == ['details.txt', 'omdbContent.txt']):
        
            f = open(subdir + '/'+files[1], 'r')
            data=f.read()
            obj = json.loads(data)
            omdbPlotCounter = omdbPlotCounter + len(obj['Plot'].split())
            movieCounter = movieCounter + 1
            f.close()

    return omdbPlotCounter/movieCounter


def moviesPerLanguage():

    
    

    languages = []

    rootdir = "movies"
    for subdir, dirs, files in os.walk(rootdir):
        if(files == ['details.txt', 'omdbContent.txt']):
            f = open(subdir + '/'+files[1], 'r')
            data=f.read()
            obj = json.loads(data)
            for i in obj['Language'].split(', '):
                languages.append(i)
                
    word_counts = dict(Counter(languages))

    return dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    


def plotMoviesPerLanguage():
    data_dict = (moviesPerLanguage())
    del data_dict["N/A"]
    data_dict = dict(itertools.islice(data_dict.items(), 10))


    courses = list(data_dict.keys())
    values = list(data_dict.values())
    fig = plt.figure(figsize = (10, 5))
    #  Bar plot
    plt.yticks(np.arange(0, max(values)+1, 500.0))
    
    plt.bar(courses, values, color ='green',
            width = 0.5)

    bars = plt.bar(courses, height=values, width=.5)

    # access the bar attributes to place the text in the appropriate location
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .005, yval)

    plt.xlabel("Languages")
    plt.ylabel("Number of movies")
    plt.title("Top 10 languages in our movie dataset")
    plt.show()

def mostCommonPlotWords():
    rootdir = "movies"

    #number of words to show
    number_of_words_to_display = 200

    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    
    words = []

    
    for subdir, dirs, files in os.walk(rootdir):
        if(files == ['details.txt', 'omdbContent.txt']):
        
            f = open(subdir + '/'+files[1], 'r')
            data=f.read()
            obj = json.loads(data)
            for i in obj['Plot'].split():
                i = re.sub(r'[^\w\s]','',i)
                i = i.lower()
                if i not in stopwords:
                    
                    words.append(i)
            f.close()

    for subdir, dirs, files in os.walk(rootdir):
        if(files == ['details.txt', 'omdbContent.txt']):
        
            f = open(subdir + '/'+files[0], 'r')
            data=f.read()
            obj = json.loads(data)
            for i in obj['overview'].split():
                
                i = re.sub(r'[^\w\s]','',i)
                i = i.lower()
                if i not in stopwords:
                    
                    words.append(i)
                
            f.close()

    
    
    word_counts = dict(Counter(words))

    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

    



    return dict(itertools.islice(word_counts.items(), number_of_words_to_display))

print(mostCommonPlotWords())