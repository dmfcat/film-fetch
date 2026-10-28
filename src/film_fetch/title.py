from rich.console import Console
from rich.text import Text


# Prints title ASCII art
def print_title() -> None:
    console = Console()

    with open("src/film_fetch/assets/title.txt") as f:
        text = Text(f.read(), justify="center")
        text.stylize("bold red")
        console.print(text)
