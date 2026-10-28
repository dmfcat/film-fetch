# Maps sort options to their associated key
SORT_OPTIONS = {
    "Year": "release_date",
    "Rating": "weighted_average",
    "Popularity": "popularity",
}


def filter_films(filmography, genres, year) -> list:
    res = []

    # Filter filmography based on arguments after person_id
    # NOTE: Violating DRY here
    if year == None:
        for film in filmography:
            if any(genre in genres for genre in film.get("genre_ids")):
                res.append(film)

    else:
        for film in filmography:
            if (
                any(genre in genres for genre in film.get("genre_ids"))
                and year in film.get("release_date")[:4]
            ):
                res.append(film)

    # NOTE: Could include what the selection was in the error message
    if res == []:
        raise ValueError("No films found based on selection")

    return add_weighted_ratings(res)


# Adds weighted Bayesian average (v/(v+m) * R)+(m/(v+m) * C)
def add_weighted_ratings(films) -> list:
    m = 100
    c = 6  # This is meant to represent the mean average, arbitrary assumed value
    for film in films:
        v = film.get("vote_count") or 0
        r = film.get("vote_average") or c
        film["weighted_average"] = v / (v + m) * r + (m / (v + m) * c)

    return films


def sort_films(films, order) -> list:
    order = order.split()
    ele = SORT_OPTIONS[order[0]]

    if order[1] == "(Ascending)":
        films.sort(key=lambda film: film[ele])
    else:
        films.sort(key=lambda film: film[ele], reverse=True)

    return films
