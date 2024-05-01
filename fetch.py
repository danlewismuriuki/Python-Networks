import urllib.request

# Open a conection to the URL
response = urllib.request.urlopen('https://www.bonfireadventures.com/')
# Read the data from the response
data = response.read()
# Decoded the data if necessary
decoded_data = data.decode('utf-8')
# Print the fetched data
print(decoded_data)