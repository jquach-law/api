# Hockey API
RESTful Backend API built with FastAPI, SQLalchemy with Python's built-in database SQLite

## Development Tools
* FastAPI
* Python 3.10+ (version requirement)
* SQLalchemy
* SQLite
* Pandas

## Docker Run
cd to where the Dockfile is (outside of sql_app folder):
```bash
docker build -t hockeyimage .
docker run -d --name mycontainer -p 90:90 hockeyimage
```

## Local Install & Run
Please create a virtual environment before following step(s).
cd outside of the sql_app folder:
```bash
pip install -r requirements.txt
uvicorn sql_app.main:app --reload
```

## Selective CSV
I only used the first 13 columns of the CSV - up to and including 'GWG' column

## Endpoints Query
Please use /docs to interact with the endpoints. 
Click endpoint, and click "Try it out" and fill out neccessary information for query

There are 5 endpoints:
1. /players/ returns all players
2. /players/{player_id} takes ID and returns a player's stats
3. (and 4. as well) /most/{stat_name} and /team/most/{stat_name} can query any of the following stats:
```bash
# Existing stats column titles
exist_stats = {'games_played', 'goals', 'assists', 'points', 'plus_minus', 'PIM', 'PPG', 'SHG', 'GWG'}
```
5. /switched/most/ shows who switched team the most

## Development Summary + Review
I explored deeper and included new methods and techs:
1. The application is self-contained. No external database. It uses Python's built-in SQLite that uses client's storage.
2. Using FastAPI's Pydantic model (schemas.py) to generate query structure for /docs
3. Using SQLalchemy's Session
4. Accepts JSON query bodies (not just URL in-line query)
