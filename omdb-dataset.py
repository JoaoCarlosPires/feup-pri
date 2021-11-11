from __future__ import print_function
import urllib.request
import json
import os 

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def getOmdbMovie(movie_folder_path):

    #example: getOmdbMovie("Projeto/movies/DespicableMe")

    detailsDirectory = movie_folder_path + "/details.txt"
    file_exists = os.path.exists(detailsDirectory)

    if file_exists == False:
        print("ERROR: File "+detailsDirectory + " doesn't exist")
    
    else:
        rawFile = open(detailsDirectory, "r")
        jsonObj = json.load(rawFile)
        movieTitle = jsonObj['original_title']



        if 'release_date' not in jsonObj:
            print("ERROR: Movie " + movieTitle + " has no release_date available")
        

        elif not is_ascii(movieTitle):
            print("ERROR: the movie title is not ascii, cannot be looked on OMDb")
        
        else:

            movieDate = jsonObj['release_date']
            rawFile.close()

            formattedString = "http://www.omdbapi.com/" + "?apikey=f2fa9863&t=" + movieTitle.replace(" ", "+") + "&y=" + movieDate[:4] + "&plot=full"

            with urllib.request.urlopen(formattedString) as url:
                page = json.loads(url.read().decode())
                if(page['Response']=="True"):
                    #adicionar num ficheiro novo------------------------------
                    
                    with open(movie_folder_path + "/omdbContent.txt","w") as file:
                        json.dump(page, file)
                        print("SUCCESS - Movie " + movieTitle + " OMDb log was updated")

                    # -----------------------------------------


                    #se for para adicionar no mesmo ficheiro------------------------------

                    #f = open(detailsDirectory, 'r+')
                    #text = f.read()
                    #text = '['+text+','+json.dumps(page)+']'
                
                    #f.seek(0)
                    #f.write(text)
                    #f.truncate()
                    #f.close()

                    # -----------------------------------------
                else:
                    print("ERROR: Movie " + movieTitle + " could not be found on OMDb")


            
            

#getOmdbMovie("Projeto/movies/DespicableMe")

rootdir = "Projeto/movies"

my_list = os.listdir(rootdir)

for i in my_list:
    
    getOmdbMovie(rootdir+'/' + str(i))