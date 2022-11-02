from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from game_manager import GameManager

router = APIRouter()
gameManager = GameManager()

# TODO trace and fix receive call after Disconnect
@router.websocket("/game/host/ws")
async def host(ws: WebSocket):
    await ws.accept()
    id = gameManager.new()
    gameManager.get(id).connect_host(ws)
    await ws.send_json({
        "game_id": id
    })
    while True:
        try:
            await ws.receive()
        except WebSocketDisconnect:
            await gameManager.get(id).disconnect(ws)
            gameManager.remove(id)
            break


@router.websocket("/game/{game_id}/ws")
async def player(ws: WebSocket, game_id: str):
    await ws.accept()
    if not gameManager.validId(game_id):
        await ws.close(reason="Game doesn't exit")
        return

    gameManager.get(id).connect_player(ws)

    while True:
        try:
            data = await ws.receive_json()
            gameManager.get(game_id).update_state(ws, data)
            await gameManager.get(game_id).send_state()
        except WebSocketDisconnect:
            await gameManager.get(id).disconnect(ws)
            break

