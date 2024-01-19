from sqlalchemy.orm import Session
from sqlalchemy import desc, asc, func

from . import models, schemas

# Get all players
def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Player).offset(skip).limit(limit).all()

# Get a player's stats
def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.player_id == player_id).first()

# Get most of any stats
def get_most(db: Session, input: str, skip: int = 0, limit: int = 10):
    result = eval(f"db.query(models.Player).order_by(desc(models.Player.{input})).offset(skip).limit(limit).all()")
    return result

# Get most by team of any stats
def get_team_most(db: Session, input: str, skip: int = 0, limit: int = 10):
    # Query databse, returns list of tuples
    data = eval(f"db.query(models.Player.team, func.sum(models.Player.{input}).label('{input}'))\
        .group_by(models.Player.team)\
        .order_by(desc('{input}'))\
        .offset(skip).limit(limit).all()"
    )
    # Convert tuple to dictionary for JSON
    result = list()
    for row in data:
        result.append({
            'team': row[0],
            f"{input}": row[1]
        })

    return result

# Get who switched the most teams
def get_most_switched(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).order_by(desc(func.length(models.Player.past_teams))).offset(skip).limit(limit).all()