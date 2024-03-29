import requests


def downloader(url):
    pass


def check_internet_connection():
    url = "https://google.com"
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.ConnectionError:
        return "No internet connection"


n = check_internet_connection()
print(n)
