# Prints title ASCII art
def print_title() -> None:
    with open("src/film_fetch/assets/title.txt") as f:
        print(f.read())
