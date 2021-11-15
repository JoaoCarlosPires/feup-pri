import urllib.request
import json
import os 
import urllib.parse

#not working after the "Astonishing X MEN Torn". Url next to this film doesn't exist

def getReviews(movie_folder_path):

    detailsDirectory = movie_folder_path + "/details.txt"
    file_exists = os.path.exists(detailsDirectory)

    rawFile = open(detailsDirectory, "r")
    jsonObj = json.load(rawFile)
    movieID = jsonObj['id']
    movieTitle=jsonObj['original_title']
    rawFile.close()

    formattedstring= "https://api.themoviedb.org/3/movie/" + str(movieID) + "/reviews?api_key=8dfe13cb077bf9bf0ae14ed0b0b81656"
    

    with urllib.request.urlopen(formattedstring) as url:
        page = json.loads(url.read().decode())
        totalPages= page['total_pages']
                        
        if not os.path.exists(movie_folder_path + "/reviews.txt") and (totalPages==1):
            with open(movie_folder_path + "/reviews.txt","w") as file:
                json.dump(page, file)
                print("reviews created sucessfully")
            
        elif (totalPages>1):
            for i in range(1, totalPages + 1):
                with urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(movieID) + "/reviews?api_key=8dfe13cb077bf9bf0ae14ed0b0b81656&page=" + i) as url:
                    page = json.loads(url.read().decode())
                    with open(movie_folder_path + "/reviews.txt","w") as file:
                        json.dump(page, file)
                        print("reviews created")
        else:
            print(movieTitle + "doesn't have reviews sucessfully")

        
rootdir = "movies"
my_list = os.listdir(rootdir)

for x in my_list:
    getReviews(rootdir+'/' + str(x))


