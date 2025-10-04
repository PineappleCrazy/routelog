# --- WELCOME ---

# Please DO NOT TOUCH unless you know what you're doing.
# I've vaguely commented the functions of sections.. but you'll need to reach out for a proper breakdown.

import shutil # module to backup files
import os
import json

citypath = os.path.join(os.path.dirname(__file__), 'references', 'cityref.json') # finding references folder to fetch json files
countrypath = os.path.join(os.path.dirname(__file__), 'references', 'countryref.json')
firpath = os.path.join(os.path.dirname(__file__), 'references', 'firref.json')
airlpath = os.path.join(os.path.dirname(__file__), 'references', 'airlref.json')
aircpath = os.path.join(os.path.dirname(__file__), 'references', 'aircref.json')

routenumtxt = os.path.join(os.path.dirname(__file__), 'localdata', 'routenum.txt') # letting silly python find its text files
routestxt = os.path.join(os.path.dirname(__file__), 'localdata', 'routes.txt')
shuttletxt = os.path.join(os.path.dirname(__file__), 'localdata', 'shuttle.txt')
backuptxt = os.path.join(os.path.dirname(__file__), 'localdata', 'backup.txt')
logtxt = os.path.join(os.path.dirname(__file__), 'localdata', 'log.txt')
aircraftseltxt = os.path.join(os.path.dirname(__file__), 'localdata', 'aircsel.txt')
firtxt = os.path.join(os.path.dirname(__file__), 'localdata', 'fir.txt')

with open(citypath,'r',encoding='utf-8') as i:
    citynames = json.load(i) # fetching cities from json
with open(countrypath,'r',encoding='utf-8') as i:
    countryref = json.load(i) # fetching cities from json
with open(firpath,'r',encoding='utf-8') as i:
    firref = json.load(i) # fetching cities from json
with open(airlpath,'r',encoding='utf-8') as i:
    airlines = json.load(i) # fetching valid airlines from json
with open(aircpath,'r',encoding='utf-8') as i:
    aircrafts = json.load(i) # fetching valid aircraft from json
 
end = 1 # constants, so fun
valid = 0

with open(aircraftseltxt,'r') as file:
        airclist = str(file.readlines())
        airclist.strip()

with open(firtxt,'r') as file:
    localFIR = str(file.readlines())
    localFIR = localFIR.strip("[]").strip("'")

def backup():
    shutil.copy(routestxt, backuptxt) # copying routes to backup after every modification

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

def firVal(): # checking if an airport of home FIR selected
    return firref[localFIR]

def airlVal():
    while True:
        user_input = input("\nEnter airline: ")
        user_input = user_input.lower()
        if user_input in airlines or user_input == 'null':
            return user_input
        else:
            print("Invalid input. Please enter a valid airline ICAO code.")

def aircVal():
    while True:
        user_input = input("\nEnter aircraft: ")
        user_input = user_input.lower()
        if user_input in aircrafts or user_input == 'null':
            return user_input
        else:
            print("Invalid input. Please enter a valid aircraft type code.")
            # they can read - lovely. might do that.. once

def numVal(): # as of now acts as presence check.. might make more complex later, eg making it fit with airline
    while True:
        user_input = input("\nEnter flight number: ")
        user_input = user_input.upper()
        if len(user_input) > 2:
            return user_input
        else:
            print("Invalid input. Ensure at least 3 characters.")

