from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import random
import asyncio

mock_router = APIRouter()

@mock_router.websocket("/dev/host/ws")
async def host(ws: WebSocket):    
    await ws.accept()

    host_ws = ws
    
    await ws.send_json({
        "game_id": "aaaaaaaa"
    })

    player_1_pos = 500
    player_2_pos = 500

    while True:
        try:
            player_1_pos += random.random() * 100 - 50
            player_2_pos += random.random() * 100 - 50

            player_1_pos = max(min(player_1_pos, 1000), 0)
            player_2_pos = max(min(player_2_pos, 1000), 0)

            if host_ws is not None:
                await host_ws.send_json({
                    "player_1": player_1_pos,
                    "player_2": player_2_pos,
                })

            await asyncio.sleep(1/64)
        except:
            return
