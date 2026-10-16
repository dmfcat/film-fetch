def filter_films(filmography, genres, year, order):
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

    # TODO: Order list

    # NOTE: Could include what the selection was in the error message
    if res == []:
        raise ValueError("No films found based on selection")

    return res
