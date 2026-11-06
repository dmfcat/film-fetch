# Film Fetch

A CLI Python tool that gets the filtered filmography of any cast/crew based on user given genres, and release year. Results can be ordered by popularity, ratings, or year.

## Features

- Easy to use and visually appealing CLI tool.
- Queries the TMDB database for the filmography of any cast/crew.
- Allows for easy filtering based on genre and year
- Easy to read and informative table output

## Demo Video

![Demo](demo/demo.gif)

## Getting Started

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

## Usage

Simply enter a name when prompted, if the person exists you will then be asked to select genres, year and how you would like the table ordered. As shown in the demo video above.

## How It Works

See the below UML sequence diagram for an overview of what this app does:

<img width="533" height="934" alt="sequence diagram" src="https://github.com/user-attachments/assets/e3d4cb62-a182-4729-9c5d-64d2eb1857a0" />

The TMDB API is queried twice, first to get the selected person and a second time to get their filmography, which then gets filtered depending on the selected genres and year.

## Future Improvements

A few additional improvements include:

- Adding unitests to try and catch any more bugs.
- Ability to customise the output table (possibly via `.yaml` or `.toml`).
- More filters, user should be able to filter out unreleased films or films without a release date.
- Add the option to search for films containing two or more cast/crew.
- Additional options after generating the table (e.g. ability to reorder, or create a new query).
- Add an export option to the above options, so the user can generate `.csv` or `.pdf` file based on the output.

## Licence

[MIT](LICENCE)