def add():
    cont = 1
    dep = inputVal()
    arr = inputVal()
    # using logs like this is disgustingly inefficient.. it's a text file, they'll cope
    
    with open(logtxt,'w') as file:
        logwrite = (dep+'\n'+arr)
        file.write(logwrite)
    with open(logtxt,'r') as file:
        lines = file.readlines()
        lines.sort()
    with open(logtxt,'w') as sorted_file:
        sorted_file.writelines(lines)
    with open(logtxt, 'r') as file:
        routeid = [line.strip() for line in file.readlines()]
    airl = airlVal()
    adding = ''.join(routeid) + airl

    # oh god it's disgusting.. might be made more efficient by the next century


    with open(routestxt,'r') as file:
        lines = file.readlines()
        for line in lines:
            if adding in line:
              print('\nRoute already found!\n')
              cont = 0
    
    if cont == 1:
        print("\nEnter 'yes' to select an aircraft. Press ENTER to skip an aircraft")
        if 'a220' in airclist:
            a220 = input("\nA220?: ")
            if a220 == 'yes':
                adding += ',a2200'
        if 'a320' in airclist:
            a320 = input("A320?: ")
            if a320 == 'yes':
                adding += ',a3200'
        if 'a330' in airclist:
            a330 = input("A330?: ")
            if a330 == 'yes':
                adding += ',a3300'
        if 'a340' in airclist:
            a340 = input("A340?: ")
            if a340 == 'yes':
                adding += ',a3400'
        if 'a350' in airclist:
            a350 = input("A350?: ")
            if a350 == 'yes':
                adding += ',a3500'
        if 'a380' in airclist:
            a380 = input("A380?: ")
            if a380 == 'yes':
                adding += ',a3800'
        if 'b737' in airclist:
            b737 = input("B737?: ")
            if b737 == 'yes':
                adding += ',b7370'
        if 'b747' in airclist:
            b747 = input("B747?: ")
            if b747 == 'yes':
                adding += ',b7470'
        if 'b757' in airclist:
            b757 = input("B757?: ")
            if b757 == 'yes':
                adding += ',b7570'
        if 'b767' in airclist:
            b767 = input("B767?: ")
            if b767 == 'yes':
                adding += ',b7670'
        if 'b777' in airclist:
            b777 = input("B777?: ")
            if b777 == 'yes':
                adding += ',b7770'
        if 'b787' in airclist:
            b787 = input("B787?: ")
            if b787 == 'yes':
                adding += ',b7870'
        if 'ex45' in airclist:
            ex45 = input("E145?: ")
            if ex45 == 'yes':
                adding += ',ex450'
        if 'ejet' in airclist:
            ejet = input("Ejet?: ")
            if ejet == 'yes':
                adding += ',ejet0'
        if 'atrs' in airclist:
            atrs = input("ATRs?: ")
            if atrs == 'yes':
                adding += ',atrs0'
        if 'crjs' in airclist:
            crjs = input("CRJs?: ")
            if crjs == 'yes':
                adding += ',crjs0'
        if 'dash' in airclist:
            dash = input("Dash?: ")
            if dash == 'yes':
                adding += ',dash0'
        if 'dx28' in airclist:
            dx28 = input("Dorniers?: ")
            if dx28 == 'yes':
                adding += ',dx280'
        adding = adding + '\n'

        # shit lets just limit them to 7 type ranges.. more should be easy to do if i want
        # is a yes/no system good, no - will it stop people from being nonces and putting in invalidities, yes!
        
        if len(adding) > 13:
            with open(routestxt, 'a') as file:
                file.write(adding)

            with open(routestxt, 'r') as file:
                lines = file.readlines()
                header = lines[0]
                middle_lines = lines[1:]
                middle_lines.sort()
                sorted_lines = [header] + middle_lines

                # all to stop sorting the funny txt validation into the list hahaha

            with open(routestxt, 'w') as file:
                file.writelines(sorted_lines)
            print('\nRoute added succesfully. Thanks!\n')
            backup()
        else:
            print("\nYou must select an aircraft. Addition failed.")


def display():
    dep = inputVal()
    arr = inputVal()
    with open(logtxt,'w') as file:
        logwrite = (dep+'\n'+arr)
        file.write(logwrite)
    with open(logtxt,'r') as file:
        lines = file.readlines()
        lines.sort()
    with open(logtxt,'w') as sorted_file:
        sorted_file.writelines(lines)
    with open(logtxt, 'r') as file:
        routeid = [line.strip() for line in file.readlines()]
    airl = airlVal()
    search = ''.join(routeid) + airl

    with open(routestxt, 'r') as file:
        for i, line in enumerate(file, 1):
            if search in line:
                grab = line.strip()
                print('\n - ')
                title = (f"\n{grab[:4]} - {grab[4:8]} | {airlines.get(grab[8:11])}\n")
                title = title.upper()
                print(title)
                print(f"{citynames.get(grab[:4], 'Unknown')} - {citynames.get(grab[4:8], 'Unknown')}\n") # oh this will be fun to decrypt in the future..

                with open(routenumtxt,'r') as file:
                    lines = file.readlines()
                    lists = ''
                    for line in lines:
                        if grab[:11] in line:
                            grab1 = line.strip()
                            lists = (f"{lists}{grab1[-6:]}, ") # compiling list of route numbers

                if len(lists) != 0:
                    print(f"{lists}\n") # only show route numbers if they.. exist.. duh

                for aircraft in grab.split(",")[1:]:
                        if aircraft[:-1] in airclist:
                            if aircraft[-1] == "0":
                                print(f'{aircraft[:-1].upper()} - Incomplete')
                            elif aircraft[-1] == "1":
                                print(f'{aircraft[:-1].upper()} - Complete')
                            else:
                                print(f"Invalid formating for the aircraft {aircraft[:-1]}")
                        else:
                            print(f"The aircraft {aircraft[:-1]} does not exist within the list!")

