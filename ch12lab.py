#!/usr/bin/env python3.7

#Python implementation here

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

words = message.split() #splits the phrase apart into words
print("Words:", words)

sorted_words = sorted(words) #Puts words in alphabetical order by character number
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])