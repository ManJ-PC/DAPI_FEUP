#!/usr/bin/env python
import pitchfork
import json
import csv
from progressbar import ProgressBar

artists = []
storedAlbums = []
reviews = []

p1 = pitchfork.search('a', '') # the title is autocompleted

char = 97 # ASCII for 'a'

# Python code to remove duplicate elements 
def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

# Open artists file
filepath = 'artists.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 0

# Store artists in array
    while line:
        artists.append(line.strip())
        line = fp.readline()
        cnt += 1

    numberArtists = cnt

# Store reviews in array
    cnt -= 1
    aux = 0
    while(cnt >= 0):
        artist = artists[cnt]
        aux += 1
        print("Parsing artist " + artist + " (" + str(aux) + "/" + str(numberArtists) + ")")
        while(char < 123):
            try:
                tempReview = pitchfork.search( artist , str(chr(char)))
                album = str(tempReview.album())
                artist = str(tempReview.artist())
                score = str(tempReview.score())
                year = str(tempReview.year())
                abstract = str(tempReview.abstract())
                editorial = str(tempReview.editorial())
                label = str(tempReview.label())
                
                review = [album, artist, year, score, abstract, editorial, label]

                if album not in storedAlbums:
                    storedAlbums.append(album)
                    reviews.append(review)
            except:
                cnt = cnt
            char += 1
        char = 97
        cnt -= 1

# Write reviews to csv file

    with open('data.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(reviews)
        csvFile.close()
    print(len(reviews))
