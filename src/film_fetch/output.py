def print_raw(person, films):
    print(f"*** FILMS STARRING: {person.get('name')} ***")
    for f in films:
        print(f"{f.get('title')} ({f.get('release_date')})")
