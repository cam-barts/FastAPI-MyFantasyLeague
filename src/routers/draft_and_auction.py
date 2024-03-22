from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from src.utils import request_api_with_league

draft_auction_router = APIRouter(tags=["Draft And Auction"])


@draft_auction_router.get("/draft_results")
async def draft_results() -> dict[str, Any]:
    """Get draft results for a given league.

    Note that this data may be up to 15 minutes delayed as it is meant to display draft
    results after a draft is completed.
    """
    return request_api_with_league("draftResults")


@draft_auction_router.get("/auction_results")
async def auction_results() -> dict[str, Any]:
    """Get auction results for a given league."""
    return request_api_with_league("auctionResults")


@draft_auction_router.get("/selected_keepers")
async def selected_keepers(franchise_id: int | None = None) -> dict[str, Any]:
    """Get currently selected keepers."""
    return request_api_with_league("selectedKeepers", FRANCHISE=franchise_id)


@draft_auction_router.get("/my_draft_list")
async def my_draft_list() -> dict[str, Any]:
    """Get My Draft List."""
    return request_api_with_league("myDraftList")
