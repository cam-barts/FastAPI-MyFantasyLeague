from __future__ import annotations

from enum import Enum
from typing import Any

from fastapi import APIRouter

from src.utils import request_api_with_league

transactions_router = APIRouter(tags=["Transactions"])


class TransactionType(str, Enum):
    """Available transaction types."""

    default = "DEFAULT"
    waiver = "WAIVER"
    bbid_waiver = "BBID_WAIVER"
    free_agent = "FREE_AGENT"
    waiver_request = "WAIVER_REQUEST"
    bbid_waiver_request = "BBID_WAIVER_REQUEST"
    trade = "TRADE"
    ir = "IR"
    taxi = "TAXI"
    auction_init = "AUCTION_INIT"
    auction_bid = "AUCTION_BID"
    auction_won = "AUCTION_WON"
    survivor_pick = "SURVIVOR_PICK"
    pool_pick = "POOL_PICK"
    all = "*"


@transactions_router.get("/transactions")
async def transactions(
    transaction_type: TransactionType,
    week: int | None = None,
    franchise_id: int | None = None,
    days: int | None = None,
    count: int | None = None,
) -> dict[str, Any]:
    """Get all non-pending transactions for a given league.

    Note that this can be a very large set, so it's recommended that you filter
    the result using one or more of the available parameters.
    """
    return request_api_with_league(
        "transactions",
        W=week,
        TRANS_TYPE=transaction_type,
        FRANCHISE=franchise_id,
        DAYS=days,
        COUNT=count,
    )


@transactions_router.get("/pending_waivers")
async def pending_waivers(franchise_id: int | None = None) -> dict[str, Any]:
    """Get pending unprocessed waivers that the current franchise has submitted."""
    return request_api_with_league(
        "pendingWaivers",
        FRANCHISE_ID=franchise_id,
    )


@transactions_router.get("/pending_trades")
async def pending_trades(franchise_id: int | None = None) -> dict[str, Any]:
    """Get pending trades for this franchise.

    Pass in '0000' to `franchise_id` to get trades pending commissioner action.
    """
    return request_api_with_league(
        "pendingTrades",
        FRANCHISE_ID=franchise_id,
    )


@transactions_router.get("/trade_bait")
async def trade_bait(
    include_draft_picks: bool = False,
) -> dict[str, Any]:
    """Get the Trade Bait for all franchises in a league.

    When `include_draft_picks` set, this will also return draft picks offered.
    Current year draft picks look like DP_02_05 which refers to the 3rd round 6th pick
    (the round and pick values in the string are one less than the actual round/pick).

    For future years picks, they are identified like FP_0005_2018_2 where 0005 referes
    to the franchise id who originally owns the draft pick, then the year and then the
    round (in this case the rounds are the actual rounds, not one less). This also
    includes Blind Bid dollars (in leagues that use them), which will be specified as
    BB_10 to indicate $10 in blind bid dollars.
    """
    if include_draft_picks:
        return request_api_with_league("tradeBait", INCLUDE_DRAFT_PICKS=1)
    return request_api_with_league("tradeBait")


@transactions_router.get("/assets")
async def assets() -> dict[str, Any]:
    """Get all tradable assets for a given league.

    This includes:
    - players
    - current year draft picks
    - future draft picks
    """
    return request_api_with_league("assets")
