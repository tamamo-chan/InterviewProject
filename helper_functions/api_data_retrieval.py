import requests

url = "https://d16m5wbro86fg2.cloudfront.net"


def get_all_users():
    endpoint = "/api/users"
    return requests.get(url + endpoint).json()


def get_user_summary(username: str) -> dict:
    endpoint = "/api/user/by-username/"
    return requests.get(url + endpoint + username).json()


def get_user_full_data(user_id: str) -> dict:
    endpoint = "/api/user/by-id/"
    return requests.get(url + endpoint + user_id).json()


def get_all_sets() -> dict:
    endpoint = "/api/sets"
    return requests.get(url + endpoint).json()


def get_set_summary(set_name: str) -> dict:
    endpoint = "/api/set/by-name/"
    return requests.get(url + endpoint + set_name).json()


def get_set_full_data(set_id: str) -> dict:
    endpoint = "/api/set/by-id/"
    return requests.get(url + endpoint + set_id).json()
