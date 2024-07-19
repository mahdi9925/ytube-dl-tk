import requests


def downloader(url):
    pass


def check_internet_connection(queue):
    url = "https://www.google.com/"
    try:
        response = requests.get(url)
        result = f"HTTP STATUS : {response.status_code} | Connection established"
        # print(result)
        queue.put(result)
    except requests.exceptions.ConnectionError:
        queue.put("No internet connection")
