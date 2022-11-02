### <span style="color:red">Still under development, hasn't been tested</span>

# Website side
Connect at:  
`ws://\<ip>:\<port>/game/host/ws`

The server sendk a json with the game id (string), similar to this
```json
{
	"game_id": "WRgKf82h"
}
```

Position updates  
Possible position range TBD range
```json
{
    "player_1": 0.0,
    "player_2": 0.0
}
```

# Phone side

Connect at:  
`ws://\<ip>:\<port>/game/\<game id>/ws`

If invalid game id is given (meaning no game such game exists) the server will close the connection

Send psoition as:
```json
{
    "possition": 0.0
}
```


