import requests
"Needed to use request to grab webpage"

from bs4 import BeautifulSoup
"Needed for the soup command to parser webpage"

url = 'http://cnn.com'
response = requests.get(url)
"Grabs the cnn.com webpage"

soup = BeautifulSoup(response.text, "html.parser")
"Parsers the webpage"

print(soup.get_text())
"Prints just the text from the webpage"


