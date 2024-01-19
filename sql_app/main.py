from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, edit_csv, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

edit_csv.import_csv()

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Existing stats column titles
exist_stats = {'games_played', 'goals', 'assists', 'points', 'plus_minus', 'PIM', 'PPG', 'SHG', 'GWG'}

# Get all players
@app.get("/players/", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_query = crud.get_players(db, skip=skip, limit=limit)
    if db_query is None:
        raise HTTPException(status_code=404, detail="Information not found")
    return db_query

# Get a player's stats
@app.get("/players/{player_id}", response_model=schemas.Player)
def player_stats(player_id: int, db: Session = Depends(get_db)):
    db_query = crud.get_player(db, player_id=player_id)
    if db_query is None:
        raise HTTPException(status_code=404, detail="Information not found")
    return db_query

# Get most of any stats
@app.get("/most/{stat_name}", response_model=list[schemas.Player])
def read_most(stat_name: str, skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    if stat_name in exist_stats:
        db_query = crud.get_most(db, input=stat_name, skip=skip, limit=limit)
        if db_query is None:
            raise HTTPException(status_code=404, detail="Information not found")
        return db_query
    else:
        raise HTTPException(status_code=404, detail="Invalid stats query name")

# Get most of any stats by team
@app.get("/team/most/{stat_name}")
def read_team_most(stat_name: str, skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    if stat_name in exist_stats:
        db_query = crud.get_team_most(db, input=stat_name, skip=skip, limit=limit)
        if db_query is None:
            raise HTTPException(status_code=404, detail="Information not found")
        return db_query
    else:
        raise HTTPException(status_code=404, detail="Invalid stats query name")

# Get who switched the most team
@app.get("/switched/most", response_model=list[schemas.Player])
def read_switched(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    db_query = crud.get_most_switched(db)
    if db_query is None:
        raise HTTPException(status_code=404, detail="Information not found")
    return db_query