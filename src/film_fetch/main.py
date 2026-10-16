# NOTE: Make sure requests don't go over API limit (Shouldn't happen because limit is quite generous)
# TODO: Add 'first start' option, prompting user to get their own API key
# NOTE: Extra features?
# TODO: Enchnce formatted output (more colours?)
# TODO: Add option to results allowing user to query again, reorder or quit
# TODO: Add export option to results, export as .csv?

from .output import print_formatted
from .user_input import confirm_person, get_info, get_person


def run_app() -> None:
    people = get_person()
    person = confirm_person(people)
    films = get_info(person)

    print_formatted(person, films)
