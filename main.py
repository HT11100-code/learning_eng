import requests
from bs4 import BeautifulSoup

def extract_word():
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")





if __name__ == "__main__":
    url = input("enter the url")
    extract_word(url)
