import requests


def downloader(url):
    pass


def check_internet_connection(queue):
    url = "https://www.wikipedia.org/"
    try:
        response = requests.get(url)
        result = f"HTTP STATUS : {response.status_code} | Connection established"
        queue.put(result)
    except requests.exceptions.ConnectionError:
        queue.put("No internet connection")
