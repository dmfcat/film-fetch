# NOTE: Potential extra features?
# TODO: Enchnce formatted output (more colours?)
# TODO: Add option to results allowing user to query again, reorder or quit
# TODO: Add export option to results, export as .csv?
# TODO: Allow for searching for multiple cast/crew

from .output import print_formatted
from .query import load_api_key
from .title import print_title
from .user_input import confirm_person, get_info, get_person


def run_app() -> None:
    load_api_key()

    print_title()

    people = get_person()
    person = confirm_person(people)
    films = get_info(person)

    print_formatted(person, films)
