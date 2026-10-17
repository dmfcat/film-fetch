## Film Fetch

CLI tool that gets the filtered filmography based on cast/crew, genres and release year. Results can be ordered by popularity, ratings or release year.

This tool offers an easy way to lookup the filmography of any actor, director, or other crew from the terminal and outputs an easily readable table.

## Running

Make sure you have [Python](https://www.python.org/downloads/), [git](https://git-scm.com/install/) and [uv](https://docs.astral.sh/uv/getting-started/installation/) installed. Then run the following commands in your terminal:

1. Clone the repo

```bash
git clone https://github.com/dmfcat/film-fetch
cd film-fetch
```

2. Run the application

```bash
uv run film-fetch
```

> [!NOTE]
> You need your own API key to use this app. You can obtain your own key for free from TMDB.
>
> 1. Sign-up for a TMDB account: https://www.themoviedb.org/signup
> 2. Request a free personal API key: https://www.themoviedb.org/settings/api
> 3. Go to the API settings and copy and paste your `API Key` into `.env`
>
> An example `.env` file can be found in [`.env.example`](.env.example). Change the placeholder `API_KEY` variable to your key and rename `.env.example` to `.env`
>
> You can optionally create your own `.env` file from within the `film-fetch` directory, replacing `YOURKEY` with your personal key, like so:
>
> ```bash
> echo "API_KEY = YOURKEY" > .env
> ```

## How it Works

See the below UML sequence diagram for an overview of what this app does:

<img width="533" height="934" alt="seqdiagram" src="https://github.com/user-attachments/assets/84d49380-2588-409a-8b8a-48b941656dc0" />

For a breakdown of what each file does:

- [`main.py`](src/film_fetch/main.py) is responsible for running all the functions in every file.
- [`user_input.py`](src/film_fetch/user_input.py) is responsible for allowing the user to enter information. [questionary](https://github.com/tmbo/questionary) is used to assist the user in entering information. The tool first asks for cast/crew, if multiple matches for a search are found the user is presented a list to select from. If no matches are found the app terminates early. After this the user then picks what genres and release year they want to search for. They are also given an option to choose what order the resulting table is in.
- [`query.py`](src/film_fetch/query.py) is responsible for communicating with the TMDB REST API, [tmdbsimple](https://github.com/celiao/tmdbsimple) is used as a wrapper for this API. Information the user inputs from `user_input.py` is used for the queries. The API is queried twice, first to obtain a list of people, and then to obtain the entire filmography of the selected person. Before the tool does anything, however, it first 'loads' the API key using [python-dotenv](https://github.com/theskumar/python-dotenv). If the API key doesn't exist the app terminates early and the user is directed towards this README to fix the problem.
- [`filter.py`](src/film_fetch/filter.py) filters the list of films obtained from `query.py`, the filmography obtained from the second query is filtered depending on the selected genres and release year. The code for sorting the filmography is also in this file.
- [`output.py`](src/film_fetch/output.py) contains the code for outputing the filtered filmography. [rich](https://github.com/Textualize/rich) is used for formatting, the outputted filmography is in a table.
- [`genre_ids.py`](src/film_fetch/genre_ids.py) contains two constants, one mapping genre names to their TMDB id number and other doing the opposite. These constants are used by `filter.py` and `output.py`.

## Future Improvements

Some future improvements ideas are currently in the comments of `main.py`, to reiterate:

- Enhanced table output (e.g. more colours, ASCII art, unicode star symbols in place of number ratings (i.e. ★ and ☆), more useful popularity output (the numbers could be confusing))
- Additional options after generating the table (e.g. ability to reorder, or create a new query)
- Add an export option to the above options, so the user can generate `.csv` or `.pdf` file based on the output
- Add the option to search for films containing two or more cast/crew

## Demo Video

<img width="1200" height="600" alt="demo" src="https://github.com/user-attachments/assets/e133642d-6b3e-4b69-ae41-9e3a9ca0c47d" />

## Third Party Dependencies

- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [questionary](https://github.com/tmbo/questionary)
- [rich](https://github.com/Textualize/rich)
- [tmdbsimple](https://github.com/celiao/tmdbsimple)

## Licence

[GPLv3](LICENCE)
