# Website side
Connect at:  
`ws://<ip>:<port>/game/host/ws`

Position updates also include the game id  
Possible position range 0-100  
If a player is not connected the position will `-1`
```json
{
    "game_id": "zRJxriL5",
    "player_1": 0.0,
    "player_2": 0.0
}
```

## Mock data

Connect at:  
`ws://<ip>:<port>/dev/host/ws`

Sends random positions between `0-100`.  
Does not simulate disconnected player.

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


