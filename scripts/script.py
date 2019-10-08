#!/usr/bin/env python
import pitchfork

artists = []
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

# Store reviews in array
    cnt -= 1
    while(cnt >= 0):
        artist = artists[cnt]
        print(artist)
        while(char < 123):
            try:
                review = pitchfork.search( artist , str(chr(char)))
                if review not in reviews:
                    reviews.append(review)
            except:
                cnt = cnt
            char += 1
        char = 97
        cnt -= 1
    
    print(len(reviews))
    

"""
p1 = pitchfork.search('a', 'a') # the title is autocompleted
p2 = pitchfork.search('a', 'b') # the title is autocompleted
p3 = pitchfork.search('a', 'c') # the title is autocompleted
p4 = pitchfork.search('a', 'd') # the title is autocompleted
p5 = pitchfork.search('b', 'a') # the title is autocompleted
p6 = pitchfork.search('b', 'b') # the title is autocompleted

print(p1.album() + " | " + p1.artist())
print(p2.album() + " | " + p2.artist())
print(p3.album() + " | " + p3.artist())
print(p4.album() + " | " + p4.artist())
print(p5.album() + " | " + p5.artist())
print(p6.album() + " | " + p6.artist())
"""