import os

import requests
from dotenv import load_dotenv

# Loading env variables
load_dotenv()
BASE_URL = "https://api.themoviedb.org/3"
KEY = os.environ["API_KEY"]


# Fetch list of people, depending on the search term
def query_person(person: dict) -> list:
    # API call
    try:
        response = requests.get(
            f"{BASE_URL}/search/person",
            params={"query": person, "api_key": KEY},
            timeout=15,
        )
        response.raise_for_status()

    except requests.HTTPError as e:
        raise requests.HTTPError(e)

    people = response.json().get("results", [])

    # NOTE: Max of 10 people included in the selection
    res = [
        {
            "id": p.get("id"),
            "name": p.get("name"),
            "dept": p.get("known_for_department"),
        }
        for p in people[:10]
    ]

    # Error if no results
    if not res:
        raise ValueError(f"No results for '{person}' found")

    return res


# Fetch filmography based on person_id
# NOTE: Will return unreleased films (potentially unwanted)
def query_films(person: dict) -> list:
    person_id = person["id"]
    # API Call
    try:
        response = requests.get(
            f"{BASE_URL}/person/{person_id}/movie_credits",
            params={"api_key": KEY},
            timeout=15,
        )
        response.raise_for_status()

    except requests.HTTPError as e:
        raise requests.HTTPError(e)

    credits = response.json()

    # Get correct roles for person
    if person.get("dept") != "Acting":
        films = credits.get("crew")
        # NOTE: Need to filter by department, otherwise any sort of crew credit gets included
        res = [film for film in films if film.get("department") == person.get("dept")]

    else:
        res = credits.get("cast")

    return res
