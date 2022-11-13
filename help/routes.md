# Website side
Connect at:  
`ws://<ip>:<port>/game/host/ws`

The server sends a json with the game id (string), similar to this
```json
{
	"game_id": "WRgKf82h"
}
```

Position updates  
Possible position range TBD  
If a player is not connected the position will `-1`
```json
{
    "player_1": 0.0,
    "player_2": 0.0
}
```

## Mock data

Connect at:  
`ws://<ip>:<port>/dev/host/ws`

Sends random positions between `0-1000`.  
Does not simluate disconnected player.

# Phone side

Connect at:  
`ws://<ip>:<port>/game/<game id>/ws`

If invalid game id is given (meaning no game such game exists) the server will close the connection with the code being `1003`

If the host disconnects the player webosckets will be closed with the code being `1001`

### Send position as:
```json
{
    "position": 0.0
}
```


