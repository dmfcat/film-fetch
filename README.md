## Film Fetch

CLI tool that gets the filtered filmography based on cast/crew, genres, and release year. Results can be ordered by popularity, ratings, or release year.

This tool offers an easy way to look up the filmography of any actor, director, or other crew from the terminal and outputs an easily readable table. I consider myself both a film buff and a fan of the terminal, which is why I opted for a CLI tool.

## Running

Make sure you have [Python](https://www.python.org/downloads/), [git](https://git-scm.com/install/) and [uv](https://docs.astral.sh/uv/getting-started/installation/) installed. Then run the following commands in your terminal:

1. Clone the repo

```bash
git clone https://github.com/dmfcat/film-fetch
cd film-fetch
```

2. Install dependencies

```bash
uv sync
```

3. Run the application

```bash
uv run film-fetch
```

> [!NOTE]
> You need your own API key to use this app. You can obtain your own key for free from TMDB.
>
> 1. Sign up for a TMDB account: https://www.themoviedb.org/signup
> 2. Request a free personal API key: https://www.themoviedb.org/settings/api
> 3. Go to the API settings and copy and paste your `API Key` into `.env`
>
> An example `.env` file can be found in [`.env.example`](.env.example). Change the placeholder `API_KEY` variable to your key and rename `.env.example` to `.env`
>
> You can optionally create your own `.env` file from the root directory, replacing `YOURKEY` with your personal key, like so:
>
> ```bash
> echo "API_KEY = YOURKEY" > .env
> ```

## How it Works

See the below UML sequence diagram for an overview of what this app does:

<img width="533" height="934" alt="sequence diagram" src="https://github.com/user-attachments/assets/e3d4cb62-a182-4729-9c5d-64d2eb1857a0" />

For a breakdown of what each file does:

- [`main.py`](src/film_fetch/main.py) handles running all the functions in every file.
- [`user_input.py`](src/film_fetch/user_input.py) handles allowing the user to enter information. [`questionary`](https://github.com/tmbo/questionary) is used for assisting the user in entering information. The tool first asks for cast/crew, if multiple matches for a search are found the user is presented a list to select from. If no matches are found the app terminates early. After this the user then picks what genres and release year they want to search for. They are also given an option to choose what order the resulting table is in.
- [`query.py`](src/film_fetch/query.py) handles communicating with the TMDB REST API, [`tmdbsimple`](https://github.com/celiao/tmdbsimple) is used as a wrapper for this API. Information the user inputs from `user_input.py` is used for the queries. The API is queried twice, first to get a list of people, and then to get the entire filmography of the selected person. Before the tool does anything, however, it first 'loads' the API key using [`python-dotenv`](https://github.com/theskumar/python-dotenv). If the API key doesn't exist the app terminates early and the user is directed towards this README to fix the problem.
- [`filter.py`](src/film_fetch/filter.py) filters the list of films obtained from `query.py`, based on the selected genres and release year. The code for sorting the filmography is also in this file.
- [`output.py`](src/film_fetch/output.py) contains the code for outputting the filtered filmography. [`rich`](https://github.com/Textualize/rich) is used for formatting, the outputted filmography is in a table.
- [`genre_ids.py`](src/film_fetch/genre_ids.py) contains two constants, one mapping genre names to their TMDB ID number and other doing the opposite. These constants are used by `filter.py` and `output.py`.

## Future Improvements

A few additional improvements include:

- Adding unitests to try and catch any more bugs.
- Ability to customise the output table (possibly via `.yaml` or `.toml`).
- Enhanced table output (e.g. more colours, ASCII art, more useful popularity output (the numbers could be confusing)).
- More filters, user should be able to filter out unreleased films or films without a release date.
- Add the option to search for films containing two or more cast/crew.
- Additional options after generating the table (e.g. ability to reorder, or create a new query).
- Add an export option to the above options, so the user can generate `.csv` or `.pdf` file based on the output.
- Further code optimisation, some functions have repeated code.

## Demo Video

![Demo](demo.gif)

## Third Party Dependencies

- [`python-dotenv`](https://github.com/theskumar/python-dotenv)
- [`questionary`](https://github.com/tmbo/questionary)
- [`rich`](https://github.com/Textualize/rich)
- [`tmdbsimple`](https://github.com/celiao/tmdbsimple)
- [`requests`](https://github.com/psf/requests)

## Licence

[GPLv3](LICENCE)
