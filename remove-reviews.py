import os 

def removeReviews(movie_folder_path):
    exists = os.path.exists(movie_folder_path + "/reviews.txt")
    if exists:
        os.remove(movie_folder_path + "/reviews.txt")
        
rootdir = os.getcwd() + "/movies"
my_list = os.listdir(rootdir)

for x in my_list:
    removeReviews(rootdir+'/' + str(x))


