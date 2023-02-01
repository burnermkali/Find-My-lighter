import geoip2.database

# Create a reader object
reader = geoip2.database.Reader('path/to/GeoLite2-City.mmdb')

# Get the location information for an IP address
response = reader.city('8.8.8.8')

# Extract the location information
city = response.city.name
country = response.country.name
latitude = response.location.latitude
longitude = response.location.longitude

# Print the location information
print('City:', city)
print('Country:', country)
print('Latitude:', latitude)
print('Longitude:', longitude)
