from __future__ import annotations

from functools import partial
from typing import Any

import requests
from decouple import config

API_KEY: str = config("MYFANTASYLEAGUE_API_KEY")
LEAGUE_ID: int = config("MYFANTASYLEAGUE_LEAGUE_ID")


def request_api_data(
    request_type: str,
    **kwargs: Any,  # noqa: ANN401 **kwargs can be of any type
) -> dict[str, Any]:
    """Make a request to the league api endpoint.

    For the purposes of this application, we will only make requests to the API via
    an APIKEY parameter for simplicity, and we will only ever want JSON back instead of
    xml. This is a helper function to make those calls to the api. Eventually, to save
    the number of API calls, this function will likely also wrap some caching
    in an external store like redis.
    """
    params = {
        "APIKEY": API_KEY,
        "JSON": 1,
        "TYPE": request_type,
    }
    if kwargs:
        params.update(kwargs)
    host = "https://www44.myfantasyleague.com/2024/export"
    resp = requests.get(host, timeout=10, params=params)
    return resp.json()


# This partial is to just reduce some of the redundancy with calls to the fantasy api,
# as many of them require a league. For the purposes of this app, the user will
# generally only belong to the one league, so this is just adding an extra parameter to
# the above function.
request_api_with_league = partial(
    request_api_data,
    L=LEAGUE_ID,
)
