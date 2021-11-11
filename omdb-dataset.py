from __future__ import print_function
import urllib.request
import json
import os 

def getOmdbMovie(movie_folder_path):
    
    #example: getOmdbMovie("Projeto/movies/DespicableMe")

    detailsDirectory = movie_folder_path + "/details.txt"

    rawFile = open(detailsDirectory, "r")
    jsonObj = json.load(rawFile)
    movieTitle = jsonObj['original_title']
    movieDate = jsonObj['release_date']
    rawFile.close()

    formattedString = "http://www.omdbapi.com/" + "?apikey=f2fa9863&t=" + movieTitle.replace(" ", "+") + "&y=" + movieDate[:4] + "&plot=full"

    with urllib.request.urlopen(formattedString) as url:
        page = json.loads(url.read().decode())
        
        #se for para adicionar no mesmo ficheiro------------------------------

        #f = open(detailsDirectory, 'r+')
        #text = f.read()
        #text = '['+text+','+json.dumps(page)+']'
        
        #f.seek(0)
        #f.write(text)
        #f.truncate()
        #f.close()

        # -----------------------------------------


        #adicionar num ficheiro novo------------------------------
        with open(movie_folder_path + "/omdbContent.txt","w") as file:
            json.dump(page, file)

        # -----------------------------------------
        



