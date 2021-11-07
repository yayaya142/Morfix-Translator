from openpyxl import Workbook
import requests
import re
import webbrowser
import os
import time
import subprocess
import codecs
import requests
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

window = Tk()


def morfix_translate(word):
    """
   :This func is used for translate words from english to hebrew
   :Param word: the word you want to translate
   :Type bass: str
   :Return: The word in hebrew
   :Retype: str
   """
    URL = "http://www.morfix.co.il/"

    word = word.replace(' ', "%20")  # the URL see %20 as space
    URL = URL + word

    try:
        # sending the http(s) request.  this is where the program can crash. it's probably the server so try again
        response = requests.get(URL)
        html = response.text
    except:
        return("Problem with the server, please restart (The program crashed)")

    if html.find("Request - Invalid") > -1:
        return("Invalid input")

        if len(html) >= 3000:  # more than 3000 is 99% means no result found
            return(f"Bug 1 use: {URL}")

        else:
            html.replace("\n", '')
            return(html)

    elif URL.find("%20") > -1:  # if there are more than 2 English words
        place = html.find(
            """class="MachineTranslation_divfootertop_enTohe">""")
        html = html[place + 48:]
        place = html.find("</div>")
        html = html[: place]

        if len(html) >= 3000:  # more than 3000 is 99% means no result found
            return (f"Bug 2 use: {URL}")
        else:
            html.replace("\n", '')
            x = html
            x = x.strip()
            return x.replace("\n", " ")

    else:  # one English or Hebrew word
        place = html.find("normal_translation_div")
        html = html[place + 24:]
        place = html.find("div class")
        html = html[:place - 1]
        html = html.replace("</div>", "")

        html = html.replace("</span>", "")
        html = html.replace(
            "<span class='clearOutputLanguageMeaningsString'>;", ",")

        if len(html) >= 3000:  # more than 3000 is 99% means no result found
            return (f"Bug 3 use: {URL}")

        else:
            html.replace("\n", '')
            x = html
            x = x.strip()
            return x.replace("\n", " ")

#region file location
#               execl part
# open execl 
def openFile():
    """
   :This func is used return the file location 
   :Param word: This is used in anoter func called 'file_location' 
   :Type bass: str
   :Return: The file location
   :Retype: str
   """
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Choose file",
                                          filetypes=(("xlsx files", "*.xlsx"),
                                                     ("all files", "*.*")))
    global x
    x = (filepath)
    window.destroy()
#end execl

# file path excel
def file_location():
    """
   :This func is used to Open a window from which you can select the location of the file
   :Return: the file loction as (x)
   :Retype: str
   """
    Button(window, text='Open file', command=openFile).pack(fill=X)
    mainloop()
    return x
# end file path excel



#                   HTML part 
#open HTML
def openFile_HTML():
    """
   :This func is used return the file location 
   :Param word: This is used in anoter func called 'file_location' 
   :Type bass: str
   :Return: The file location
   :Retype: str
   """
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Choose file",
                                          filetypes=(("HTML files", "*.html"),
                                                     ("all files", "*.*")))
    global x
    x = (filepath)
    window.destroy()


def Open_html(file_path):

    file = codecs.open(f"{file_path}", "r", "utf-8")
    file = file.read()
    file = file.split("\n")
    note_text = 0
    word_list = []
    for word in file:
        if note_text == 1:
            word = remove_worng_strings(word)
            word_list.append(word)
            note_text = 0
        elif '<div class="noteText">' in word:
            note_text = 1
    return word_list
# end open html
#               end open HTML
def file_location_html():
    """
   :This func is used to Open a window from which you can select the location of the file
   :Return: the file loction as (x)
   :Retype: str
   """
    Button(window, text='Open file', command=openFile_HTML).pack(fill=X)
    mainloop()
    return x
# end file path excel
#fix files
def remove_worng_strings(word):
    """
   :This func is used return the word clean with no marks 
   :Param word: word' 
   :Type bass: str
   :Return: word
   :Retype: str
   """
    try:
        word = word.replace("?", "")
        word = word.replace("@", "")
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(":", "")
        word = word.replace("-", "")
        word = word.replace('"', "")
        word = word.replace("“", "")
        word = word.replace("”", "")
        word = word.replace("'", "")
        word = word.replace("!", "")
        word = word.rstrip()
        word = word.lstrip()
        return word
    except AttributeError:
        print("\t\t\t\t\n\nError\nremove empty lines")
        input("")
#end fix files

#endregion
