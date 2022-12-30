# Date: December 9, 2022
# CompSci 1026A-003 - Assignment #4
# Name: Andrew Zhang
# This is a class that handles and processes the flight aspect of handling flights
from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):
        # Check if the `origin` and `destination` arguments are of type `Airport`
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            # If they are, store the flight number and origin and destination airports
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            # If they are not, raise a `TypeError`
            raise TypeError("The origin and destination must be Airport Objects")

    def __repr__(self):
        # Check if the flight is a domestic flight
        if self.isDomesticFlight() == True:
            isDomesticFlight = "domestic"
        else:
            isDomesticFlight = "international"
        # Return a string representation of the flight
        return "Flight:{} from {} to {} {}".format(self._flightNo, self._origin.getCity(), self._destination.getCity(), "{" + isDomesticFlight + "}")

    def __eq__(self, other):
        # Check if the origin and destination of the current flight and the given flight are the same
        if self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination():
            # If they are, return `True`
            return True
        else:
            # If they are not, return `False`
            return False

    def getFlightNumber(self):
        # Return the flight number of the flight
        return self._flightNo

    def getOrigin(self):
        # Return the origin airport of the flight
        return self._origin

    def getDestination(self):
        # Return the destination airport of the flight
        return self._destination

    def isDomesticFlight(self):
        # Check if the origin and destination airports of the flight are in the same country
        if self._origin.getCountry() == self._destination.getCountry():
            # If they are, return `True`
            return True
        else:
            # If they are not, return `False`
            return False

    def setOrigin(self, newOrigin):
        # Set the origin airport of the flight to the given airport
        self._origin = newOrigin

    def setDestination(self, newDestination):
        # Set the destination airport of the flight to the given airport
        self._destination = newDestination
