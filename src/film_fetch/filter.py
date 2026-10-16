SORT_OPTIONS = {
    "Year": "release_date",
    "Rating": "vote_average",
    "Popularity": "popularity",
}


def filter_films(filmography, genres, year) -> list:
    res = []

    # Filter filmography based on arguments after person_id
    #  NOTE: Violating DRY here
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

    return res


def sort_films(films, order) -> list:
    order = order.split()
    ele = SORT_OPTIONS[order[0]]

    if "(Ascending)" == order[1]:
        films.sort(key=lambda film: film[ele])
    else:
        films.sort(key=lambda film: film[ele], reverse=True)

    return films
