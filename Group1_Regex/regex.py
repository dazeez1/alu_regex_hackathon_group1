#!/usr/bin/env python

import re

# Group 3 Sample input strings
strings = [
    "Avengers (2019)",
    "The gods must be crazy (1980)",
    "365 Days (2020)",
    "[Verse 1] Crossed over like I'm Iverson on Jordan",
    "@Malongmak",
    "ISBN 123-4-567-89012-3",
    "Why did the bug seem stressful? Because it adds up to all your problems!",
    "Show Name S01E02: Episode Title",
    "12-March-1996",
    "#ABC123",
    "192.168.0.1",
    #Song Lyrics:
    "[Verse 1] I wanna hold your hand",

    #Twitter Usernames:
    "@johnsmith",
    "@sarahjones",
    "@awesome_dev",
    "@ajoshuamalong2",
    "@emmanuelyakubu3",
    #ISBN numbers:,
    "ISBN 1-2-345-67890-1",
    "ISBN 9-87-654321-0",
    #Jokes:
    "Why did the chicken cross the road? Because it wanted to get to the other side!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the cow have a bell? Because it didnt have a working horn!",
    #TV Episode Titles:
    "Friends S02E05: The One with Five Steaks and an Eggplant",
    "Breaking Bad S03E10: Fly",
    #Weirdly Formatted Dates:
    "22-May-2023",
    "01-Dec-2022",
    #Hex Color Codes:
    "#FFA500",
    "#00FF00",
    #IP Addresses:
    "192.168.0.1",
    "10.0.0.254",

]

# Regular expressions
movie_title_regex = r"^(.*?) \(\d{4}\)$"
song_lyrics_regex = r"^\[Verse \d+] .*$"
twitter_username_regex = r"^@[\w\d]+$"
isbn_regex = r"^ISBN \d{3}-\d-\d{3}-\d{5}-\d$"
joke_regex = r"^Why did the .*?\? Because.*$"
episode_title_regex = r"^.*? S\d{2}E\d{2}: .*$"
date_regex = r"^\d{2}-[A-Za-z]{3}-\d{4}$"
hex_color_regex = r"^#[A-Fa-f1-9]{6}$"
ip_address_regex = r"^(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$"

# Extract data types using regular expressions
movie_titles = []
song_lyrics = []
twitter_usernames = []
isbn_numbers = []
jokes = []
episode_titles = []
weird_dates = []
hex_colors = []
ip_addresses = []

for string in strings:
    if re.match(movie_title_regex, string):
        movie_titles.append(string)
    elif re.match(song_lyrics_regex, string):
        song_lyrics.append(string)
    elif re.match(twitter_username_regex, string):
        twitter_usernames.append(string)
    elif re.match(isbn_regex, string):
        isbn_numbers.append(string)
    elif re.match(joke_regex, string):
        jokes.append(string)
    elif re.match(episode_title_regex, string):
        episode_titles.append(string)
    elif re.match(date_regex, string):
        weird_dates.append(string)
    elif re.match(hex_color_regex, string):
        hex_colors.append(string)
    elif re.match(ip_address_regex, string):
        ip_addresses.append(string)

# Print extracted data types
print("Movie Titles:", movie_titles)
print("Song Lyrics:", song_lyrics)
print("Twitter Usernames:", twitter_usernames)
print("ISBN Numbers:", isbn_numbers)
print("Jokes:", jokes)
print("Episode Titles:", episode_titles)
print("Weird Dates:", weird_dates)
print("Hex Colors:", hex_colors)
print("IP Addresses:", ip_addresses)
