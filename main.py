from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get():
    return {"Hello ": "world"}


@app.websocket("/ws")
async def ws(websocket: WebSocket):
    ws.accept()
    while True:
        try:
            data = await websocket.receive_json()
            print(data)
            await websocket.send_json(data)
        except WebSocketDisconnect:
            print("\nDisconected\n")
