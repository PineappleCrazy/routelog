import os
import json
from PIL import Image

citypath = os.path.join(os.path.dirname(__file__), 'references', 'cityref.json') # finding references folder to fetch json files
navaid_data = os.path.join(os.path.dirname(__file__), 'references', 'navaids.json')
country_name_data = os.path.join(os.path.dirname(__file__), 'references', 'country_names.json')
airlpath = os.path.join(os.path.dirname(__file__), 'references', 'airlref.json')
countrypath = os.path.join(os.path.dirname(__file__), 'references', 'countryref.json')
firpath = os.path.join(os.path.dirname(__file__), 'references', 'firref.json')
aircpath = os.path.join(os.path.dirname(__file__), 'references', 'aircref.json')

with open(navaid_data,'r',encoding='utf-8') as i:
    navaids = json.load(i) # fetching navaids from json
with open(country_name_data,'r',encoding='utf-8') as i:
    country_names = json.load(i) # fetching countries from json
with open(airlpath,'r',encoding='utf-8') as i:
    airlines = json.load(i) # fetching valid airlines from json
with open(citypath,'r',encoding='utf-8') as i:
    citynames = json.load(i) # fetching cities from json
with open(countrypath,'r',encoding='utf-8') as i:
    countryref = json.load(i) # fetching cities from json
with open(firpath,'r',encoding='utf-8') as i:
    firref = json.load(i) # fetching cities from json
with open(aircpath,'r',encoding='utf-8') as i:
    aircrafts = json.load(i) # fetching valid aircraft from json

def numVal(): # as of now acts as presence check.. might make more complex later, eg making it fit with airline
    while True:
        user_input = input("\nEnter flight number: ")
        user_input = user_input.upper()
        if len(user_input) > 2:
            return user_input
        else:
            print("Invalid input. Ensure at least 3 characters.")

def inputVal():
    while True:
        user_input = input("\nEnter airport: ")
        user_input = user_input.lower()
        if user_input in citynames or user_input == 'null': # a user COULD enter 'null' and it would get logged... haha.. just dont
            return user_input
        else:
            print("Invalid input. Please enter a valid airport ICAO code.") # should be self explanatory

def inputVal1(): # secondary function only used selecting airports for searches
    while True:
        user_input = input("\nEnter location (airport or supported grouping): ")
        user_input = user_input.lower()
        char_map = {
            'á': 'a', 'ä': 'a', 'å': 'a', 'ă': 'a',
            'é': 'e', 'ë': 'e', 'è': 'e',
            'í': 'i', 'ī': 'i',
            'ö': 'o', 'ø': 'o',
            'ü': 'u',
            'ș': 's', 'š': 's'
        }
        user_input = user_input.translate(str.maketrans(char_map))
        if user_input in citynames or user_input == 'null': # a user COULD enter 'null' and it would get logged... haha.. just dont
            return user_input
        elif user_input in countryref:
            return countryref[user_input]
        else:
            print("Invalid input. Please enter a valid airport ICAO code.") # should be self explanatory

def aircVal():
    while True:
        user_input = input("\nEnter aircraft: ")
        user_input = user_input.lower()
        if user_input in aircrafts or user_input == 'null':
            return user_input
        else:
            print("Invalid input. Please enter a valid aircraft type code.")

def airlVal():
    while True:
        user_input = input("\nEnter airline: ")
        user_input = user_input.lower()
        if user_input in airlines or user_input == 'null':
            return user_input
        else:
            print("Invalid input. Please enter a valid airline ICAO code.")

def search_navaid():
    navaid = input("\nEnter navaid identifier: \n\n")
    navaid = navaid.lower()
    print(f"\n{navaids[f"{navaid}"]["name"]} | {navaids[f"{navaid}"]["type"]}")
    country_id = navaids[f"{navaid}"]["country"]
    print(country_names[country_id])
    print(f"{navaids[f"{navaid}"]["freq"]}")

def selectImage():
    imageAirp = inputVal()
    imageAirp = imageAirp.upper()
    imageAirl = airlVal()
    imageAirl = imageAirl.upper()
    fileLocation = os.path.join(os.path.dirname(__file__), 'images', 'portlayouts', f'{imageAirp}{imageAirl}.png') # compiles file name to search for
    try: # looks for image
        currentImage = Image.open(fileLocation)
        print(f"\nShowing gate info for {imageAirl} at {imageAirp}... window opening now")
        currentImage.show()
    except FileNotFoundError:
        print("\nGate info unavailable, or inputs invalid!")