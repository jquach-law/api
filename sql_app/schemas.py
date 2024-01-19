from pydantic import BaseModel


class Player(BaseModel):
    player_id: int
    name: str
    team: str
    position: str
    games_played: int | None = 0
    goals: int | None = 0
    assists: int | None = 0
    points: int | None = 0
    plus_minus: int | None = 0
    PIM: int | None = 0
    PPG: int | None = 0
    SHG: int | None = 0
    GWG: int | None = 0
    past_teams: str | None


    class Config:
        orm_mode = True

