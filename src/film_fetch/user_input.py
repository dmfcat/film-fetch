import sys

import questionary
from questionary import Choice

from .filter import filter_films
from .query import query_films, query_person

# Hardcoded genres and ids
# NOTE: Could query TMDB for this list as well, hardcoded to prevent unnecessary API calls
GENRES = {
    "Action": 28,
    "Adventure": 12,
    "Animated": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Sci-Fi": 878,
    "Thriller": 53,
    "TV Movie": 10770,
    "War": 10752,
    "Western": 37,
}


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

    print(f"You have selected {person}")

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

    # Convert to year to None if empty
    if year == "":
        year = None

    # TODO: Ordering
    # NOTE: Probably a better way to do this, shouldn't be using weird unicode symbols in strings
    order = questionary.select(
        "Select order:",
        choices=[
            "Year ↑",
            "Year ↓",
            "Popularity ↑",
            "Popularity ↓",
            "Rating ↑",
            "Rating ↓",
        ],
    )

    # Query, then filter based on selection, errors if nothing found
    try:
        films = query_films(person)
        return filter_films(films, genres, year, order)
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
