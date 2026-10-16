from rich.console import Console
from rich.table import Table


# Plaintext output
def print_raw(person, films):
    print(f"*** FILMS STARRING: {person.get('name')} ***")
    for film in films:
        print(f"{film.get('title')} ({film.get('release_date')})")


# Table formatted output with rich
def print_formatted(person, films):
    print(films)

    table = Table(
        title=f"*** FILMS STARRING: {person.get('name')} ***", highlight=True, leading=1
    )

    table.add_column("Date", justify="right", no_wrap=True)
    table.add_column("Title")
    table.add_column("Genres")
    table.add_column("Rating")
    table.add_column("Popularity")

    # Add films to table
    # TODO: Should get names for the ids
    for film in films:
        table.add_row(
            film.get("release_date"),
            film.get("title"),
            str(film.get("genre_ids")),
            str(film.get("vote_average")),
            str(film.get("popularity")),
        )

    console = Console()
    console.print(table)
