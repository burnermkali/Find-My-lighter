# Find-My-lighter
using python to track devices via IPV4 

ruby
Copy code
# Documentation for geolocation script using MaxMind GeoIP2 library

## Importing the library
The first line of the code imports the `geoip2.database` module from the MaxMind GeoIP2 library.



import geoip2.database

vbnet
Copy code

## Creating a reader object
The next step is to create a `reader` object by calling the `geoip2.database.Reader` function and passing the path to the MaxMind GeoLite2-City database as a parameter. The `reader` object will be used to retrieve location information for an IP address.


Create a reader object

reader = geoip2.database.Reader('path/to/GeoLite2-City.mmdb')

css
Copy code

## Retrieving location information
The code then calls the `reader.city` method, passing the IP address as a parameter. The method returns a `response` object that contains the location information for the IP address.


Get the location information for an IP address

response = reader.city('8.8.8.8')

python
Copy code

## Extracting location information
Next, the code extracts the relevant location information from the `response` object and stores it in variables. The location information includes the city name, country name, latitude, and longitude.


Extract the location information

city = response.city.name
country = response.country.name
latitude = response.location.latitude
longitude = response.location.longitude

shell
Copy code

## Printing the location information
Finally, the code prints the location information to the console.


Print the location information

print('City:', city)
print('Country:', country)
print('Latitude:', latitude)
print('Longitude:', longitude)

css
Copy code

This script uses the MaxMind GeoIP2 library to retrieve the location information for an IP address. The location information includes the city name, country name, latitude, and longitude. The script imports the `geoip2.database` module, creates a `reader` object using the MaxMind GeoLite2-City database, retrieves the location information for an IP address, extracts the relevant location information, and prints the location information to the console.
