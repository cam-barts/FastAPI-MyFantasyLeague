from __future__ import annotations

import datetime
from enum import Enum
from typing import Any, Literal

from fastapi import APIRouter

from src.utils import request_api_data, request_api_with_league

fantasy_router = APIRouter(tags=["Fantasy Content"])


class Period(str, Enum):
    """Valid periods."""

    all = "ALL"
    recent = "RECENT"
    draft = "DRAFT"
    june = "JUNE"
    july = "JULY"
    aug = "AUG1"
    aug_15 = "AUG15"
    start = "START"
    mid = "MID"
    playoff = "PLAYOFF"


@fantasy_router.get("/players")
async def get_players(
    details: bool = False,
    since: datetime.datetime | None = datetime.datetime.now(  # noqa: B008
        tz=datetime.UTC,
    ),
    player_id: int | None = None,
) -> dict[str, Any]:
    """Get all player IDs, names, and positions.

    If `since` is specified, retrieve only changes to the player database since that
    time.
    """
    if since:
        timestamp = int(since.timestamp())
        return request_api_with_league(
            "players",
            DETAILS=int(details),
            SINCE=timestamp,
            PLAYERS=player_id,
        )

    return request_api_with_league(
        "players",
        DETAILS=int(details),
        PLAYERS=player_id,
    )


@fantasy_router.get("/player_profile")
async def get_player_profile(
    player_id: int,
) -> dict[str, Any]:
    """Get a player profile summary."""
    return request_api_data(
        "playerProfile",
        P=player_id,
    )


@fantasy_router.get("/all_rules")
async def get_all_rules() -> dict[str, Any]:
    """Get all scoring rules."""
    return request_api_data("allRules")


@fantasy_router.get("/player_ranks")
async def get_player_ranks(
    position: str | None = None,
) -> dict[str, Any]:
    """Get player rankings from experts at FantasySharks.com."""
    return request_api_data("playerRanks", POS=position)


@fantasy_router.get("/adp")
async def get_adp(
    period: Period = Period.all,
    fcount: int | None = None,
    is_ppr: bool | None = None,
    is_keeper: str = "NKR",
    is_mock: bool | None = None,
    cutoff: int | None = None,
    details: bool = False,
) -> dict[str, Any]:
    """Get ADP results."""
    return request_api_data(
        "adp",
        PERIOD=period,
        FCOUNT=fcount,
        IS_PPR=int(is_ppr) if is_ppr else None,
        IS_KEEPER=is_keeper,
        IS_MOCK=int(is_mock) if is_mock else None,
        CUTOFF=cutoff,
        DETAILS=int(details),
    )


@fantasy_router.get("/aav")
async def get_aav(
    period: Period = Period.all,
    is_ppr: bool | None = None,
    is_keeper: str = "NKR",
) -> dict[str, Any]:
    """Get AAV results."""
    return request_api_data(
        "aav",
        PERIOD=period,
        IS_PPR=int(is_ppr) if is_ppr else None,
        IS_KEEPER=is_keeper,
    )


@fantasy_router.get("/top_adds")
async def get_top_adds(
    count: int | None = None,
    status: Literal["FA"] | None = None,
) -> dict[str, Any]:
    """Get the most added players."""
    return request_api_data("topAdds", COUNT=count, STATUS=status)


@fantasy_router.get("/top_drops")
async def get_top_drops(
    count: int | None = None,
    status: Literal["FA"] | None = None,
) -> dict[str, Any]:
    """Get the most dropped players."""
    return request_api_data("topDrops", COUNT=count, STATUS=status)


@fantasy_router.get("/top_starters")
async def get_top_starters(
    count: int | None = None,
    status: Literal["FA"] | None = None,
) -> dict[str, Any]:
    """Get the most started players."""
    return request_api_data("topStarters", COUNT=count, STATUS=status)


@fantasy_router.get("/top_trades")
async def get_top_trades(
    count: int | None = None,
) -> dict[str, Any]:
    """Get the most traded players."""
    return request_api_data("topTrades", COUNT=count)


@fantasy_router.get("/top_owns")
async def get_top_owns(
    count: int | None = None,
    status: Literal["FA"] | None = None,
) -> dict[str, Any]:
    """Get the most owned players."""
    return request_api_data("topOwns", COUNT=count, STATUS=status)


@fantasy_router.get("/who_should_i_start")
async def who_should_i_start(
    league_id: int | None = None,
    week: int | None = None,
    franchise: int | None = None,
) -> dict[str, Any]:
    """Get 'Who Should I Start?' data."""
    return request_api_with_league(
        "whoShouldIStart",
        L=league_id,
        WEEK=week,
        FRANCHISE=franchise,
    )
