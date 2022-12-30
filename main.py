
# Date: December 9, 2022
# CompSci 1026A-003 - Assignment #4
# Name: Andrew Zhang
# This is a program that handles flights based on airport codes, city of airport, country of airport, flight codes, flight origin, and flight destination
from Flight import *
from Airport import *

allAirports = {}
allFlights = {}
def loadData(airportFile,flightFile):
        # Try to open and read the given files
        try:
            # Open the airport file in read-only mode
            with open(airportFile, 'r', encoding="utf8") as f:
                # Loop through each line in the file
                for line in f:
                    # Split the line on the comma character to get a list of values
                    values = line.split(",")
                    # Check if the line has the correct number of values (3)
                    if len(values) == 3:
                        # Create an airport object using the values
                        airport = Airport(values[0].strip().lstrip(), values[2].strip().lstrip(),
                                          values[1].strip().lstrip())
                        # Add the airport to the `allAirports` dictionary using the code as the key
                        allAirports[values[0].strip()] = airport

            # Open the flight file in read-only mode
            with open(flightFile, 'r', encoding="utf8") as f:
                # Loop through each line in the file
                for line in f:
                    # Split the line on the comma character to get a list of values
                    values = line.split(",")
                    # Check if the line has the correct number of values (3)
                    if len(values) == 3:
                        # Get the origin and destination airports from the `allAirports` dictionary using the codes from the file
                        origin = allAirports[values[1].strip()]
                        destination = allAirports[values[2].strip()]
                        # Create a flight object using the values from the file and the origin and destination airports
                        flight = Flight(values[0].strip().lstrip(), origin, destination)
                        # If the origin airport is not in the `allFlights` dictionary, add it as a key and set the value to a list containing the flight
                        if values[1].strip() not in allFlights:
                            allFlights[values[1].strip()] = [flight]
                        else:
                            # If the origin airport is already in the `allFlights` dictionary, append the flight to the list of flights for that airport
                            allFlights[values[1].strip()].append(flight)
            # Return `True` to indicate that the data was loaded successfully
            return True

        # If an IOError occurs while reading the files, return `False` to indicate that the data was not loaded
        except IOError:
            return False

def getAirportByCode(code):
    # Loop through the keys in the `allAirports` dictionary
    for airport_code in allAirports:
        # If the given code is in the dictionary, return the airport object with that code
        if code == airport_code:
            return allAirports[code]
    # If the given code is not in the dictionary, return -1
    return -1


def findAllCityFlights(city):
    # Create an empty list to hold the flights that originate or destination in the given city
    city_flights = []

    # Loop through the airport objects in the `allAirports` dictionary
    for airport in allAirports.values():
        # If the city of the current airport matches the given city, get the code for the airport
        if airport.getCity() == city:
            code = airport.getCode()

            # Loop through the flights that originate at the airport with the given city
            for f in allFlights[code]:
                # Add the flight to the list of flights for the city
                city_flights.append(f)

            # Loop through the keys (origin airport codes) in the `allFlights` dictionary
            for origin_code in allFlights.keys():
                # Loop through the flights that originate at the current origin airport
                for flights in allFlights[origin_code]:
                    # If the code for the airport with the given city is in the destination code for the current flight, add the flight to the list of flights for the city
                    if str(code) in str(flights.getDestination()):
                        city_flights.append(flights)
    # Return the list of flights for the city
    return city_flights

def findAllCountryFlights(country):
    # Create an empty list to hold the flights that originate or have a destination in the given country
    country_flights = []

    # Loop through the airport objects in the `allAirports` dictionary
    for airport in allAirports.values():
        # If the country of the current airport matches the given country, get the code for the airport
        if airport.getCountry() == country:
            code = airport.getCode()

            # Loop through the flights that originate at the airport with the given country
            for f in allFlights[code]:
                # Add the flight to the list of flights for the country
                country_flights.append(f)

            # Loop through the keys (origin airport codes) in the `allFlights` dictionary
            for origin_code in allFlights.keys():
                # Loop through the flights that originate at the current origin airport
                for flights in allFlights[origin_code]:
                    # If the code for the airport with the given country is in the destination code for the current flight, add the flight to the list of flights for the country
                    if str(code) in str(flights.getDestination()):
                        country_flights.append(flights)
    # Return the list of flights for the country
    return country_flights

def findFlightBetween(origAirport, destAirport):
    # Create an empty set to hold the codes for airports that can be used as a stopover for a one-hop flight between the given airports
    singleHop = set()

    # Loop through the values (lists of flights) in the `allFlights` dictionary
    for flights in allFlights.values():
        # Loop through the flights in the current list of flights
        for flight in flights:
            # If the origin of the current flight is the given origin airport and the destination is the given destination airport, return a string indicating a direct flight between the two airports
            if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
                return 'Direct Flight: {} to {}'.format(str(flight.getOrigin().getCode()), str(flight.getDestination().getCode()))

            # If the origin of the current flight is the given origin airport, loop through the values (lists of flights) in the `allFlights` dictionary again to find a one-hop flight
            elif flight.getOrigin() == origAirport:
                for flights2 in allFlights.values():
                    for flight2 in flights2:
                        # If the origin of the current flight is the destination of the first flight and the destination of the current flight is the given destination airport, add the code for the destination airport of the first flight to the set of stopover airports
                        if flight2.getOrigin() == flight.getDestination() and flight2.getDestination() == destAirport:
                            singleHop.add(str(flight.getDestination().getCode()))

    # If the set of stopover airports is not empty, return the set of stopover airports
    if len(singleHop) > 0:
        return singleHop
    # If the set of stopover airports is empty, return -1
    else:
        return -1

def findDirectFlight(origin, destination):
    # Loop over the values in the allFlights dictionary
    for flights in allFlights.values():
        # Loop over the individual flights in the flights list
        for flight in flights:
            # Check if there is a direct flight between the origin and destination airports
            if flight.getOrigin() == origin and flight.getDestination() == destination:
                return flight

    # Return None if no direct flight was found
    return -1


def findReturnFlight(firstFlight):
    # Get the origin and destination codes for the first flight
    origin_code = firstFlight.getOrigin().getCode()
    destination_code = firstFlight.getDestination().getCode()

    # Loop over the values in the allFlights dictionary
    for flights in allFlights.values():
        # Loop over the individual flights in the flights list
        for flight in flights:
            # Check if there is a direct flight between the origin and destination airports
            if flight.getOrigin().getCode() == destination_code and flight.getDestination().getCode() == origin_code:
                return flight

    # Return None if no return flight was found
    return -1
