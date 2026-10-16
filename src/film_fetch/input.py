import sys

import questionary
from questionary import Choice

from .query import query_person


def get_person() -> list:
    try:
        return query_person(questionary.text("Enter cast or crew:").ask())
    except ValueError as e:
        print(e)
        sys.exit(1)


# Ask user to confirm selection if more than 1 result
def check_person(people) -> dict:
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


def get_info() -> None:
    return
