# Date: December 9, 2022
# CompSci 1026A-003 - Assignment #4
# Name: Andrew Zhang
# This is a class that handles and processes the airport aspect of handling flights
class Airport:
    def __init__(self, code, city, country):
        # Store the code, city, and country for the airport
        self.code = code
        self.city = city
        self.country = country

    def __repr__(self):
        # Return a string representation of the airport in the format "CODE (CITY, COUNTRY)"
        return '{} ({}, {})'.format(self.code.upper(), self.city.title(), self.country.title())

    def getCode(self):
        # Return the code of the airport
        return self.code

    def getCity(self):
        # Return the city where the airport is located
        return self.city

    def getCountry(self):
        # Return the country where the airport is located
        return self.country

    def setCity(self, newCity):
        # Set the city where the airport is located to the given city
        self.city = newCity

    def setCountry(self, newCountry):
        # Set the country where the airport is located to the given country
        self.country = newCountry
