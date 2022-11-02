from fastapi import WebSocket


class Game:
    host_ws: WebSocket
    player_1_ws: WebSocket
    player_2_ws: WebSocket

    def __init__(self) -> None:
        self.host_ws = None
        self.player_1_ws = None
        self.player_2_ws = None

        self.player_1_pos = 0
        self.player_2_pos = 0

    def connect_host(self, ws: WebSocket):
        self.host_ws = ws

    def connect_player(self, ws: WebSocket):
        if self.player_1_ws is None:
            self.player_1_ws = ws
        elif self.player_2_ws is None:
            self.player_2_ws = ws
        else:
            ws.close(reason="Got all players")

    async def send_state(self):
        await self.host_ws.send_json({
            "player_1": self.player_1_pos,
            "player_2": self.player_2_pos,
        })

    def update_state(self, ws: WebSocket, data):
        if ws == self.player_1_ws:
            self.player_1_ws = None
            self.player_1_pos = data['position']
        elif ws == self.player_2_ws:
            self.player_2_ws = None
            self.player_2_pos = data['position']

    async def disconnect(self, ws: WebSocket):
        # TODO add None check before sending
        if ws == self.player_1_ws:
            self.player_1_ws = None
            await self.host_ws.send_text("PLayer 1 disconnected")
        elif ws == self.player_2_ws:
            self.player_2_ws = None
            await self.host_ws.send_text("PLayer 2 disconnected")
        else:
            self.host_ws = None
            await self.player_1_ws.send_text("Host disconnected")
            await self.player_2_ws.send_text("Host disconnected")
