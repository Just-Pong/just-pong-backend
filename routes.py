from fastapi import APIRouter, WebSocket
import json

from game_manager import GameManager

router = APIRouter()
gameManager = GameManager()


@router.websocket("/game/host/ws")
async def host(ws: WebSocket):
    await ws.accept()
    game_id = gameManager.new()
    gameManager.get(game_id).connect_host(ws)
    await ws.send_json({
        "game_id": game_id
    })
    while True:
        res = await ws.receive()
        if res['type'] == 'websocket.disconnect':
            await gameManager.get(game_id).disconnect(ws)
            gameManager.remove(game_id)
            return


@router.websocket("/game/{game_id}/ws")
async def player(ws: WebSocket, game_id: str):
    await ws.accept()
    if gameManager.validId(game_id) == False:
        await ws.close(1003, "Game doesn't exit")
        return

    gameManager.get(game_id).connect_player(ws)

    while True:
        res = await ws.receive()
        if res['type'] == 'websocket.receive':
            gameManager.get(game_id).update_state(ws, json.loads(res['text']))
            await gameManager.get(game_id).send_state()
        if res['type'] == 'websocket.disconnect':
            await gameManager.get(game_id).disconnect(ws)
            await gameManager.get(game_id).send_state()
            return
