import os
import sys

import tmdbsimple as tmdb
from dotenv import load_dotenv


# Fetch list of people, depending on the search term
# BUG: Will crash if invalid API key, need try except
def query_person(person) -> list:
    response = tmdb.Search().person(query=person)

    res = []
    # NOTE: Max of 10 people included in the selection
    for r in response.get("results")[:10]:
        res.append(
            {
                "id": r.get("id"),
                "name": r.get("name"),
                "dept": r.get("known_for_department"),
            }
        )

    # Error if no results
    if not res:
        raise ValueError(f"No results for '{person}' found")

    return res


# Fetch filmography based on person_id
# BUG: Doesn't grab directorial credits (check for Directing job in movie_credits() ? person job is in "known_for_department")
# NOTE: Will return unreleased films (potentially unwanted)
def query_films(person) -> list:
    return tmdb.People(person.get("id")).movie_credits().get("cast")


# Tries to load API key from .env
def load_api_key() -> None:
    load_dotenv()
    try:
        tmdb.API_KEY = os.environ["API_KEY"]
    except KeyError:
        print("KEYERROR: No API KEY detected")
        print(
            "Please consult README.md for instructions on how to obtain a key and set it up"
        )
        print("See: https://github.com/dmfcat/film-fetch/ for more details")
        sys.exit(1)
