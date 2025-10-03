# Welcome to Routelog!

This nifty program stores your routes and completion progress, allowing you to add and manage routes seamlessly.
We currently have over 2,000 flights stored, allowing you to keep track of and achieve your flying goals


### IF YOU NEED SUPPORT
Reach out on Discord



### Upon running, you will be prompted with all functions available. There is a guide to each below.

+ 1 - Adding routes:
This function adds a route to your database. It will ask for 2 airports and an airline, before prompting you with each available aircraft category.
The two airports must be input as their `4-DIGIT ICAO CODES`. They can be input in either order - it does not matter.
The airline must be input as its `3-DIGIT ICAO CODE`. Note that subsidiaries are generalised, eg. `RUK` (Ryanair UK) included into `RYR` (Ryanair).
When prompted with aircraft, enter EXACTLY "yes" to confirm an aircraft for that route. Under any other input, the program will assume otherwise. If you miss an aircraft, use function 7.
You will only be prompted with aircraft currently selected.
If you mistype an airport or airline code, there is currently no way to restore besides manually opening "routes.txt" and changing it yourself. Routes are in alphabetical order by airports.
Change only the characters mistyped, ensuring they are put with the EXACT replacement.
Once done, the route will be stored.

+ 2 - View specific route:
This function lets you view the properties of a specific route. It will ask for 2 airports and an airline. These are to be inputted the same as in function 1.
You will be provided with the route's characteristics.

+ 3 - This function marks a route as completed. You will once again be asked for 2 airports and an airline. It will then ask for the aircraft type completed.
The database will be updated, and the route under that aircraft will be marked as completed.

+ 4 - Inverse of function 3 - un-complete routes.

+ 5 - View all Routes
Similar to function 2, this will provide information for every route available. May cause issues on slower computers, so treat with care.

+ 6 - Filtered Routes
This function displays routes under input filters. These filters are (one) airport, airline and aircraft type.
In the airport section, you may also enter a COUNTRY, CITY or CONTROL position (eg. `Austria`, `London`, `EGLL_N_APP`, `EBBU_W_CTR`), and all airports within these will be selected.
You may either input a value, or `NULL` to disregard that filter. You may use one filter, or any mixture of the three.

+ 7 - Add Aircraft to Route
This function adds an aircraft to an existing route.
You will be asked for the airports and airline as per usual, then the aircraft to be added. The aircraft will be assumed as uncompleted when added.

+ 8 - Add Route Number
This function assigns a route number to an existing route. This lets you track your routes by searching up such numbers.
Multiple numbers can be added per route. To remove a number, manually edit "routenum.txt" and delete its entire line.
This is good to use, as you can search up routes to see if they remain in service. Route numbers will be displayed in viewing functions.

+ 9 - Select Aircraft
This function lets you choose which aircraft you'll be prompted with when adding or viewing routes. These can be changed at any time.

+ 10 - Select Home FIR
Routes will only be displayed if they are to/from your home FIR. Enter `any` to disregard this. Your home FIR can be changed at any time.



### WANT A COMMUNITY TOUCH?

I'm currently working on a way to share your databases and compare with others. This will also allow you to better backup your data, as compared to current.





### For now, it's just me on my own. I'm clueless in all coding aspects, so use with a grain of salt. Have fun :D

### If you want to contribute, uhh, DM me - making my code less inefficient would be nice

