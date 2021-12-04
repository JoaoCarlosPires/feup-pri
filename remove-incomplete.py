import os
import shutil

rootdir = os.getcwd() + '/movies'

counter = 0

for subdir, dirs, files in os.walk(rootdir):
    if(files != ['details.txt', 'omdbContent.txt'] and subdir!=rootdir):
        try:
            shutil.rmtree(subdir)
            print("REMOVING - " + subdir)
            counter = counter+1

        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    
    
    #else:
        #print("NOT REMOVE - " + subdir)

print('\n' + str(counter) + " movies removed")


