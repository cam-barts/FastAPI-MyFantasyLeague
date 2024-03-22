from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from src.utils import request_api_with_league

players_router = APIRouter(tags=["League Players"])


@players_router.get("/player_roster_status")
async def player_roster_status(
    player_id: int | None = None,
    week: int | None = None,
    franchise_id: int | None = None,
) -> dict[str, Any]:
    """Get the player's current roster status.

    The franchise(s) the player is on are listed in the subelement. There may more than
    one of this for leagues that have multiple copies of players. Each of this elements
    will have a franchise id and status attribute. The status attribute can be one of:
    R (roster), S (starter), NS (non-starter), IR (injured reserve) or TS (taxi squad).
    The R value is only provided when there's no lineup submitted or the caller has no
    visibility into the lineup. If the player is a free agent, there will be a 'is_fa'
    attribute on the parent element. In those cases the elements 'cant_add' and
    'locked' attributes may be set indicating whether a player can't be added or is
    locked.
    """
    return request_api_with_league(
        "playerRosterStatus",
        P=player_id,
        W=week,
        F=franchise_id,
    )


@players_router.get("/my_watch_list")
async def my_watch_list() -> dict[str, Any]:
    """Get My Watch List."""
    return request_api_with_league("myWatchList")


@players_router.get("/contest_players")
async def contest_players(
    week: int | None = None,
    franchise_id: int | None = None,
) -> dict[str, Any]:
    """Get eligible players to be in franchise's starting lineup for Contest Leagues.

    While this request can be used by any league it's best suited for leagues with the
    loadRosters setting set to either 'contest' or 'setem'.
    """
    return request_api_with_league("contestPlayers", W=week, F=franchise_id)


@players_router.get("/salaries")
async def salaries() -> dict[str, Any]:
    """Get the current player salaries and contract fields.

    Only players with values are returned. If a value is empty it means that the
    default value is in effect.

    The default values are specified under the player id '0000'.
    """
    return request_api_with_league("salaries")


@players_router.get("/salary_adjustments")
async def salary_adjustments() -> dict[str, Any]:
    """Get all extra salary adjustments for a given league."""
    return request_api_with_league("salaryAdjustments")
