from .database import engine

import pandas as pd


def import_csv():
    # Read csv
    df = pd.read_csv("sql_app/hockey_data.csv")

    # Select first 13 columns
    df = df.iloc[:, 0:13]

    # Modify columns
    df['past_teams'] = df['Team']
    df = df.rename(columns={
        'playerId': 'player_id',
        'Name': 'name',
        'Team': 'team',
        'Pos': 'position',
        'GP': 'games_played',
        'G': 'goals',
        'A': 'assists',
        'P': 'points',
        '+/-': 'plus_minus'
        })
    df['team'] = df['team'].str[-3:]

    # Export columns to SQLite database
    df.to_sql("players", con=engine, if_exists="replace", index=False)
