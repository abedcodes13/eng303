import requests
from bs4 import BeautifulSoup

# URL of the article
url = "https://www.sciencedirect.com/science/article/pii/S0022169417308259?via%3Dihub"

# Make a GET request to fetch the raw HTML content
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")


print(soup)
