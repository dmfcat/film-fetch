import os
import sys

import requests
import tmdbsimple as tmdb
from dotenv import load_dotenv


# Fetch list of people, depending on the search term
def query_person(person) -> list:
    try:
        response = tmdb.Search().person(query=person)
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError("Invalid API key")

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
# NOTE: Will return unreleased films (potentially unwanted)
def query_films(person) -> list:
    try:
        if person.get("dept") != "Acting":
            films = tmdb.People(person.get("id")).movie_credits().get("crew")
            # NOTE: Need to filter by department, otherwise any sort of crew credit gets included
            response = [
                film for film in films if film.get("department") == person.get("dept")
            ]
        else:
            response = tmdb.People(person.get("id")).movie_credits().get("cast")

    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError("Invalid API key")

    return response


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
