import os

import tmdbsimple as tmdb
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
tmdb.API_KEY = os.environ["API_KEY"]


# WARNING: Will crash if no one found!!!
# NOTE: Will return an arbitrary amount of people, might want to limit to 5
def query_person(person) -> list:
    search = tmdb.Search()
    response = search.person(query=person)

    # Append results to list
    res = []
    for r in response.get("results"):
        res.append(
            {
                "id": r.get("id"),
                "name": r.get("name"),
                "dept": r.get("known_for_department"),
            }
        )

    return res


def query_films():
    return
