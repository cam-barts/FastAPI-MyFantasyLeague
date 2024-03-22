from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from src.utils import request_api_with_league

common_info_router = APIRouter(tags=["Common League Info"])


@common_info_router.get("/league")
async def league() -> dict[str, Any]:
    """Get general league setup parameters for a given league.

    Response includes:
    - league name
    - roster size
    - IR/TS size
    - starting and ending week
    - starting lineup requirements
    - franchise names
    - division names
    """
    return request_api_with_league("league")


@common_info_router.get("/rules")
async def rules() -> dict[str, Any]:
    """Get league scoring rules for a given league."""
    return request_api_with_league("rules")


@common_info_router.get("/rosters")
async def rosters(
    week: int | None = None,
    franchise_id: int | None = None,
) -> dict[str, Any]:
    """Get the current rosters.

    When `franchise_id` is specified, the response will include the
    current roster of just the specified franchise.

    When `week` is specified, it returns the roster for that week.
    The week must be less than or equal to the upcoming week.
    Changes to salary and contract info is not tracked so those fields (if used)
    always show the current values.
    """
    return request_api_with_league("rosters", W=week, FRANCHISE=franchise_id)


@common_info_router.get("/free_agents")
async def free_agents(position: str | None = None) -> dict[str, Any]:
    """Get fantasy free agents.

    When `position` is specified, return only players from that position.
    """
    # TODO: turn position into an enum for easier access in frontend.
    return request_api_with_league("freeAgents", POSITION=position)


@common_info_router.get("/schedule")
async def schedule(
    week: int | None = None,
    franchise_id: int | None = None,
) -> dict[str, Any]:
    """Get the fantasy schedule.

    When `franchise_id` is specified, the response will include the
    schedule of just the specified franchise.

    When `week` is specified, it returns the schedule for that week.
    """
    return request_api_with_league("schedule", W=week, FRANCHISE=franchise_id)


@common_info_router.get("/calendar")
async def calendar() -> dict[str, Any]:
    """Get summary of league calendar events."""
    return request_api_with_league("calendar")


@common_info_router.get("/playoff_brackets")
async def playoff_brackets() -> dict[str, Any]:
    """Get all playoff brackets for a given league."""
    return request_api_with_league("playoffBrackets")


@common_info_router.get("/playoff_bracket")
async def playoff_bracket(bracket_id: int | None = None) -> dict[str, Any]:
    """Get the games (with results if available) of the specified playoff bracket."""
    return request_api_with_league("playoffBracket", BRACKET_ID=bracket_id)
