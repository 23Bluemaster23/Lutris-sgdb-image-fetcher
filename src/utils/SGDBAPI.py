import requests

from utils.Config import get_config


__api_key = get_config("FETCHING", "api_key")


def get_games_search(search: str):
    res = requests.get(
        f"https://www.steamgriddb.com/api/v2/search/autocomplete/{search}",
        headers={"Authorization": f"Bearer {__api_key}"},
    )
    return res.json()["data"]


def get_game_coverart(id: int):
    res = requests.get(
        f"https://www.steamgriddb.com/api/v2/grids/game/{id}",
        headers={"Authorization": f"Bearer {__api_key}"},
        params={"dimensions": "600x900", "limit": "12"},
    )
    return res.json()["data"]


def get_game_banner(id: int):
    res = requests.get(
        f"https://www.steamgriddb.com/api/v2/grids/game/{id}",
        headers={"Authorization": f"Bearer {__api_key}"},
        params={"dimensions": "460x215,920x430", "limit": "12"},
    )
    if len(res.json()["data"]) > 0:
        return res.json()["data"]
    res = requests.get(
        f"https://www.steamgriddb.com/api/v2/grids/game/{id}",
        headers={"Authorization": f"Bearer {__api_key}"},
        params={"dimensions": "460x215", "limit": "12"},
    )


def get_game_icon(id: int):
    res = requests.get(
        f"https://www.steamgriddb.com/api/v2/icons/game/{id}",
        headers={"Authorization": f"Bearer {__api_key}"},
        params={"limit": "12"},
    )
    if len(res.json()["data"]) > 0:
        return res.json()["data"]
