from fastapi import WebSocket


class Game:
    host_ws: WebSocket
    player_1_ws: WebSocket
    player_2_ws: WebSocket

    def __init__(self) -> None:
        self.host_ws = None
        self.player_1_ws = None
        self.player_2_ws = None

        self.player_1_pos = -1
        self.player_2_pos = -1

    def connect_host(self, ws: WebSocket):
        self.host_ws = ws

    def end(self):
        if self.player_1_ws is not None:
            self.player_1_ws.close()
        if self.player_2_ws is not None:
            self.player_2_ws.close()
        if self.host_ws is not None:
            self.host_ws.close()

    def connect_player(self, ws: WebSocket):
        if self.player_1_ws is None:
            self.player_1_ws = ws
        elif self.player_2_ws is None:
            self.player_2_ws = ws
        else:
            ws.close(reason="Got all players")

    async def send_state(self):
        if self.host_ws is not None:
            await self.host_ws.send_json({
                "player_1": self.player_1_pos,
                "player_2": self.player_2_pos,
            })

    def update_state(self, ws: WebSocket, data):
        if ws == self.player_1_ws:
            self.player_1_pos = data['position']
        elif ws == self.player_2_ws:
            self.player_2_pos = data['position']

    async def disconnect(self, ws: WebSocket):
        if ws == self.player_1_ws:
            self.player_1_ws = None
            self.player_1_pos = -1
        elif ws == self.player_2_ws:
            self.player_2_ws = None
            self.player_1_pos = -1
        else:
            self.host_ws = None
            if self.player_1_ws is not None:
                await self.player_1_ws.close(1001, "Host disconnected")
            if self.player_2_ws is not None:
                await self.player_2_ws.close(1001, "Host disconnected")
