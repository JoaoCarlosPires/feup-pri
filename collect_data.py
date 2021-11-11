# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:24:50 2021

@author: joaocarlosmrp
"""

from __future__ import print_function
import urllib.request
import json
import os 

# Get first page
with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key=8dfe13cb077bf9bf0ae14ed0b0b81656&with_genres=16") as url:
    first_page = json.loads(url.read().decode())
    number_pages = first_page['total_pages'];

# Create directory to save TMDB data
directory = "movies"
curr_dir = os.getcwd()
complete_path = os.path.join(curr_dir, directory)
exists = os.path.exists(complete_path)
if not exists:
    os.mkdir(complete_path)

print('Saving movie data from TMDB...')

# Save all pages
for i in range (1, number_pages + 1): 
    with urllib.request.urlopen("https://api.themoviedb.org/3/discover/movie?api_key=8dfe13cb077bf9bf0ae14ed0b0b81656&with_genres=16&page=" + str(i)) as url:
        content = json.loads(url.read().decode())
        movies = content['results']
        for movie in movies:
            title = movie['original_title'] # or title = movie['title']
            if 'release_date' in movie:
                release_date = movie['release_date']
            movie_folder_path = os.path.join(complete_path, ''.join(e for e in title if e.isalnum()))
            exists = os.path.exists(movie_folder_path)
            if not exists:
                os.mkdir(movie_folder_path)
            with open(movie_folder_path + "/details.txt","w") as file:
                json.dump(movie, file)
                
            # ToDo: search for data in other APIs using the title and release_date
            # ToDo: save then the results in a new folder and in new files (c.f. above) 

