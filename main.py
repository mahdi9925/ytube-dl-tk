import requests

# ? This function is for download files
def downloader(url):
    pass

# ? This function is for check internet connectivity and if there is an error it will be shown
def check_internet_connection(queue):
    url = "https://www.google.com/"
    try:
        response = requests.get(url)
        result = f"HTTP STATUS : {response.status_code} | Connection established"
        # print(result)
        queue.put(result)
    except requests.exceptions.ConnectionError:
        queue.put("No internet connection")
