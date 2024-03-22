from __future__ import annotations

from typing import Any, Literal

from fastapi import APIRouter

from src.utils import request_api_with_league

scoring_router = APIRouter(tags=["Scoring And Results"])


@scoring_router.get("/league_standings")
async def league_standings(
    column_names: bool = False,
    all_fields: bool = False,
    web: bool = False,
) -> dict[str, Any]:
    """Get the current standings for the league.

    When `column_names` is specified, returns a mapping of column keys to column names.
    This also shows the proper order of the standings columns.

    When `all_fields` is specified, returns additional standings field values that are
    not part of the league standings report but are important for sorting league
    standings.
    Note that some of these extra fields may not be relevant for all leagues
    and may include duplicate info from the basic set.

    When `web` is specified, returns the columns shown on the web site only.
    This is in case the app wants to just replicate the report from the web site.
    This parameter is ignored if ALL is set.
    """
    return request_api_with_league(
        "leagueStandings",
        COLUMN_NAMES=int(column_names),
        ALL=int(all_fields),
        WEB=int(web),
    )


@scoring_router.get("/weekly_results")
async def weekly_results(
    week: int | Literal["YTD"] | None = None,
    missing_as_bye: bool = False,
) -> dict[str, Any]:
    """Get the weekly results for a league/week.

    This includes the scores for all starter and non-starter players for all franchises
    in a league. The `week` parameter can be "YTD" to give all year-to-date weekly
    results.

    If `missing_as_bye` is specified, fantasy teams with no scheduled opponents will
    be shown as playing vs a BYE opponent.
    """
    return request_api_with_league(
        "weeklyResults",
        W=week,
        MISSING_AS_BYE=int(missing_as_bye),
    )


@scoring_router.get("/live_scoring")
async def live_scoring(
    week: int | None = None,
    details: bool = False,
) -> dict[str, Any]:
    """Get live scoring for a given league and week.

    Includes:
    - Each franchises current score
    - How many game seconds remaining that franchise has
    - players who have yet to play
    - players who are currently playing
    """
    return request_api_with_league("liveScoring", W=week, DETAILS=int(details))


@scoring_router.get("/player_scores")
async def player_scores(
    week: int | Literal["YTD"] | None = None,
    year: int | None = None,
    player: int | None = None,
    positions: str | None = None,
    status: Literal["freeagent"] | None = None,
    rules: bool = False,
    count: int | None = None,
) -> dict[str, Any]:
    """Get all player scores for a given week.

    Includes all rostered players and free agents.
    """
    return request_api_with_league(
        "playerScores",
        W=week,
        YEAR=year,
        PLAYERS=player,
        POSITIONS=positions,
        STATUS=status,
        RULES=int(rules),
        COUNT=count,
    )


@scoring_router.get("/projected_scores")
async def projected_scores(
    week: int | None = None,
    year: int | None = None,
    player: int | None = None,
    positions: str | None = None,
    status: Literal["freeagent"] | None = None,
    rules: bool = False,
    count: int | None = None,
) -> dict[str, Any]:
    """Get calculation of expected fantasy points, using the league's scoring system."""
    return request_api_with_league(
        "projectedScores",
        W=week,
        YEAR=year,
        PLAYERS=player,
        POSITIONS=positions,
        STATUS=status,
        RULES=int(rules),
        COUNT=count,
    )
