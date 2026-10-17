import sys

import questionary
from questionary import Choice

from .filter import filter_films, sort_films
from .genre_ids import GENRES
from .query import query_films, query_person


# Returns list of people based on search term
def get_person() -> list:
    term = questionary.text("Enter cast or crew:").ask()
    try:
        return query_person(term)
    except ValueError as e:
        print(e)
        sys.exit(1)


# Ask user to confirm selection if more than 1 result
# NOTE: Could pass the entire person json back here to prevent having to query the API twice
# NOTE: Might not get an exhaustive list of films from the first query however
# BUG: CTRL+C out of the selection will result in a ValueError from None
def confirm_person(people) -> dict:
    if len(people) > 1:
        person = questionary.select(
            "Confirm selection:",
            choices=[
                Choice(title=f"{p.get('name')} ({p.get('dept')})", value=p)
                for p in people
            ],
        ).ask()
    else:
        person = people[0]

    return person


# Gets additional info, for filtered person's filmography
def get_info(person) -> list:
    # Genres
    genre_names = questionary.checkbox("Select genres:", choices=list(GENRES)).ask()
    genres = [GENRES.get(g) for g in genre_names]

    # Release year
    year = questionary.text(
        "Enter year: (leave blank for none)", validate=validate_year
    ).ask()

    # Convert year to None if empty
    if year == "":
        year = None

    # Ordering
    order = questionary.select(
        "Select order:",
        choices=[
            "Year (Descending)",
            "Year (Ascending)",
            "Rating (Descending)",
            "Rating (Ascending)",
            "Popularity (Descending)",
            "Popularity (Ascending)",
        ],
    ).ask()

    # Query, then filter based on selection, errors if nothing found
    try:
        films = filter_films(query_films(person), genres, year)
        return sort_films(films, order)
    except ValueError as e:
        print(e)
        sys.exit(1)


def validate_year(year):
    # No answer
    if year == "":
        return True

    # Invalid length
    if len(year) != 4:
        return "Enter valid year"

    # Try to convert year to int
    try:
        int(year)
        return True
    except ValueError:
        return "Enter valid year"
