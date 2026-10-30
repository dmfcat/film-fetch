# Maps sort options to their associated key
SORT_OPTIONS = {
    "Year": "release_date",
    "Rating": "weighted_average",
    "Popularity": "popularity",
}


# Filter filmography based on arguments after person_id
def filter_films(filmography, genres, year) -> list:
    res = [
        film
        for film in filmography
        if any(genre in genres for genre in film.get("genre_ids"))
        and (year is None or year in film.get("release_date")[:4])
    ]

    # NOTE: Could include what the selection was in the error message
    if not res:
        raise ValueError("No films found based on selection")

    return add_weighted_ratings(res)


# Adds weighted Bayesian average (v/(v+m) * r)+(m/(v+m) * c)
def add_weighted_ratings(films) -> list:
    m = 100  # Represents the cutoff point for minimum votes
    c = 6  # Represents the mean average of every film, arbitrary assumed value
    for film in films:
        v = film.get("vote_count") or 0
        r = film.get("vote_average") or c
        film["weighted_average"] = v / (v + m) * r + (m / (v + m) * c)

    return films


def sort_films(films, order) -> list:
    # Stops errors related to CTRL+Cing out of order selection
    try:
        order = order.split()
    except AttributeError:
        order = ["Year", "(Descending)"]

    # Gets correct sort option
    ele = SORT_OPTIONS[order[0]]

    # Sorts in ascending or descending order
    if order[1] == "(Ascending)":
        films.sort(key=lambda film: film[ele])
    else:
        films.sort(key=lambda film: film[ele], reverse=True)

    return films
