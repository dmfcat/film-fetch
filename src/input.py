import questionary
from questionary import Choice

from query import query_person


def get_person() -> dict:
    people = query_person(questionary.text("Enter cast or crew:").ask())

    # WARNING: Will crash if no one found!!!
    # Ask user to confirm selection if more than 1 result
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