def addnum():
    found = False
    found1 = False
    dep = inputVal()
    arr = inputVal()
    with open(logtxt,'w') as file:
        logwrite = (dep+'\n'+arr)
        file.write(logwrite)
    with open(logtxt,'r') as file:
        lines = file.readlines()
        lines.sort()
    with open(logtxt,'w') as sorted_file:
        sorted_file.writelines(lines)
    with open(logtxt, 'r') as file:
        routeid = [line.strip() for line in file.readlines()] # gathering ID
    airl = airlVal()
    search = ''.join(routeid) + airl

    num = numVal()

    if len(num) < 6:
        num = num.ljust(6, '/') # extending flight num to 6 characters if shorter.. means reading later on doesn't kill itself
    num = f",{num}"

    with open(routestxt,'r') as file:
        lines = file.readlines()
        for line in lines:
            if search in line:
                found1 = True # checking if route exists

    with open(routenumtxt,'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if num in line and search in line:
                found = True # checking if route number already in use

    if found == False and found1 == True:
        with open(routenumtxt,'a') as file:
            file.write(f"{search}{num}\n")
        with open(routenumtxt,'r') as file:
            lines = file.readlines()
            lines.sort()
        with open(routenumtxt,'w') as file:
            file.writelines(lines)
        print('\nFlight num added succesfully!') # adding routenumber is 2 prior criteria are valid

    if found == True:
        print('\nFlight num already found!')
    if found1 == False:
        print('\nRoute invalid!')


def addacft():
    dep = inputVal()
    arr = inputVal()
    with open(logtxt,'w') as file:
        logwrite = (dep+'\n'+arr)
        file.write(logwrite)
    with open(logtxt,'r') as file:
        lines = file.readlines()
        lines.sort()
    with open(logtxt,'w') as sorted_file:
        sorted_file.writelines(lines)
    with open(logtxt, 'r') as file:
        routeid = [line.strip() for line in file.readlines()] # nonsense compiling the ID to later implement
    airl = airlVal()
    search = ''.join(routeid) + airl
    
    adding = aircVal()
    adding1 = (f',{adding}0')

    with open(routestxt, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines): # finding where to correctly add
        if search in line:
            if adding1 not in line and adding in aircrafts:
                grab = line.strip()
                acfts = [grab[i:i+6] for i in range(11, len(grab), 6)]
                acfts.append(adding1)
                acfts.sort()
                readd = grab[:11] + "".join(acfts)
                lines[i] = readd + '\n'
                print('\nAircraft added, thanks!')
                break
            else:
                print('\nAircraft already in database!')
    with open(routestxt, 'w') as file:
        file.writelines(lines)
    backup()


def viewall():
    incompRts = 0
    allRts = 0
    with open(routestxt,'r') as file:
        next(file)
        print('\n - ')
        lines = file.readlines()
        for line in lines:
            secondPos = line[18:22] if len(line) >= 22 else '#'
            thirdPos = line[24:28] if len(line) >= 28 else '#'
            fourthPos = line[30:34] if len(line) >= 34 else '#'
            fifthPos = line[36:40] if len(line) >= 40 else '#'
            sixthPos = line[42:46] if len(line) >= 46 else '#'
            
            FIRports = firVal()
            if (line[12:16] in airclist or secondPos in airclist or thirdPos in airclist or fourthPos in airclist or fifthPos in airclist or sixthPos in airclist) and (match(FIRports, line)):
                grab = line.strip()
                title = (f"\n{grab[:4]} - {grab[4:8]} | {airlines.get(grab[8:11])}\n")
                title = title.upper()
                print(title)
                print(f"{citynames.get(grab[:4], 'Unknown')} - {citynames.get(grab[4:8], 'Unknown')}\n")

                with open(routenumtxt,'r') as file:
                        lines = file.readlines()
                        lists = ''
                        for line in lines:
                            if grab[:11] in line:
                                grab1 = line.strip()
                                lists = (f"{lists}{grab1[-6:]}, ") # all viewing stuff noted prior

                if len(lists) != 0:
                    print(f"{lists}\n")

                for aircraft in grab.split(",")[1:]:
                        if aircraft[:-1] in airclist:
                            if aircraft[-1] == "0":
                                print(f'{aircraft[:-1].upper()} - Incomplete')
                                allRts += 1
                                incompRts += 1
                            elif aircraft[-1] == "1":
                                print(f'{aircraft[:-1].upper()} - Complete')
                                allRts += 1
                            else:
                                print(f"Invalid formating for the aircraft {aircraft[:-1]}")
                        else:
                            print(f"The aircraft {aircraft[:-1]} does not exist within the list!")

                        print("\n - ")
    if allRts > 0:
        print(f'\n{allRts-incompRts} flights completed of {allRts} total.\n')
        print(f'% completion: {100*((allRts-incompRts)/allRts)}\n\nRoutes for {localFIR.upper()} FIR') # nice little stats after the spewage.. fun. Gives total and percentage for now
    else:
        print("No applicable routes!")
                    

def complete():
    dep = inputVal()
    arr = inputVal()
    with open(logtxt,'w') as file:
        logwrite = (dep+'\n'+arr)
        file.write(logwrite)
    with open(logtxt,'r') as file:
        lines = file.readlines()
        lines.sort()
    with open(logtxt,'w') as sorted_file:
        sorted_file.writelines(lines)
    with open(logtxt, 'r') as file:
        routeid = [line.strip() for line in file.readlines()]
    airl = airlVal()
    search = ''.join(routeid) + airl

    acft = aircVal()
    with open(routestxt,'r') as file:
        lines = file.readlines()

    with open(routestxt,'w') as file:
        for line in lines:
            if search in line:
                incomp = (acft+'0')
                comp = (acft+'1')
                line = line.replace(incomp,comp)
            file.write(line)
        print('\nRoute marked as completed. Thanks!\n')
    backup()
    # besides the log shenanigans, this isn't too awful. don't touch it !!!


def uncomplete():
    dep = inputVal()
    arr = inputVal()
    with open(logtxt,'w') as file:
        logwrite = (dep+'\n'+arr)
        file.write(logwrite)
    with open(logtxt,'r') as file:
        lines = file.readlines()
        lines.sort()
    with open(logtxt,'w') as sorted_file:
        sorted_file.writelines(lines)
    with open(logtxt, 'r') as file:
        routeid = [line.strip() for line in file.readlines()]
    airl = airlVal()
    search = ''.join(routeid) + airl

    acft = aircVal()
    with open(routestxt,'r') as file:
        lines = file.readlines()

    with open(routestxt,'w') as file:
        for line in lines:
            if search in line:
                incomp = (acft+'1')
                comp = (acft+'0')
                line = line.replace(incomp,comp)
            file.write(line)
        print('\nRoute marked as uncompleted. Thanks!\n')
    backup()
    # exact same as prior function.. just inverse

def match(val, line): # searches based on country
    line_slice = line.strip()[:8].lower()

    if isinstance(val, list):
        return any(item.lower() in line_slice for item in val)
    else:
        return val.lower() in line_slice

def special():
    incompRts = 0
    allRts = 0
    print(' - ENTER "NULL" TO SKIP ANY CRITERIA - ')
    searchAirp = inputVal1()
    searchAirl = airlVal()
    FIRports = firVal()
    if searchAirl == 'null':
        searchAirl = ','
    searchAirc = aircVal()
    if searchAirc == 'null':
        searchAirc = ','
    with open(routestxt,'r') as file:
        lines = file.readlines()
        print('\n - ')
        for line in lines:
            airlCheck = line[8:11] # finding airline used on route
            if (match(searchAirp, line) or searchAirp == 'null') and (searchAirl in airlCheck or searchAirl == ',') and searchAirc in line and (match(FIRports, line)): # checking if airport is in countryref item, if airline is correct, yada yada filterswhy 

                secondPos = line[18:22] if len(line) >= 22 else '#'
                thirdPos = line[24:28] if len(line) >= 28 else '#'
                fourthPos = line[30:34] if len(line) >= 34 else '#'
                fifthPos = line[36:40] if len(line) >= 40 else '#'
                sixthPos = line[42:46] if len(line) >= 46 else '#'
                
                if line[12:16] in airclist or secondPos in airclist or thirdPos in airclist or fourthPos in airclist or fifthPos in airclist or sixthPos in airclist:
                    grab = line.strip()
                    title = title = (f"\n{grab[:4]} - {grab[4:8]} | {airlines.get(grab[8:11])}\n")
                    title = title.upper()
                    print(title)
                    print(f"{citynames.get(grab[:4], 'Unknown')} - {citynames.get(grab[4:8], 'Unknown')}\n")

                    with open(routenumtxt,'r') as file:
                        lines = file.readlines()
                        lists = ''
                        for line in lines:
                            if grab[:11] in line:
                                grab1 = line.strip()
                                lists = (f"{lists}{grab1[-6:]}, ") # accumulating list of flight nums

                    if len(lists) != 0:
                        print(f"{lists}\n")

                    for aircraft in grab.split(",")[1:]:
                        if aircraft[:-1] in airclist:
                            if aircraft[-1] == "0":
                                print(f'{aircraft[:-1].upper()} - Incomplete')
                                allRts += 1
                                incompRts += 1
                            elif aircraft[-1] == "1":
                                print(f'{aircraft[:-1].upper()} - Complete')
                                allRts += 1
                            else:
                                print(f"Invalid formating for the aircraft {aircraft[:-1]}")
                        else:
                            print(f"The aircraft {aircraft[:-1]} does not exist within the list!")

                        print("\n - ")

        if allRts > 0:
            print(f'\n{allRts-incompRts} flights completed of {allRts} total.\n')
            print(f'% completion: {100*((allRts-incompRts)/allRts)}\n\nRoutes for {localFIR.upper()} FIR')
        else:
            print("No applicable routes!")

def aircsel():
    print("\nType 'y' to select an aircraft. These aircraft will be prompted when adding and viewing routes.")
    airclist = ''
    a220 = input("\nA220?: ")
    if a220 == 'y':
        airclist += 'a220'
    a320 = input("A320?: ")
    if a320 == 'y':
        airclist += 'a320'
    a330 = input("A330?: ")
    if a330 == 'y':
        airclist += 'a330'
    a340 = input("A340?: ")
    if a340 == 'y':
        airclist += 'a340'
    a350 = input("A350?: ")
    if a350 == 'y':
        airclist += 'a350'
    a380 = input("A380?: ")
    if a380 == 'y':
        airclist += 'a380'
    b737 = input("B737?: ")
    if b737 == 'y':
        airclist += 'b737'
    b747 = input("B747?: ")
    if b747 == 'y':
        airclist += 'b747'
    b757 = input("B757?: ")
    if b757 == 'y':
        airclist += 'b757'
    b767 = input("B767?: ")
    if b767 == 'y':
        airclist += 'b767'
    b777 = input("B777?: ")
    if b777 == 'y':
        airclist += 'b777'
    b787 = input("B787?: ")
    if b787 == 'y':
        airclist += 'b787'
    ex45 = input("Embraer 145?: ")
    if ex45 == 'y':
        airclist += 'ex45'
    ejet = input("Embraer 170/5/90/95?: ")
    if ejet == 'y':
        airclist += 'ejet'
    atrs = input("ATRs?: ")
    if atrs == 'y':
        airclist += 'atrs'
    crjs = input("CRJs?: ")
    if crjs == 'y':
        airclist += 'crjs'
    dash = input("Dash?: ")
    if dash == 'y':
        airclist += 'dash'
    dx28 = input("DX28?: ")
    if dx28 == 'y':
        airclist += 'dx28'
    with open(aircraftseltxt,'w') as file:
        file.write(airclist)
    print("\nSuccess - thanks! To apply, restart program")

def setFIR():
    FIRentry = input("\nEnter 4-digit FIR: ")
    if FIRentry == 'any':
        with open(firtxt,'w') as file:
            file.write('unselected')
            print('\nRemoved your home FIR!\nRestart program for changes to take effect\n')
    elif FIRentry == 'ebbu' or FIRentry == 'EBBU':
        with open(firtxt,'w') as file:
            file.write('ebbu')
            print('\nSet your home FIR to EBBU - Thanks!\nRestart program for changes to take effect\n')
    elif FIRentry == 'ehaa' or FIRentry == 'EHAA':
        with open(firtxt,'w') as file:
            file.write('ehaa')
            print('\nSet your home FIR to EHAA - Thanks!\nRestart program for changes to take effect\n')
    elif FIRentry == 'gccc' or FIRentry == 'GCCC':
        with open(firtxt,'w') as file:
            file.write('gccc')
            print('\nSet your home FIR to GCCC - Thanks!\nRestart program for changes to take effect\n')
    elif FIRentry == 'gmmm' or FIRentry == 'GMMM':
        with open(firtxt,'w') as file:
            file.write('gmmm')
            print('\nSet your home FIR to GMMM - Thanks!\nRestart program for changes to take effect\n')
    elif FIRentry == 'gvsc' or FIRentry == 'GVSC':
        with open(firtxt,'w') as file:
            file.write('gvsc')
            print('\nSet your home FIR to GVSC - Thanks!\nRestart program for changes to take effect\n')
    elif FIRentry == 'lccc' or FIRentry == 'LCCC':
        with open(firtxt,'w') as file:
            file.write('lccc')
            print('\nSet your home FIR to LCCC - Thanks!\nRestart program for changes to take effect\n')
    else:
        print("FIR entry invalid, or unsupported FIR. Currently supported: EBBU")


def welcome():
    print('Welcome to Routelog! - your comprehensive tracker of all flight progress\n\nTo begin, please select your wanted aircraft types using the -9- function you will be prompted with next\n')
    print("Function information can be found in README.md\nThanks,")
    print("\nYou are currently on NO routedata. To use our official data, import through the shuttle (follow funct. 11)\n")
    a = input('\nPress ENTER to continue: ')
    with open(logtxt,'w') as file:
        file.write("entry")



def importing():
    print("\nImporting. This may take anywhere from an instant to a minute or two, depending on the load...")
    addingcount = 0
    with open (shuttletxt,'r') as file:
        lines = file.readlines()
        for line in lines:
            found2 = False
            line.replace('1','0')
            with open(routestxt,'r') as file:
                linescheck = file.readlines()
                for line1 in linescheck:
                    if line in line1:
                        found2 = True
            if found2 == False:
                addingcount += 1
                with open(routestxt,'a') as file:
                    line = line.replace('1','0')
                    file.write(line)
    if addingcount > 0:
        print(f"\nThanks! Succesfully imported {addingcount} routes!")
    else:
        print("\nNo routes applicable to add!")



# - END OF FUNCTIONS -
                

with open(routestxt,'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'LOCAL ROUTE DATA - DO NOT MODIFY' in line: # checking the sillies havent tampered with their routes.txt file
            valid = 1

with open(logtxt,'r') as file:
    lines = file.readlines()
    firstTime = 0
    for line in lines:
        if 'INIT' in line:
            welcome()
            firstTime=1

if firstTime != 1:
    print("Welcome to Routelog!")

if valid == 1:
    while True:
        choice = input("\n - - - - - - - - - - - - -\n\nWould you like to: \n\n1 - Add a route\n2 - View a specific route\n3 - Mark flight as complete\n4 - Mark flight as uncomplete\n5 - View all routes\n6 - View filtered routes\n7 - Add an aircraft to a route\n8 - Add a route number\n9 - Select your aircraft\n10 - Select your based FIR\n11 - Data settings\n\n") # beautifully simple
        if choice == '1':
            add()
        elif choice == '2':
            display()
        elif choice == '3':
            complete()
        elif choice == '4':
            uncomplete()
        elif choice == '5':
            viewall()
        elif choice == '6':
            special()
        elif choice == '7':
            addacft()
        elif choice == '8':
            addnum()
        elif choice == '9':
            aircsel()
        elif choice == '10':
            setFIR()
        elif choice == '11':
            setchoice = input("\n1 - Import shuttle\n\n")
            if setchoice == '1':
                importing()
        elif choice == 'firs':
            print('\nCurrently supported FIRs:\n\nEBBU - Brussels\nEHAA - Amsterdam\nGCCC - Canary Islands\nGOOO - Nouakchott\nGVSC - Cape Verde\nLCCC - Nicosia')
        else:
            print('\nPlease enter a number as displayed above.') # taking choices for function

else:
    print('! CAUTION !\n\nLocal route data has been tampered with, or is corrupted. Your data may be recovered using steps as follows:\n\n') # punishing the silies if they HAVE tampered with their routes.txt file
    print('Delete all contents from "routes.txt"\nCopy contents of "backup.txt" and paste into "routes.txt" IN FULL\nData should be restored - if not, reach out.')
