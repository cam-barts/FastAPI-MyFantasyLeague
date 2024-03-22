from __future__ import annotations

from enum import Enum
from typing import Any

from fastapi import APIRouter

from src.utils import request_api_with_league

other_info_router = APIRouter(tags=["Other League Info"])


class PoolType(str, Enum):
    nfl = "NFL"
    fantasy = "Fantasy"


@other_info_router.get("/future_draft_picks")
async def future_draft_picks() -> dict[str, Any]:
    """Get future draft picks for a given league."""
    return request_api_with_league("futureDraftPicks")


@other_info_router.get("/accounting")
async def accounting() -> dict[str, Any]:
    """Get summary of league accounting records.

    In the response, negative amounts are charges against the franchise while positive
    amounts is money paid by the franchise or owed to the franchise.
    """
    return request_api_with_league("accounting")


@other_info_router.get("/pool")
async def pool(pool_type: PoolType = PoolType.nfl) -> dict[str, Any]:
    """Get all NFL or Fantasy picks for a given league."""
    return request_api_with_league("pool", POOLTYPE=pool_type)


@other_info_router.get("/survivor_pool")
async def survivor_pool() -> dict[str, Any]:
    """Get all survivor pool picks for a given league."""
    return request_api_with_league("survivorPool")


@other_info_router.get("/abilities")
async def abilities(
    franchise_id: int | None = None,
    details: bool = False,
) -> dict[str, Any]:
    """Get the abilities of the current franchise."""
    return request_api_with_league(
        "abilities",
        F=franchise_id,
        DETAILS=int(details),
    )
