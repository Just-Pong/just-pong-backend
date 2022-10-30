from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
async def get():
    return "Hello world"

@app.websocket("/ws")
def ws(ws: WebSocket):
    ws.accept();    

