from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import random
import asyncio

mock_router = APIRouter()

@mock_router.websocket("/dev/host/ws")
async def host(ws: WebSocket):    
    await ws.accept()

    host_ws = ws

    player_1_pos = 50
    player_2_pos = 50

    while True:
        try:
            player_1_pos += random.random() * 10 - 5
            player_2_pos += random.random() * 10 - 5

            player_1_pos = max(min(player_1_pos, 100), 0)
            player_2_pos = max(min(player_2_pos, 100), 0)

            if host_ws is not None:
                await host_ws.send_json({
                    "game_id": "aaaaaaaa",
                    "player_1": player_1_pos,
                    "player_2": player_2_pos,
                })

            await asyncio.sleep(1/2)
        except:
            return
