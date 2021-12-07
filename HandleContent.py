import json
import os
from typing_extensions import final

finalData = []
data = {}


class doubleQuoteDict(dict):
    def __str__(self):
        return json.dumps(self)

    def __repr__(self):
        return json.dumps(self)


def getMovieContent(folder):

    moviefoldername = folder.replace("Projeto/movies/", "")
   
    data["id"] = str(moviefoldername)

    omdb_txt = ["Title", "Rated", "Release", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot", "Language", "Country", "Awards", "Poster", "Metascore", "imdbRating", "imdbVotes", "DVD", "BoxOffice", "Production", "Website"]
    tmdb_txt = ["overview", "popularity", "poster_path", "video", "vote_average", "vote_count"]


    
    if(os.path.isfile(folder+"/omdbContent.txt")):
        with open(folder+"/omdbContent.txt", 'r') as handle:
                parsed = json.load(handle)
                for attr in omdb_txt:
                    if attr in parsed:
                        data[(attr)] = (parsed[attr])
                    else:
                        data[(attr)] = "N/A"
        handle.close()

                
    else:
        #print(folder+"/omdbContent.txt doesn't exist")
        return {}


    if(os.path.isfile(folder+"/details.txt")):
        with open(folder+"/details.txt", 'r') as handle:
                parsed = json.load(handle)
                for attr in tmdb_txt:
                    if attr in parsed:
                        data[(attr.title())] = (parsed[attr])
                    else:
                        data[(attr.title())] = "N/A"
        handle.close()





    else:
        #print(folder+"/details.txt doesn't exist")
        return {}

    if(os.path.isfile(folder+"/reviews.txt")):
        with open(folder+"/reviews.txt", 'r') as handle:
                

            lines = handle.readline()
            lines = lines.split("\\r\\n\\r\\n")
            
            data["Reviews"] = (lines)


            
        handle.close()
    else:
        data["Reviews"] = "N/A"



    


    if data["Overview"] == data["Plot"]:
        del data["Overview"]


    formattedData = doubleQuoteDict(data)
    
    return formattedData

    
    
    

rootdir = 'Projeto/movies'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        auxDict = getMovieContent(d)
        finalData.append(auxDict)
        
            
        
        

#print(finalData)
#dd = (getMovieContent("movies/MonstersInc"))
#print(dd)
with open('Projeto/data.json', 'w') as fp:
    fp.write(str(finalData))


