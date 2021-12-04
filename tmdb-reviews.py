import urllib.request
import json
import os 
import urllib.parse

movies_whithout_reviews = 0
movies_whith_reviews = 0
num_reviews = 0

def getReviews(movie_folder_path):

    detailsDirectory = movie_folder_path + "/details.txt"
    file_exists = os.path.exists(detailsDirectory)
    
    if not file_exists:
        print("ERROR - Movie not found")
    else: 
        rawFile = open(detailsDirectory, "r")
        jsonObj = json.load(rawFile)
        movieID = jsonObj['id']
        movieTitle = jsonObj['original_title']
        rawFile.close()
    
        formattedstring= "https://api.themoviedb.org/3/movie/" + str(movieID) + "/reviews?api_key=8dfe13cb077bf9bf0ae14ed0b0b81656"
        
        try:
            with urllib.request.urlopen(formattedstring) as url:
                page = json.loads(url.read().decode())
                totalPages=page['total_pages']
                
                if totalPages == 0:
                    global movies_whithout_reviews
                    movies_whithout_reviews+=1
                else:
                    global movies_whith_reviews
                    movies_whith_reviews += 1
                    if not os.path.exists(movie_folder_path + "/reviews.txt"):
                        for i in range(1, totalPages + 1):
                            with urllib.request.urlopen(formattedstring + "&page=" + str(i)) as url:
                                content = json.loads(url.read().decode())
                                results = content['results']
                                with open(movie_folder_path + "/reviews.txt","a") as file:
                                    for result in results: 
                                        json.dump(result['content'], file)
                                        json.dump("\n", file)
                                        global num_reviews
                                        num_reviews += 1
        except urllib.error.HTTPError as e: print("ERROR - " + movieTitle); ResponseData = ''
        
rootdir = os.getcwd() + "/movies"
my_list = os.listdir(rootdir)

for x in my_list:
    getReviews(rootdir+'/' + str(x))
    
print("Number of movies without reviews: " + str(movies_whithout_reviews))
print("Number of movies with reviews: " + str(movies_whith_reviews))
print("Number of reviews: " + str(num_reviews))


