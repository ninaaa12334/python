import requests

url="https://www.wikipidia.org"

try:
    response =requests.get(url)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.TimeoutError as timeout_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.TimeoutError as timeout_err:
    print(f"Connection error occurred: {conn_err}")


