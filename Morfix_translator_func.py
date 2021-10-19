import requests
import re
import webbrowser
import pygame
import os
import time
import subprocess
import requests


def morfix_translate(word):
    
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
            return("TEST 1")

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
            return  (URL)
# No results found
        else:
            html.replace("\n", '')
            return(html)

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
            return("TEST 3")

        else:
            html.replace("\n", '')
            x = html
            return x.replace("\r\n", " ").replace(",", ", ")
