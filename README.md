# Welcome to Routelog!

This nifty program stores your routes and completion progress, allowing you to add and manage routes seamlessly.
We currently have over 2,000 flights stored, allowing you to keep track of and achieve your flying goals


### To import our current, *official* routes:
Download the latest [shuttle](https://github.com/PineappleCrazy/routelog/blob/main/shuttle.txt) and replace with old shuttle in your respective files. Import through `Data Settings` > `Import Shuttle` 


### To run:
Run the [batch file](https://github.com/PineappleCrazy/Routelog/blob/main/_routelog.bat)



### Where is supported?
We proudly (fully) support 57 aerodromes over 14 different countries.

**Countries fully supported:**
> + Belgium
> + Cape Verde
> + Gambia
> + Guinea
> + Guinea-Bissau
> + Luxembourg
> + Mauritania
> + Senegal
> + Sierra Leone
> 
**Countries partially supported:**
> + Morocco
> + Netherlands
> + Portugal (madeira + azores only)
> + Spain (canaries only)

**Countries coming soon:**
> + Algeria
> + Ireland
> + Portugal
> + Spain


## Guides:

### 1 - Adding routes:
This function adds a route to your database. It will ask for 2 airports and an airline, before prompting you with each available aircraft category.
The two airports must be input as their `4-DIGIT ICAO CODES`. They can be input in either order - it does not matter.
The airline must be input as its `3-DIGIT ICAO CODE`. Note that subsidiaries are generalised, eg. `RUK` (Ryanair UK) included into `RYR` (Ryanair).
When prompted with aircraft, enter EXACTLY "yes" to confirm an aircraft for that route. Under any other input, the program will assume otherwise. You will only be prompted with aircraft currently selected.

### 2 - View specific route:
This function lets you view the properties of a specific route. It will ask for 2 airports and an airline. These are to be input with the two airports and airline applicable. You will be provided with the route's characteristics.

### 3 - Mark route as Complete:
This function marks a route as complete under a specific aircraft type. Enter the route's details and the respective type.

### 4 - Mark route as Incomplete:
This function marks a route as incomplete under a specific aircraft type. Enter the route's details and the respective type.

### 5 - View all Routes
This function provides information for every route available. May cause issues on slower computers, so treat with care.

### 6 - Filtered Routes
This function displays routes under input filters. These filters are (one) airport, airline and aircraft type.
In the airport section, you may also enter a COUNTRY, CITY or CONTROL position (eg. `Austria`, `London`, `EGLL_N_APP`, `EBBU_W_CTR`), and all airports within these will be selected.
You may either input a value, or `NULL` to disregard that filter. You may use one, two, three filters in any order.

### 7 - Add Aircraft to Route
This function adds an aircraft to an existing route.
Input the two respective airports and airline before the new aircraft type. The aircraft will be assumed as incomplete when added.

### 8 - Add Route Number
This function assigns a route number to an existing route. Multiple numbers can be added per route. Route numbers will be displayed in viewing functions.

### 9 - Select Aircraft
This function lets you choose which aircraft you'll be prompted with when adding or viewing routes. These can be changed at any time.

### 10 - Select Home FIR
Routes will only be displayed if they are to/from your home FIR. Enter `any` to disregard this. Your home FIR can be changed at any time.

### 11 - Data Settings
Import routedata from shuttles provided

~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - 

Bits may not look amazing, but I'm working on it. Official routes are updated regularly, with future areas of development detailed above. If you'd be interested in further collecting and assessing routedata, pop me a message.

Thanks :D