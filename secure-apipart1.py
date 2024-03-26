import pandas as pd
from fastapi import FastAPI, HTTPException, Header, Path

#read data from csv file
df = pd.read_csv('players.csv')

#make fastapi instance
app = FastAPI()

#add api key
API_KEY = 'ini_password'

#make home page
@app.get('/')
def home():
    return {'message':'Welcome to players API'}

#get all data
@app.get('/players')
def all_players(api_key:str = Header(None)):
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(401,detail="Not Authorized")
    else:    
        return df.to_dict(orient='records')
    
#get the player by the state
@app.get('/players/state/{state}')
def getPlayersByState(state:str, api_key:str = Header(None)):
    print(api_key)
    print(state)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(401,detail="Not Authorized")
    else:    
        playerState = df[df['state'] == state]
        return playerState.to_dict(orient='records')
    
#get the player by year
@app.get('/players/year/{year}')
def getPlayersByYear(year:str, api_key:str = Header(None)):
    print(api_key)
    print(year)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(401,detail="Not Authorized")
    else:    
        playerYear = df[df['year'] == year]
        return playerYear.to_dict(orient='records')
    
#get the player by position
@app.get('/players/position/{position}')
def getPlayersByPosition(position:str, api_key:str = Header(None)):
    print(api_key)
    print(position)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(401,detail="Not Authorized")
    else:    
        playerPosition = df[df['position'] == position]
        return playerPosition.to_dict(orient='records')
    

#get the player by id
@app.get('/players/id/{id}')
def getPlayersById(id:int, api_key:str = Header(None)):
    print(api_key)
    print(id)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(401,detail="Not Authorized")
    else:    
        playerId = df[df['id'] == id]
        return playerId.to_dict(orient='records')
    
#delete players
@app.delete('/players/delete/{id}')
def delPlayers(id:int, api_key:str = Header(None)):
    """
    DELETE PLAYERS BY ID
    """
    print(id)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(401,detail="Not Authorized")
    else:    
        if id not in df['id'].values:
            raise HTTPException(status_code=404,detail=f"{id} gada bang")
        else:
            df.drop(df[df['id'] == id].index, inplace=True)
        return {"message":f"player dengan id {id} udah dihapus bang"}