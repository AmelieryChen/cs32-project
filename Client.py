#speaking to client

#Asking our client some questions to get started with the art gallery
#print("Hello! Welcome to create your own Art Exhibit!")

#name = input("What's your name? ")

# Do something with the input
print("Hello, " + name + "! Nice to meet you and let's get started!!")

year = input('What year would you like? ')
title = input('What is your desired art piece called? ')
#start_time = input("Please enter the start year: ")
#end_time = input("Please enter the end year: ")
#write a program to only accept years within a certain range
#if not in range, let user know and set the time limit
artist = input('What artist would you like? ' )

#artist = input("Do you have a preferred artist? or type 'N/A' if none:  ")
    #if there is none, disregard this search
#country = input("Please enter the culture or country: ")
    #searching for culture and country all together

#material = input("Please specify the material: (print, paint,..)")
    #look up material or classification on Harvard website to find different types

#Start Searching!

#pull out a piece of artwork:
import csv

with open("artworks.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

print(f'{title} was made in {year} by {artist}')



#Searching can be implemented on another piece of code:


