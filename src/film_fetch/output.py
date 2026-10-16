from rich.console import Console
from rich.table import Table


# Plaintext output
def print_raw(person, films):
    print(f"*** FILMS STARRING: {person.get('name')} ***")
    for film in films:
        print(f"{film.get('title')} ({film.get('release_date')})")


# Table formatted output with rich
def print_formatted(person, films):
    table = Table(
        title=f"*** FILMS STARRING: {person.get('name')} ***", highlight=True, leading=1
    )

    table.add_column("Date", justify="right", no_wrap=True)
    table.add_column("Title")

    # Add films to table
    for film in films:
        table.add_row(film.get("release_date"), film.get("title"))

    console = Console()
    console.print(table)
