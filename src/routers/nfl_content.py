from __future__ import annotations

from typing import Any, Literal

import requests
from fastapi import APIRouter

from src.utils import request_api_with_league

nfl_router = APIRouter(tags=["NFL Content"])


def request_nfl_data(
    request_type: str,
    **kwargs: Any,  # noqa: ANN401 **kwargs can be of any type
) -> dict[str, Any]:
    """Make a request to the league api endpoint."""
    params = {
        "JSON": 1,
        "TYPE": request_type,
    }
    if kwargs:
        params.update(kwargs)
    host = "https://api.myfantasyleague.com/2024/export"
    resp = requests.get(host, timeout=10, params=params)
    return resp.json()


@nfl_router.get("/injuries")
async def get_injuries(
    week: int | None = None,
) -> dict[str, Any]:
    """Get NFL injuries report."""
    return request_nfl_data(
        "injuries",
        W=week,
    )


@nfl_router.get("/nfl_schedule")
async def get_nfl_schedule(
    week: int | Literal["ALL"] | None = None,
) -> dict[str, Any]:
    """Get NFL schedule for a week or the full season."""
    return request_nfl_data(
        "nflSchedule",
        W=week,
    )


@nfl_router.get("/nfl_bye_weeks")
async def get_nfl_bye_weeks(
    week: int | None = None,
) -> dict[str, Any]:
    """Get bye weeks for all NFL teams or for teams with a bye in a specified week."""
    return request_nfl_data(
        "nflByeWeeks",
        W=week,
    )


@nfl_router.get("/points_allowed")
async def get_points_allowed() -> dict[str, Any]:
    """Get fantasy points allowed by each NFL team, broken out by position."""
    return request_api_with_league(
        "pointsAllowed",
    )
