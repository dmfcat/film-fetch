# NOTE: Make sure requests don't go over API limit
# TODO: Reformat results with rich
# TODO: Print formatted results
# TODO: Add more options? Ordering, release year, etc...
# TODO: Add option to results allowing user to query again or quit
# TODO: Add 'first start' option, prompting user to get their own API key
# NOTE: Extra features?
# TODO: Add reorder field to results?
# TODO: Add export option to results, export as .csv?

from .output import print_raw
from .user_input import confirm_person, get_info, get_person


def run_app() -> None:
    people = get_person()
    person = confirm_person(people)
    films = get_info(person)

    print_raw(person, films)
