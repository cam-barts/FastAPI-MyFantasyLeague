from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from src.utils import request_api_with_league

communications_router = APIRouter(tags=["Communications"])


@communications_router.get("/message_board")
async def message_board(count: int = 10) -> dict[str, Any]:
    """Get summary of recent message board posts."""
    return request_api_with_league("messageBoard", COUNT=count)


@communications_router.get("/message_board_thread/{thread_id}")
async def message_board_thread(thread_id: int) -> dict[str, Any]:
    """Display posts in a thread from a league message board."""
    return request_api_with_league("messageBoardThread", THREAD_ID=thread_id)


@communications_router.get("/polls")
async def polls() -> dict[str, Any]:
    """Get all current league polls."""
    return request_api_with_league("polls")
