from __future__ import print_function
import urllib.request
import json
import os 
import urllib.parse


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def getSafeString(s):
    return urllib.parse.quote_plus(s)


    

def getOmdbMovie(movie_folder_path):

    detailsDirectory = movie_folder_path + "/details.txt"
    file_exists = os.path.exists(detailsDirectory)

    if file_exists == False:
        print("ERROR: File "+detailsDirectory + " doesn't exist")
    
    else:
        rawFile = open(detailsDirectory, "r")
        jsonObj = json.load(rawFile)
        movieTitle = jsonObj['original_title']


        if 'release_date' not in jsonObj:
            print("ERROR: " + movieTitle + " has no release_date available")
        
        
        else:

            movieDate = jsonObj['release_date']
            rawFile.close()

            #keys = df31360f f2fa9863 323c392a 946648df d9437efe d097fef5 1afe7e7f b5479ba2 666383ae cc1b993a

            formattedString = "http://www.omdbapi.com/" + "?apikey=df31360f&t=" + getSafeString(movieTitle) + "&y=" + movieDate[:4] + "&plot=full"


            if not os.path.exists(movie_folder_path + "/omdbContent.txt"):

                with urllib.request.urlopen(formattedString) as url:
                    page = json.loads(url.read().decode())
                    if(page['Response']=="True"):
                        
                        #adicionar num ficheiro novo------------------------------
                        
                        with open(movie_folder_path + "/omdbContent.txt","w") as file:
                            json.dump(page, file)
                            print("SUCCESS - " + movieTitle + " OMDb log was updated")

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
                        print("ERROR: " + movieTitle + " could not be found on OMDb")
            
            #else:
                #print("OMDb file already created")
            

#example 
#getOmdbMovie("Projeto/movies/DespicableMe")

rootdir = "Projeto/movies"
my_list = os.listdir(rootdir)



for i in my_list:
    
    getOmdbMovie(rootdir+'/' + str(i))

