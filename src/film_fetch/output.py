from math import ceil, floor

from rich.console import Console
from rich.table import Table
from rich.text import Text

from .genre_ids import GENRE_IDS


# Plaintext output
def print_raw(person, films) -> None:
    print(f"\n★★★★★ FILMS STARRING: {person.get('name')} ★★★★★")
    for film in films:
        print(f"{film.get('title')} ({film.get('release_date')})")


# Table formatted output
def print_formatted(person, films) -> None:
    title = Text(f"\n★★★★★ FILMS STARRING: {person.get('name')} ★★★★★")
    title.stylize("yellow", 1, 6)  # Style beginning stars
    title.stylize("yellow", -5)  # Style end stars

    table = Table(
        title=title,
        show_lines=True,
    )

    table.add_column("Date", justify="right", highlight=True, no_wrap=True)
    table.add_column("Title", style="italic")
    table.add_column("Genres")
    table.add_column("Rating", style="yellow")
    table.add_column("Popularity")

    # Add films to table
    for film in films:
        # Convert genre ids to names
        genres = ", ".join([GENRE_IDS[id] for id in film.get("genre_ids")])

        # Add rows to table
        table.add_row(
            film.get("release_date"),
            film.get("title"),
            genres,
            get_stars(film.get("weighted_average")),
            str(film.get("popularity")),
        )

    Console().print(table)


# Converts rating to stars
def get_stars(avg) -> str:
    rounded_avg = ceil(avg)

    res = "★" * floor(rounded_avg / 2)
    if rounded_avg % 2:
        res += "½"

    return res
