from __future__ import annotations

from fastapi import FastAPI

from src.routers.common_info import common_info_router
from src.routers.communications import communications_router
from src.routers.draft_and_auction import draft_auction_router
from src.routers.fantasy_content import fantasy_router
from src.routers.league_players import players_router
from src.routers.nfl_content import nfl_router
from src.routers.other_league_info import other_info_router
from src.routers.scoring_and_results import scoring_router
from src.routers.transactions import transactions_router
from src.routers.user_functions import user_router

app = FastAPI()

app.include_router(common_info_router)
app.include_router(transactions_router)
app.include_router(scoring_router)
app.include_router(draft_auction_router)
app.include_router(communications_router)
app.include_router(players_router)
app.include_router(other_info_router)
app.include_router(user_router)
app.include_router(fantasy_router)
app.include_router(nfl_router)
