"""

you can simple put the following code if you want to use '_' easily.
name.replace(" ", "_")

What it does is, it replaces all the space with _.
so it will be eligible to search easily on wikipedia.

"""
import urllib.request
import re
import webbrowser

name = input("Enter charcter name: ")

try:
    
    index_of_second_word = name.index(' ') + 1


    setting1 = name[0].upper()

    under = '_'
    setting2 = name[index_of_second_word].upper()

    character = setting1 + name[1:index_of_second_word - 1] + under + setting2 + name[index_of_second_word + 1:]

    print(character)
    url = 'https://en.wikipedia.org/wiki/' + str(character)
    webbrowser.open(url)
except ValueError:
    webbrowser.open('https://en.wikipedia.org/wiki/' + str(name))
#for twitter================================================



try:
    
    a_twitter = name.index(' ')
    b_twitter = a_twitter + 1

    for_twitter = name[0:a_twitter] + name[b_twitter: ]

    facebook = 'https://www.facebook.com/' + str(for_twitter)

    twitter = 'https://twitter.com/' + str(for_twitter)
    webbrowser.open(facebook)
    webbrowser.open(twitter)
except ValueError:
    webbrowser.open('https://www.facebook..com/' + str(name))
    webbrowser.open('https://twitter.com/' + str(name.lower()))


#webbrowser.open(url)

try:
    url3 = 'https://www.instagram.com/' + str(for_twitter)
    webbrowser.open(url3)

except ValueError:
    webbrowser.open('hhtps://instagram.com/') + str(name.lower())



