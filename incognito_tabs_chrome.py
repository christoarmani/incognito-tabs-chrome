"""
Created on Tue Aug 2 24:39:20 2021

@author: christoarmani
"""
import os
import webbrowser

directory = input('Paste directory path:')
clean_directory = directory.split('"')
os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito"

with open(clean_directory[1], "r") as txt_file:
    data = txt_file.readlines()

for url in data:
    webbrowser.get(chrome).open_new(url)
    print(url)