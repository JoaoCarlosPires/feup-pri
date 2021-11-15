import os
import json
from collections import Counter
import itertools
import re

import numpy as np
import matplotlib.pyplot as plt

def getTmdbPlotAverage():

    rootdir = os.getcwd() + "/movies"

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

    rootdir = os.getcwd() + "/movies"

    
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

    rootdir = os.getcwd() + "/movies"
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
    rootdir = os.getcwd() + "/movies"

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

def plotMostCommonPlotWords():
    data_dict = mostCommonPlotWords()
    data_dict = dict(itertools.islice(data_dict.items(), 30))


    courses = list(data_dict.keys())
    values = list(data_dict.values())
    fig = plt.figure(figsize = (29, 7))
    #  Bar plot
    plt.yticks(np.arange(0, max(values)+1, 500.0))
    
    plt.bar(courses, values, color ='green',
            width = 0.5)

    bars = plt.bar(courses, height=values, width=.5)

    # access the bar attributes to place the text in the appropriate location
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .005, yval)

    plt.xlabel("Words")
    plt.ylabel("Occurrences")
    plt.xticks(fontsize=7)
    plt.title("Most used words in movie plots")
   
    plt.show()


def getAverageRuntime():
    rootdir = os.getcwd() + "/movies"

    
    addition = 0
    movieCounter = 0

    
    for subdir, dirs, files in os.walk(rootdir):
        if(files == ['details.txt', 'omdbContent.txt']):
        
            f = open(subdir + '/'+files[1], 'r')
            data=f.read()
            obj = json.loads(data)
            minute = (obj['Runtime'].split()[0])
            if minute.isnumeric():
                addition = addition + int((obj['Runtime'].split()[0]))
                movieCounter = movieCounter + 1
            
            f.close()

    return addition/movieCounter

def getAvgDecade():


    rootdir = os.getcwd() + "/movies"
    list=[]

    for subdir, dirs, files in os.walk(rootdir):
        if(files == ['details.txt', 'omdbContent.txt']):
        
            f = open(subdir + '/'+files[1], 'r')
            data=f.read()
            obj = json.loads(data)
            
            decade = obj["Released"][-4:]
            if decade.isnumeric():
                decade = int(decade)
                decade = (decade//10) * 10
                list.append(decade)
    decade_counter = dict(Counter(list))

    decade_counter = dict(sorted(decade_counter.items(), key=lambda item: item[1], reverse=True))

    return decade_counter

def plotAvgDecade():
    decade_counter = getAvgDecade()

    courses = list(decade_counter.keys())
    values = list(decade_counter.values())
    fig = plt.figure(figsize = (10, 5))
    #  Bar plot
    plt.yticks(np.arange(0, max(values)+1, 500.0))
    
    
    plt.bar(courses, values, color ='green',
            width = 0.5)

    bars = plt.bar(courses, height=values, width=.5)
    

    # access the bar attributes to place the text in the appropriate location
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .5, yval)

    plt.xlabel("Decades")
    plt.ylabel("Number of movies")
    plt.title("Number of movies per decade")
    plt.show()

plotMostCommonPlotWords()