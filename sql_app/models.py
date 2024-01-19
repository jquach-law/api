from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team = Column(String, index=True)
    position = Column(String, index=True)
    games_played = Column(Integer, default=0)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    points = Column(Integer, default=0)
    plus_minus = Column(Integer, default=0)
    PIM = Column(Integer, default=0)
    PPG = Column(Integer, default=0)
    SHG = Column(Integer, default=0)
    GWG = Column(Integer, default=0)
    past_teams = Column(String, default=Column('team'))

