from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from src.utils import request_api_data

user_router = APIRouter(tags=["User Functions"])


@user_router.get("/my_leagues")
async def my_leagues(
    year: int | None = None,
    names: bool = False,
) -> dict[str, Any]:
    """Get all the leagues of the current user."""
    return request_api_data("myLeagues", YEAR=year, FRANCHISE_NAMES=int(names))


@user_router.get("/league_search")
async def league_search(
    search_term: str | None,
    league_id: int | None,
    year: int | None,
) -> dict[str, Any]:
    """Search for leagues that match `league_id` or `search_term`.

    Either `league_id` or `search_term` must be specified, but not both.
    """
    return request_api_data(
        "leagueSearch",
        SEARCH=search_term,
        ID=league_id,
        YEAR=year,
    )
